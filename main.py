import Matriz
import Microfone
import os
from sklearn import svm

audios = os.listdir("audio_famosos")
matriz =[]
matrizTreino = []
listaPessoas = []

for i in audios:
    nome_famoso = i.split('_')[0]
    Itens = Matriz.gerar_matriz("audio_famosos/" + i, nome_famoso)
    for iten in Itens:
        listaPessoas.append(iten[0])
        matrizTreino.append(iten[1])
    #matriz.append(Matriz.gerar_matriz("audio_famosos/" + i, nome_famoso))

audioUsuario = Microfone.audio_usuario()

matrizUsuario = Matriz.gerar_matriz(audioUsuario, "Usuario")



#print(listaPessoas)
#print(matrizTreino)

clf = svm.SVC()
clf.fit(matrizTreino, listaPessoas)

result = clf.predict(matrizUsuario[0][1])
print("Acabou")

#

