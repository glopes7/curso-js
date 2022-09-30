from re import X
from tkinter import N


numero_atrasos = 0
if numero_atrasos >= 3:
    print('Voce esta suspenso!')
elif numero_atrasos == 1:
    print('Pode entrar na aula, porem caso falte mais 2 vezes, voce sera suspenso!')
elif numero_atrasos == 2:
    print ('Pode entrar, porem se faltar mais uma vez, voce sera suspenso!')
else:
    print('Pode entrar, voce nao tem nenhum atrasso!')