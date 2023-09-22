conda create --name applications
conda activate applications




git config --global user.name "alphadiop"
git config --global user.email "alphadiop@gmail.com"
git config --global user.email

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/alphadiop/applications.git



Créer et utiliser notre repo GIT
se placer sur le repertoire
Ouvrir un terminal
git init
git status
git add .
git commit -m "message"
git log
git checkout ab1af52abaf483beb0dca1353b21e5bf756bca4e >>>> un commit bien identifié
git checkout master >>>> dernière version


ajouter notre repo sur GitHub
publier le code sur server GitHub
connecter le repo creer avec le repo de GitHub
Faire le lien entre le repo local et le repo GitHub
git branch -M main >>>> vrai nom d'une branche git
git remote add origin https://github.com/alphadiop/applications.git

si token demander


configurer le token
cliquer en haut à droite
aller dans setting
cliquer sur developer settings
aller dans Personal access token
git remote add origin https://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@github.com/alphadiop/applications.git

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


partager le repo avec quelqu'un d'autres
vous lui donnez : https://github.com/alphadiop/applications
la personne creer un repertoire : dev
se positionner dans dev:
ouvrir un terminal
taper : git clone https://github.com/alphadiop/applications