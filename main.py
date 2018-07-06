import Matriz
import Microfone
import os
import numpy as np
from sklearn import svm
from collections import Counter
#from Video import video_famoso

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
    matrizUsuario = Matriz.gerar_matriz(audioUsuario, "Usuario", 50)

    #print(listaPessoas)
    #print(matrizTreino)

    clf = svm.SVC()
    clf.fit(matrizTreino, listaPessoas)

    result = []
    for chunks in matrizUsuario:
        result.append(chunks[1])

    result = clf.predict(result)
    result = Counter(result)
    result = result.most_common(1)
    print("E o resultado foi...")
    print(result, "!!!")
    #video_famoso(result)
    user_answer = str.lower(input("Deseja imitar de novo? (digite 'y' para sim)"))
    #print(user_answer)

print("OK! Foi divertido jogar com você! Até a próxima!")
input("Fim do programa, aperte qualquer tecla para finalizar.")