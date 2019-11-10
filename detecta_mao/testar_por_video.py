# Autor: Daniel Lins Maciel
import numpy as np
import cv2
import imutils
#carrega o video
camera = cv2.VideoCapture('video.mp4')
#carrega o cascade xml
xml = cv2.CascadeClassifier("mapeamento.xml")
while True:
    img = camera.read()[1]
    #redimensiona a resolução do video
    img = imutils.resize(img, width=min(500, img.shape[1]))
    img = cv2.flip( img, -1 )
    height, width, c = img.shape
    #mapeia a mao, usando o cascade carregado
    objetos = xml.detectMultiScale(img, 1.2, 5)

    
    for (x, y, w, h) in objetos:
        #desenha um retângulo em volta da mao
        cv2.rectangle(img, (x, y+10), (x+w, y+h), (0, 0, 255), 2)
        #escreve um texto em cima do retângulo
        cv2.putText(img, 'mao',(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)

    #inicializa a tela
    cv2.imshow('Mão', img)
    #trava o frame em ms, aguardando a key e ao mesmo tempo delimitando a
    #quantidade de frames por segundo
    tecla = cv2.waitKey(25)

    #aguarda pela tecla esc
    if tecla == 27:
        break

cv2.destroyAllWindows()