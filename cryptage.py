#MD5Test3 + MD5Test4

import os  # pour comparer les fichiers
import uuid
import hashlib


def hash_password(password):

    salt = uuid.uuid4().hex     # uuid is used to generate a random number
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def comparefichiers(fichier1, fichier2, lgbuf=16*1024):

    """Compare les 2 fichiers et renvoie True s'ils sont identiques
       lgbuf est la taille du buffer de lecture
    """
    if os.path.getsize(fichier1) != os.path.getsize(fichier2):
        return False            # les fichiers n'ont pas la même longueur

    with open(fichier1, "rb") as f1, open(fichier2, "rb") as f2:
        while True:
            buf1 = f1.read(lgbuf)
            if len(buf1) == 0:
                return True         # fin de lecture: pas de différence
            buf2 = f2.read(lgbuf)
            if buf1 != buf2:
                return False        # on a trouvé une différence


def check_password(user_password, test_password):

    password, salt = user_password.split(':')   # sépare le cryptage en mdp et sel
    test = hashlib.sha256(salt.encode() + test_password.encode()).hexdigest()

    with open('Password.txt', 'w') as file:
        file.write(password)

    with open('Test.txt', 'w') as file:
        file.write(test)

    if comparefichiers('Password.txt', 'Test.txt'):
        return True
    else:
        return False