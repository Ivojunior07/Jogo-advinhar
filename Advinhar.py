from random import randint
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um numéro entre 0 e . Tente advinhar...')
print('-=-' * 20)
Jogador = int(input('Em que número pensei? '))
if Jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI ! Eu pensei no numero {} e não no número {}'. format(computador, Jogador))