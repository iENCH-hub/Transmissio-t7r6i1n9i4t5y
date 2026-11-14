# iENCH // SECURE TRANSMISSION 006

Site statique GitHub Pages : archives WAV chiffrées AES-256-GCM, clé unique partagée.

## Préparation sous Windows

1. Installer Python 3 depuis python.org (cocher « Add Python to PATH »).
2. Dans un terminal, dans ce dossier, lancer : `py -m pip install cryptography`
3. Mettre les WAV à chiffrer dans ce dossier (ou indiquer leur chemin).
4. Lancer : `py encrypt.py "morceau 1.wav" "morceau 2.wav"`
5. Entrer une **phrase secrète longue, unique et difficile à deviner** (idéalement 5 à 7 mots aléatoires ou 20+ caractères), puis confirmer.
6. Le script crée `archives/manifest.json` et `archives/audio_001.bin`, etc.
7. Créer un dépôt GitHub **public**. Y placer `index.html` et le dossier `archives/` (mais **jamais les WAV originaux, ni la clé, ni encrypt.py si tu ne le souhaites pas**).
8. Dans le dépôt : Settings → Pages → Deploy from a branch → main → /(root) → Save.
9. Ouvrir l'adresse GitHub Pages fournie, saisir la clé, télécharger les WAV.

## Pour ajouter ou remplacer des WAV

Relancer `encrypt.py` avec **tous les WAV à publier**, et remplacer entièrement le dossier `archives/` en ligne. Garder la même phrase secrète si tu souhaites conserver le même accès.

## Limites et sécurité

- GitHub Pages rend les fichiers `.bin` et le manifeste publiquement téléchargeables, mais leur **contenu audio reste chiffré** sans la clé.
- Les **titres, noms de fichiers, tailles, nombre de morceaux** restent visibles dans `manifest.json`. Utiliser des noms neutres si nécessaire.
- Toute personne qui possède la clé peut déchiffrer et redistribuer les WAV. Une clé partagée ne permet pas de révoquer une seule personne.
- Si la clé est divulguée, rechiffrer tous les WAV avec une nouvelle clé, supprimer les anciennes archives du dépôt et remplacer les fichiers publiés. Les copies déjà téléchargées ne peuvent pas être rappelées.
- Le déchiffrement se fait dans le navigateur, entièrement en mémoire : éviter les WAV très volumineux sur téléphone. Pour de gros fichiers, prévoir une version à déchiffrement par flux.
- Utiliser HTTPS (GitHub Pages le fournit). Le mot de passe n'est ni envoyé au serveur ni stocké localement.
- Les visiteurs peuvent accéder directement au manifeste et aux fichiers chiffrés, même sans utiliser l'interface.
- GitHub impose des limites de taille aux fichiers ; les fichiers >100 MiB ne peuvent pas être poussés par Git classique, et l'interface web a des limites plus strictes. Pour des WAV volumineux, utiliser un stockage adapté.
- Le premier WAV est entièrement déchiffré à la connexion pour vérifier la clé, puis déchiffré de nouveau lors de son téléchargement.
- Ce système protège la confidentialité du contenu contre une consultation sans clé, pas contre la redistribution par les destinataires autorisés ni contre un code du site modifié par un tiers contrôlant le dépôt.


LOGO iENCH : la page utilise directement le fichier ienchlogo.png du site NODE 004 (URL distante). Pour etre independant, telechargez ienchlogo.png depuis https://iench-hub.github.io/iENCH-SIGNAL-RESTORED/ienchlogo.png, renommez-le ienchlogo.png, placez-le a la racine du depot et remplacez le src de l image par "ienchlogo.png".


## Fond vidéo

Le fichier `transmission-007.mp4` doit être à la racine du dépôt, au même niveau que `index.html`. Il démarre automatiquement sans son, tourne en boucle et reste derrière le terminal. La vidéo est volontairement assombrie pour assurer la lisibilité. Sur certains appareils, le mode économie d’énergie peut empêcher sa lecture automatique.


Logo : logo-iench.png est inclus localement. Publier ce fichier à la racine du dépôt avec index.html et transmission-007.mp4.
