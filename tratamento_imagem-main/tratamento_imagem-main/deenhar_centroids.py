import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte
def desenhar_centroides(centroids, shape):
    # Criar uma imagem em branco
    nova_imagem = np.ones(shape, dtype=np.uint8) * 255  # Fundo branco
    
    # Definir o raio do círculo
    raio = 3
    #chamar aqui a rotacionar!
    #salvar imagem!
    # Desenhar um círculo preto em cada centróide
    for centroide in centroids:
        cv2.circle(nova_imagem, tuple(centroide[::-1]), raio, (0, 0, 0), -1,)  # Inverte a ordem (y, x) para (x, y) 
        # verificar
    cv2.imshow("Nova Imagem (antes da função)", nova_imagem)
    cv2.waitKey(0)
      # Aguarda uma tecla ser pressionada
    cv2.destroyAllWindows() 
    print(type(nova_imagem))
    print("rodou desenharc")
    return nova_imagem
