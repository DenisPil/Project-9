# Programme LitReview.

<p align="center">
<img src="https://user.oc-static.com/upload/2020/09/18/16004297044411_P7.png" width="25%"></img>
</p>

## Pour utiliser ce programme il faut commencer par installer l'environnement virtuel.




### 1- Créér l'environnement virtuel :
*  Lancer un terminal et rentrer les commandes suivantes : 

````
$ python -m venv <le nom de l'environnement> (création de l'environnement)    
````

### 2.a- Pour activer l'environnement sur windows :
````
$ <le nom de l'environnement>/Scripts.activate 
````

### OU

### 2.b- Pour activer l'environnement sur linux :

````
$ source <le nom de l'environnement>/bin/activate
````

### 3- La dernière étape est l'installation des packages. Les packages sont référencés dans le fichier
*  requirements.txt. Entrer la commande suivante pour installer tous les packages.
````
$ pip install -r requirements.txt
````

### 4- Une fois l'environnement créé et activé, il faut activer le serveur de développement.
*  À partir d'un terminal la première étape est d'exécuter le serveur.
*  Ce rendre a la racine du projet et rentrer la commande suivante:
````
$ python manage.py runserver
````
* Le serveur est activé, se rendre à l'adresse suivante: http://127.0.0.1:8000/

### 5- Se connecter avec le compte admin.
* se rendre à l'adresse http://127.0.0.1:8000/admin
* Nom d'utilisateur : admin
* Mot de passe : admin1
* Permet de controler les informations suivante de la base de donnée. Pouvoir effectuer les opérations CRUD sur les éléments suivant:
  * Utilisateurs
  * Reviews
  * Tickets 


