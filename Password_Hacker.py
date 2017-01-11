import time
from string import printable
from itertools import product

def guess_password(password,word):
    if word == password:
        return word
    else:
        return 0
    
guess = 0
result = ''
character_set = printable
loop = 1

print('Please enter a password!')
password = raw_input()
start = time.time()

while guess == 0:

    for comb in product(character_set,repeat=loop):
         word = ''.join(comb)
         result = guess_password(password,word)
         #print(word)
         
         if result:
            end = time.time()
            guess = 1
            print('Your password is ' + password + '! I hacked it in ' + str(end - start) + ' seconds!')
            break
        
    if not guess:
         loop = loop + 1


                                                                                                                                                                                        
