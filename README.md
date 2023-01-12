# P10 API sécurisée RESTful avec Django REST #
## installation: ##
Cette application executable localement peut être installée en suivant les étapes ci-dessous.
1. Cloner le dépôt de code à l'aide de la commande ```$ git clone https://github.com/B-asile/LITreviewP9OC.git``` vous pouvez également télécharger le code en tant qu'archive zip.
2. Créer un environnement virtuel : se rendre à la racine du projet puis effectuer les commandes ```$ python -m venv env``` sous windows ou ```$ python3 -m venv env``` sous macos ou linux.
3. Activer l'environnement virtuel avec ```$ env\Scripts\activate``` sous windows ou ```$ source env/bin/activate``` sous macos ou linux.
4. Installer les dépendances du projet avec la commande ```$ pip install -r requirements.txt```.
5. Démarrer le serveur avec ```$ python manage.py runserver```.

Lorsque le serveur fonctionne, après l'étape 5 de la procédure d'installation, vous pouvez vous rendre sur l'interface de l'API via l'url de base [http://127.0.0.1:8000/](http://127.0.0.1:8000/) , ou tester les point de terminaison via Postman(cf ci-dessous).
Afin de tester l'application quelques utilisateurs sont déjà enregistrer.
La connection via ces utilisateurs se fait avec ces identifiants :
  *  nom d'utilisateur : user1@softdesk.com / mot de passe : Secret 
  *   nom d'utilisateur : georgi4@sofdesk.com / mot de passe : Secret 
  *   nom d'utilisateur : user7@softdesk.com / mot de passe : Secret

6. pour couper le serveur local commande Ctrl + C dans le terminal

7. Pour desactiver l'environnement virtuel commande:  ```$ deactivate``` dans le terminal.

## documentation Postman de l'API: ##
Une documentation Postman contenant des détails sur chaque point de terminaison est disponible via ce lien [https://www.postman.com/b-asile/workspace/softdesk/api/5061e4f6-f15b-411e-980c-5559a1b357c1/documentation/19538644-c5eac461-9f79-458a-bf36-8957620a6969?version=dc5caeff-5eda-47c2-9a02-e60cc0f93db7](SoftDesk_API).
