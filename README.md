# P10 API sécurisée RESTful avec Django REST #
Création d'une API sécurisée(authentification JWT) avec le framwork Django REST pour SoftDesk. 
Application permettant de remonter et suivre des problèmes techniques(issue tracking system). 
Elle permet l'authentification ou la création d'utilisateurs qui aurons accès aux actions basiques de type CRUD sur des projets/issues/comments en fonction des permissions accordées. 

## installation: ##
Cette application executable localement peut être installée en suivant les étapes ci-dessous.
1. Cloner le dépôt de code à l'aide de la commande ```$ https://github.com/B-asile/SoftDesk.git``` vous pouvez également télécharger le code en tant qu'archive zip.
2. Créer un environnement virtuel : se rendre à la racine du projet puis effectuer les commandes ```$ python -m venv env``` sous windows ou ```$ python3 -m venv env``` sous macos ou linux.
3. Activer l'environnement virtuel avec ```$ env\Scripts\activate``` sous windows ou ```$ source env/bin/activate``` sous macos ou linux.
4. Installer les dépendances du projet avec la commande ```$ pip install -r requirements.txt```.
5. Démarrer le serveur avec ```$ python manage.py runserver```.

Lorsque le serveur fonctionne, après l'étape 5 de la procédure d'installation, vous pouvez tester les point de terminaison via Postman [SoftDesk_API](https://www.postman.com/b-asile/workspace/softdesk/api/5061e4f6-f15b-411e-980c-5559a1b357c1/documentation/19538644-c5eac461-9f79-458a-bf36-8957620a6969?version=dc5caeff-5eda-47c2-9a02-e60cc0f93db7).
Afin de tester l'application quelques utilisateurs sont déjà enregistrer dans la base de donnée "sqilte3".
La connection via ces utilisateurs se fait avec ces identifiants :
  *  nom d'utilisateur : user1@softdesk.com / mot de passe : Secret 
  *   nom d'utilisateur : georgi4@sofdesk.com / mot de passe : Secret 
  *   nom d'utilisateur : user7@softdesk.com / mot de passe : Secret

6. pour couper le serveur local commande Ctrl + C dans le terminal

7. Pour desactiver l'environnement virtuel commande:  ```$ deactivate``` dans le terminal.

## documentation Postman de l'API: ##
Une documentation Postman contenant des détails sur chaque point de terminaison est disponible via ce lien [SoftDesk_API](https://www.postman.com/b-asile/workspace/softdesk/api/5061e4f6-f15b-411e-980c-5559a1b357c1/documentation/19538644-c5eac461-9f79-458a-bf36-8957620a6969?version=dc5caeff-5eda-47c2-9a02-e60cc0f93db7).
