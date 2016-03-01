from cryptage import *

password = hash_password('mdp')
with open('mdp.txt', 'w') as file:
    file.write(password)
