import Matriz
import Microfone
import os
import numpy as np
from sklearn import svm

audios = os.listdir("audio_famosos")
matriz =[]
matrizTreino = []
listaPessoas = []

print("Carregando áudios de famosos, aguarde...")
for i in audios:
    nome_famoso = i.split('_')[0]
    Itens = Matriz.gerar_matriz("audio_famosos/" + i, nome_famoso)
    for iten in Itens:
        listaPessoas.append(iten[0])
        matrizTreino.append(iten[1])
matrizTreino = np.asarray(matrizTreino)
matrizTreino.reshape(1,-1)
print("Pronto!")
input("BEM VINDO(A)!\nPara começar aperte qualquer tecla e seu áudio será gravado.")
user_answer = 'y'

while user_answer == 'y':
    print("GRAVANDOOOO! Imite alguma celebridade, rápido!")
    audioUsuario = Microfone.audio_usuario()
    print("OK, vou adivinhar quem você imitou agora...")
    matrizUsuario = Matriz.gerar_matriz(audioUsuario, "Usuario")

    #print(listaPessoas)
    #print(matrizTreino)

    clf = svm.SVC()
    clf.fit(matrizTreino, listaPessoas)

    result = clf.predict([matrizUsuario[0][1]])
    print("E o resultado foi...")
    print(result, "!!!")
    user_answer = input("Deseja imitar de novo? (digite 'y' para sim)").lower
    print(user_answer)

print("OK! Foi divertido jogar com você! Até a próxima!")
input("Fim do programa, aprte qualquer tecla para finalizar.")