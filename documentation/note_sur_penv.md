Environnement virtuel : configuration isolée pour votre projet
Maitriser les versions de Python par projet

PIP (Installer des Packages)
Venv (Environnement Virtuel)
Pyenv (gérer plusieurs config, c'est à dire plusieurs installations de Python)


pip list
python3 -m venv venv
.\scripts\activate
deactivate

where python

penv: ges

===========================================================================================
installer penv sur windows

pip install pyenv-win --target %USERPROFILE%\\.pyenv
pip install pyenv-win --target "%USERPROFILE%/.pyenv"

Modification des variables Environnement
dans Path du haut :
supprimer : 
C:\Users\alpha\AppData\Local\Programs\Python\Python311\Scripts\
C:\Users\alpha\AppData\Local\Programs\Python\Python311\
C:\Users\alpha\anaconda3
C:\Users\alpha\anaconda3\Library\mingw-w64\bin
C:\Users\alpha\anaconda3\Library\usr\bin
C:\Users\alpha\anaconda3\Library\bin
C:\Users\alpha\anaconda3\Scripts
c'etait l'installation precedente de Python


dans variable utilisateur :
Creer une nouvelle variable Environnement qui va s'appeler : PYENV
ajouter : 
C:\Users\alpha\.pyenv\pyenv-win


dans variable système du bas
Creer : PYENV
Puis ajouter : %USERPROFILE%\.pyenv\pyenv-win


on retourne dans variable utilisateur
dans path:
ajouter : %PYENV%\bin 
ajouter : %PYENV%\shims

confrmer tout et fermer le terminal

Ensuite : rouvrir le terminal afin qu'il prenne en compte des modification
Taper : python --version
reponse : python n'est pas reconne est la réponse attendue

taper : pyenv
taper : pyenv versions
Normalement on a rien

Taper : pyenv install -l
Tper : pyenv install 3.7.3 ==> pour installer la version 3.7.3
Taper : pyenv install 3.8.0

Taper : pyenv versions ==> pour voir les versions disponibles
pour choisir la version 3.7.3 : 
taper : pyenv global 3.7.3 

python --version  >> attention sans s
pyenv rehash >>> pour dir à Python de refaire les liens


avec Pycharm : 
choisssez l'iterpreteur en pointant sur 
C:\Users\alpha\.pyenv\pyenv-win\version par exemple mais
faut choisir python.exe
 
 ===========================================================================================
 configuration de variables environnement
 ouvrir un terminal :
 se placer à l'emplacement souhaité pour crrer un environnement
 
 pip install virtualenv : installer 
 virtualenv --version : 
 virtualenv django : creer une variable d'environnement
 django\Scripts\activate.bat : activation de variable Environnement
 
 attention : ma variable d'environnement a été installé ici : C:\Users\alpha
 ==========================================================================================
 
 utils
 pip uninstall urllib3
 pip install urllib3<2.0
 
 pyenv install -l
 pyenv install 3.10.5
 pyenv global 3.10.5
 pyenv rehash
 python --version
 pip install virtualenv
 virtualenv --version
 pip install --upgrade pip
 virtualenv web
 web\Scripts\activate.bat
 deactivate
 ==========================================================================================