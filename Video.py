import cv2
from ffpyplayer.player import MediaPlayer

def video_famoso(nome):
    arquivo = "video_famosos/"+nome+".mp4"
    cap = cv2.VideoCapture(arquivo)
    player = MediaPlayer(arquivo)
    ret, frame = cap.read()
    frameAudio, val = player.get_frame()
    while(1):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
            cap.release()
            cv2.destroyAllWindows()
            break
        cv2.imshow('frame',frame)
