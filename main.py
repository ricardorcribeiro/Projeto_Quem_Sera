import Matriz
import Microfone
import os
#from sklearn import svm
audios = os.listdir("audio_famosos")
matriz = []

for i in audios:
    nome_famoso = i.split('_')[0]
    matriz.append(Matriz.gerar_matriz("audio_famosos/" + i, nome_famoso))

audioUsuario = Microfone.audio_usuario()

matrizUsuario = Matriz.gerar_matriz(audioUsuario, "Usuario")


print(matriz)
print("Acabou")

#

#clf.predict([[1,0]])