from pydub import AudioSegment
from pydub.silence import split_on_silence
from pprint import pprint
import audioop

def gerar_matriz(diretorio, nome_famoso, min_silence_len = 100):
    silence_thresh = -30

    sound_file = AudioSegment.from_wav(diretorio)

    audio_chunks = split_on_silence(sound_file, min_silence_len, silence_thresh)

    matriz = []

    for chunk in enumerate(audio_chunks):
        c = chunk[1]
        linha = []
        linha_pai = []

        amplitude = c.max
        mediaItencidade = c.rms
        dBFS = c.dBFS
        max_dBFS = c.max_dBFS
        avg = audioop.avg(c.raw_data, c.sample_width)

        linha_pai.append(nome_famoso)
        linha.append(amplitude)
        linha.append(mediaItencidade)
        linha.append(avg)
        linha.append(dBFS)
        linha.append(max_dBFS)
        linha_pai.append(linha)
        matriz.append(linha_pai)
    #print(matriz)
    return matriz