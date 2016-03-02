Ce projet a été testé sur mac, il est possible que ce ne soit pas la même chose sur d’autres OS.

- Décompressez le fichier du dépôt Github sur votre ordinateur.
- Lancez votre terminal (Applications/utilitaires ou Commande + Maj + U)

#Mode client/serveur
- Aller dans le dossier «server» du dossier décompressé en path:
     => cd <path>
- Dans ce dossier, vous pouvez voir 3 fichiers: 

	- cryptage.py -> permet de vérifier le mot de passe inscrit par le client en le comparant avec celui du fichier «mdp.txt».
	- mdp.txt ————-> renferme un mot de passe crypté.
	- server.py ——-> permet de mettre en route le serveur

- Lancer le fichier server.py:
	=> python3 server.py serveur

Connection Client-serveur:
- Revenez à la racine du du dossier décompressé et allez dans le dossier«Client»:
	=>| cd…
- Dans ce dossier, il y a un fichier python appelé «client.py» qui permet aux clients de s’identifier lors de la connection au serveur et de lui envoyez une requête afin qu’il affiche la liste des personnes qui se sont connectées.
	=> python3 client.py client
!!!! Le client doit retenir les ip ainsi que les n° de port des utilisateurs avec lequel il veut discuter dans un chat privé !!!!!! 

#Mode peer-to-peer.
- Revenez à la racine du dossier décompressé et allez dans le dossier «Chat»:
	=> |cd… 
- Enfin, à l’intérieur, le fichier chat.py permet de lancer un chat privé entre plusieurs utilisateurs ! 
- Chaque utilisateur doit lancer le fichier chat.py:
	=> python3 chat.py localhost <port> (à faire une seule fois)
  - Pour discuter avec une personne:
	=> /join localhost < le port de l’autre>
	=> /send + message
  - Pour quitter le chat:
	=> /quit
  - Pour quitter fermer la session: 
	=> /exit

	
