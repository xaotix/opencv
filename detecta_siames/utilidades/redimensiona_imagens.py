import numpy as np
import cv2
import os
import os, sys
import tqdm
import glob
import imutils
#redimensiona as imagens para o tamanho especificado
largura = 400 
def redimensiona(img_path):
    try:  

        print(img_path)
        img = cv2.imread(img_path)
    
        img = imutils.resize(img, width=min(largura, img.shape[1]))
        return img
    except Exception as e: 

        print(e)
    return cv2.imread(img_path)

arquivos = glob.glob("./img/*.jpg")
saida = './img/saida/'

if not os.path.exists(saida): 
   os.makedirs(saida) 

c = 0
for file in arquivos:
    img = redimensiona(file)
    c = c +1
    img = cv2.imwrite(str(saida + 'Mima_' + str(c) + ".jpg") , img)   





