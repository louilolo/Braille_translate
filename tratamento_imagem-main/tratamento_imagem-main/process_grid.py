import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte
def processGrid(centroids,VLine,VCol,imagem):
    # Buscar Cela
    flag = 0
    text = ''
    
    for i in range(0,len(VLine)-3,3):  # Linha
        for j in range(0,len(VCol)-2,2):  # Coluna
            vLetras = [0,0,0,0,0,0]
            cnt = 0      
            
            # Retira a sub_imagem        
            sub_img = imagem[VLine[i]:VLine[i+3], VCol[j]:VCol[j+2]]
            # Verifica se a sub_imagem é válida
            if sub_img.size == 0:
                cv2.imshow("sub imagem", sub_img)
                continue
                    
            for n in range(2): # Coluna
                for m in range(3): # Linha
                    for k in range(len(centroids)):
                            if(centroids[k][0] >= VLine[i+m] and centroids[k][0] <= VLine[(i+m)+1] and  centroids[k][1] >= VCol[j+n] and centroids[k][1] <= VCol[(j+n)+1]):                    
                                vLetras[cnt] = 1
                    cnt = cnt + 1
                
            [carac, flag] = bdLetra.bdLetra(vLetras, flag)
            text += carac
    print("rodou pgrid")
    return text