from pydub import AudioSegment
from pydub.silence import split_on_silence

def gerar_matriz(diretorio, nome_famoso):
    min_silence_len = 100
    silence_thresh = -30

    sound_file = AudioSegment.from_wav(diretorio)

    #region ' Codigo Comentado '

    '''
    toMaximo = sound_file.max_possible_amplitude
    racao = sound_file.duration_seconds
    vefile = wave.open("ab.wav", 'r')
    
    from scipy.io.wavfile import read
    
    fs, data = read('ab.wav')
    data_size = len(data)
    
    data = data / (2.**15)
    
    varia = data.shape
    
    varia2 = varia[0] / fs #aqui estou pegando a duraçao do audi. mediçao em ms(milésimo de segundo)
    
    focus_size = int(0.15 * fs)
    '''

    #endregion

    audio_chunks = split_on_silence(sound_file, min_silence_len, silence_thresh)

    matriz = []

    for i, chunk in enumerate(audio_chunks):
        linha = []
        linha_pai = []

        pontoMaximo = chunk.max_possible_amplitude
        mediaFrame = chunk.frame_rate
        amplitude = chunk.max
        mediaItencidade = chunk.rms

        linha_pai.append(nome_famoso)
        linha.append(pontoMaximo)
        linha.append(mediaFrame)
        linha.append(amplitude)
        linha.append(mediaItencidade)
        linha_pai.append(linha)
        matriz.append(linha_pai)
    return matriz