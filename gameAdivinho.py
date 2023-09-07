from random import randint
from time import sleep

computador = randint(0,10)
print('-='*30)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('-='*30)
jogador = 0
palpites = 0
#acertou == False
#while not acertou:
while True:
    jogador = int(input('Em qual número eu pensei: '))
    palpites += 1
    if(jogador == computador):
        #acertou == True
        print(f'Voce acertou. Eu pensei no número {computador}')
        break
    elif(jogador > 10):
        print('Você escolheu um número maior que 10. Tente novamente!')
    elif(jogador != computador):
        print(f'Você Errou! Tente Novamente')
        
    
if(palpites <= 5):
    print('A sorte está do seu lado! Parabéns!')
elif(palpites >= 6):
    print('A sorte não está a favor dos tolos!!! - MISS FORTUNE')

if(palpites == 0):
    print('winner winner dick winner')
else:
    print(f'Você acertou com {palpites} tentativas!')