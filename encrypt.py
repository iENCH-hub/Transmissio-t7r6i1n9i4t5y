#!/usr/bin/env python3
"""Encrypt WAV files for static GitHub Pages distribution."""
import argparse, base64, getpass, json, os, pathlib, sys, io, zipfile
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITERATIONS=600000

def main():
    p=argparse.ArgumentParser(description='Encrypt WAV archives for iENCH GitHub Pages')
    p.add_argument('files', nargs='+', type=pathlib.Path)
    p.add_argument('--output', default='archives', type=pathlib.Path)
    a=p.parse_args()
    pw=getpass.getpass('Clé secrète (12 caractères ou plus recommandés) : ')
    if len(pw)<12: sys.exit('Erreur : clé trop courte (minimum 12 caractères).')
    pw2=getpass.getpass('Confirmer la clé : ')
    if pw!=pw2: sys.exit('Erreur : clés différentes.')
    a.output.mkdir(parents=True, exist_ok=True)
    items=[]
    for i,f in enumerate(a.files,1):
        if not f.exists() or (f.is_file() and f.suffix.lower() not in ('.wav','.zip')):
            sys.exit(f'Entrée non prise en charge : {f} (dossier, WAV ou ZIP attendu)')
        if f.is_dir():
            stream=io.BytesIO()
            with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
                for child in sorted(f.rglob('*')):
                    if child.is_file(): z.write(child,arcname=str(pathlib.Path(f.name)/child.relative_to(f)))
            data=stream.getvalue()
            original_name=f.name+'.zip'
            kind='zip'
        else:
            data=f.read_bytes()
            original_name=f.name
            kind='zip' if f.suffix.lower()=='.zip' else 'wav' 
        salt=os.urandom(16); iv=os.urandom(12)
        key=PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS).derive(pw.encode('utf-8'))
        ciphertext=AESGCM(key).encrypt(iv,data,None)
        filename=f'audio_{i:03d}.bin'
        (a.output/filename).write_bytes(ciphertext)
        items.append({'title':f.stem if f.is_file() else f.name,'file':filename,'name':original_name,'type':kind,'bytes':len(data),'salt':base64.b64encode(salt).decode(),'iv':base64.b64encode(iv).decode()})
        print(f'Chiffré : {f.name} -> {filename}')
    manifest={'version':1,'iterations':ITERATIONS,'tracks':items}
    (a.output/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Terminé. Dépose index.html et le dossier archives/ sur GitHub Pages.')
    print('Attention : les titres et noms des fichiers sont visibles dans le manifeste public.')
if __name__=='__main__':main()
