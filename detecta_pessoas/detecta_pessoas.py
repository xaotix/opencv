from imutils.object_detection import non_max_suppression
import imutils
import cv2
import numpy as np


hog = cv2.HOGDescriptor()
#usa o SVM padrão para reconhecer pessoas
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#carrega o video
cam = cv2.VideoCapture('pessoas_caminhando.mp4')

#pula a introdução do video
cam.set(cv2.CAP_PROP_POS_FRAMES, 200)



while True:
    #inicializa o vídeo
    retval, image = cam.read()
    #muda a resolucao
    image = imutils.resize(image, width=min(720, image.shape[1]))
    orig = image.copy()
    
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
    padding=(8, 8), scale=1.05)
    #cria um retângulo em volta do que foi encontrado
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    
    #dá uma limpada nos itens econtrados
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    for (xA, yA, xB, yB) in pick:
        #desenha um retângulo quando encontra
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
    print("[INFO]: {} Encontrados, {} encontrados depois da supressão".format(len(rects), len(pick)))
    cv2.imshow("Pessoas", image)
    k = cv2.waitKey(1) 
    if k == 27:
        break
cv2.destroyAllWindows()