import Matriz
import  Microfone
import os

audios = os.listdir("audio_famosos")
#arquivos.gt
matriz = []

for i in audios:
    nome_famoso = i.split('_')[0]

    matriz.append(Matriz.gerar_matriz("audio_famosos/" + i, nome_famoso))

audioUsuario = Microfone.audio_usuario()

matrizUsuario = Matriz.gerar_matriz(audioUsuario, "Usuario")

print("Acabou")