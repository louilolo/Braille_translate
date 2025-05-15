
import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte
def transformarImagem(imagem):
        print(f"Tentando processar a imagem: {imagem}")
        if not os.path.exists(imagem):
            print(f"Arquivo não encontrado: {imagem}")
            return None  # Retorne None explicitamente se o arquivo não existir

        #imagem = cv2.imread(img)
        if imagem is None:
            print("Erro ao carregar a imagem com cv2.imread")
            return None
        image = io.imread(imagem)
        cv2.imshow('transformadas', image)
        cv2.waitKey(0)
    # Converter para escala de cinza
        #escala_de_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #print(f"Imagem convertida para escala de cinza: shape {escala_de_cinza.shape}")

    # Limiarização
        imagem_limiarizada = cv2.adaptiveThreshold(
        image, 210, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 8
    )
        print("Imagem limiarizada criada")

    # Filtro de ruído
        mediana = cv2.medianBlur(imagem_limiarizada, 3)
        print("Filtro de mediana aplicado")

    # Operações morfológicas
        kernel = np.ones((3, 3), np.uint8)
        escala_de_cinza_processada = cv2.erode(mediana, kernel, iterations=1)
        escala_de_cinza_processada2 = cv2.dilate(escala_de_cinza_processada, kernel, iterations=1)
        escala_de_cinza_processada3 = cv2.medianBlur(escala_de_cinza_processada2, 3)
        sucesso = cv2.imwrite('tratamento_imagem-main\\tratamento_imagem-main\\imagesTratadasescala_de_cinza_processada3.jpg', escala_de_cinza_processada3)
        if sucesso:
            print("Imagem salva ")
        else:
            print("Erro ao salvar a imagem.")
        cv2.imshow('transformada', mediana)
        cv2.waitKey(0)
        print("Processamento morfológico completo")
        
        return escala_de_cinza_processada3 , imagem_limiarizada