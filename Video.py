import cv2
from ffpyplayer.player import MediaPlayer

cap = cv2.VideoCapture("v2.mp4")
player = MediaPlayer("v2.mp4")
val = ''
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
