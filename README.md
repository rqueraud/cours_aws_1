# Inseec - TP1 : AWS

Connexion à une instance EC2, apprentissage du terminal et entrainement sur Python. 

## Partie 0 : Télécharger les supports de TP 

Consulter l'adresse https://github.com/rqueraud/cours-aws-1 pour télécharger les éléments supports du TP.

## Partie 1 : Lancement d’une instance EC2 

- Se connecter à la console AWS https://eu-west-1.console.aws.amazon.com et sélectionner le service **EC2** dans le menu déroulant de **Services**.
- Cliquer sur **Instances** dans le menu de gauche puis sur **Launch Instance**. 
- Choisir une AMI **Ubuntu 18.04**. 
- Sélectionner une instance de type **t2.micro** puis cliquer sur **Review and Launch**. 
- Créer un nouveau **keypair** puis le télécharger sur son PC.
- Lancer l'instance. 
- Dans la liste des instances, on retrouve l’instance juste lancée. Attendre le démarrage complet puis noter son **IPv4 Public IP**. 

## Partie 2 : SSH avec Bitvise 

Lancer le logiciel BitVise, puis :

- Aller sur l’onglet **Login**.
- Dans server host, renseignez l'**IP publique** de votre instance.
- Dans username, mettre **ubuntu** (propre à l'AMI sélectionnée).
- Cliquer sur **Client Key Manager** et importer votre fichier **.pem**. 
- Sélectionner ensuite votre clé.
- Puis cliquer sur **Login** et sur **Accept and save**.

La fenêtre FTP ainsi qu'un nouveau terminal se lancent, la connexion à l’instance est réussie !

Transférer le fichier **square.py** sur l'instance, puis mettre les paquets à jour avec les commandes :

```bash
sudo apt-get update  # Met à jour la liste des paquets
sudo apt-get upgrade -y  # Met à jour les paquets
```

## Partie 3 : Le terminal Linux
Voici la liste (absolument non exhaustive) des commandes de base. Noter que précéder toute commande par l'instruction `sudo` execute celle-ci en mode administrateur.

```bash
ls # Lister les fichiers du dossier actuel.
mkdir inseec # Créer un dossier.
cd inseec # Se déplacer dans le dossier inseec.
touch inseec.txt # Créer un fichier.
nano inseec.txt # Éditer un fichier.
cat inseec.txt # Afficher le contenu d’un fichier.
rm inseec.txt # Supprimer un fichier.
cd .. # Se déplacer en arrière
rm -rf inseec # Supprimer un dossier
python inseec.py # Exécuter un fichier .py.
wget http://www.inseec.com/data.csv # Télecharger un fichier.
```

Créer un dossier **test**, créer un fichier **hello.txt** dans ce dossier, écrire `Hello world ` dans le fichier, afficher son contenu puis supprimer le fichier et le dossier.

Executer les commandes suivantes pour installer **python** et lancer un script :

```bash
sudo apt-get install –y python-dev  # Install python
python3 square.py 2
```

Créer un nouveau fichier python `cube.py` (directement sur l'instance, **ne pas** réutiliser le **FTP** !) pour calculer le cube de 3 tout en gardant le même système d'arguments.

## Partie 4 : Préparer l'environnement jupyter

Installer le paquet `python3-pip` avec la commande `apt-get` (référez-vous à notre utilisation précédente). `pip` est le gestionnaire de paquets python.

Installer ensuite le paquet python `jupyterlab` en utilisant la commande `pip3 install jupyterlab`.

Ensuite il faudra le configurer pour y accéder à distance en commançant avec les commandes `jupyter-notebook --generate-config` et `jupyter-notebook password`. Essayez de comprendre ce qu'elles font et relevez le chemin d'accès au fichier de configuration généré.

Puis, allez editer le fichier de configuration généré (vous avez vu la commande en partie 3). Vous pouvez déjà vérifier que le champ `NotebookApp.password` a pour valeur le hash du mot du passe que vous avez généré précedemment.  
En suivant la même logique, rajouter les champs suivants dans le fichier **json**:

  - Un champ `NotebookApp.ip` avec la valeur `"*"`. De base, un notebook n'est accessible qu'en local, cette instruction nous permet donc d'y accéder depuis n'importe quelle adresse.
  - Un champ `NotebookApp.port` avec la valeur `8888` nous permettant d'accéder à l'application via ce port specifique.
  - Un champ `NotebookApp.allow_remote_access` avec la valeur `true`, en complément de l'autorisation sur toutes les ips.
  - Un champ `NotebookApp.open_browser` avec la valeur `false` pour ne pas ouvrir de navigateur au lancement de jupyter sur la machine distante.

Enregistrez votre fichier de configuration, et validez que le lancement de jupyter (commande `jupyter-notebook`) se fait sans aucune erreur.

## Partie 5 : Autoriser la connexion entrante à jupyter par l'interface AWS

A ce stade, jupyter autorise les connexions depuis l'exterieur, mais AWS les bloque. Il va donc falloir ouvrir les ports depuis l'interface AWS EC2.

Sur la console AWS, dans le service EC2, selectionnez votre instance puis cliquez sur le **security-group** associé (il devrait commencer par **launch-wizard...** si vous avez laissé le nom par défaut).

Dans l'onglet **Inbound**, vous pouvez voir que que seul le port SSH (le port 22) est autorisé a effectué des requêtes entrantes (c'est ce qui vous sert à vous connecter) et que les connexions de toutes les ips sont autorisées (C'est l'adresse ip `0.0...` qui indique ceci).

Editez cette configuration pour rajouter une autorisation entrante sur le port `8888` (le port vers lequel nous avons redirigé notre jupyter).

Vous pouvez maintenant accéder à l'interface web de votre jupyter-notebook via votre navigateur en accédant à http://ip-de-votre-machine:8888.

## Partie 6 : Sauvegarder une AMI

Depuis la console AWS :

- Aller dans **EC2**.
- Arrêter l’ancienne instance : Clic-droit puis **Instance State** et enfin **Stop**.
- Clic-droit puis **Images** puis **Create Image**, lui donner un nom et cliquer sur **Create Image**.
- Aller dans le menu **AMI** dans le volet de gauche, votre image est en cours de création.
- Une fois créée, choisir l’image puis **Launch** pour la relancer.
- Retourner dans **EC2**.

Vous pouvez maintenant **SSH** sur la nouvelle instance et observer que l'environnement est toujours le même.

## Partie 7 : Entrainement à python

Télécharger le fichier https://raw.githubusercontent.com/rqueraud/cours-aws-1/master/python-training.ipynb grâce à la commande wget. Puis redémarrer le service jupyter-notebook et choisir le fichier python précédemment chargé.

Résoudre les exercices présents sur le notebook.  
Nous utiliserons majoritairement le langage python pour les prochains cours, donc n'hésitez pas à **solliciter de l'aide**, même pour des questions basiques !

**Attention**: Si vous terminez l'instance EC2, vous perdez votre travail. Pensez donc à télécharger le fichier avant de partir !

## Partie 8 : Extinction 

Une fois terminé, arrêter l'instance :

- **Instance State** puis **Stop**. L'instance est arrêtée mais le disque EBS est conservé. La facturation sur le disque est toujours effective et il est possible de redémarrer une instance dans le même état que nous l'avons laissée.
- **Instance State** puis **Terminate**. L'instance est définitivement stoppée et le disque EBS est supprimé (**ne le faire que le soir avant de partir**).
