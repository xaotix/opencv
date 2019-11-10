import cv2
vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0
success = True

tamanho = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fotos = 100
contador = tamanho / fotos
print(str(tamanho) + ' frames')
while count< tamanho:
  success,image = vidcap.read(count)
  cv2.imwrite("img/frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  print('frame ' + str(count))
  count += contador