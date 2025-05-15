import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte

# Função para calcular a inclinação média dos pontos
def calcular_inclinacao_media(centroids):
    # Calcular a média das diferenças entre as coordenadas y dos pontos
    deltas_y = np.diff([p[0] for p in centroids])
    inclinacao_media_rad = np.arctan(np.mean(deltas_y))
    inclinacao_media_graus = np.degrees(inclinacao_media_rad)
    return inclinacao_media_graus

# Função para desenhar os centroides alinhados
def desenhar_centroides_alinhados(centroids, shape):
    # Calcular a inclinação média dos centroides
    inclinacao_media = calcular_inclinacao_media(centroids)
    
    # Criar uma imagem em branco
    nova_imagem = np.ones(shape, dtype=np.uint8) * 255  # Fundo branco
    
    # Definir o raio do círculo
    raio = 4
    
    # Desenhar um círculo preto em cada centróide alinhado
    for centroide in centroids:
        # Calcular as coordenadas do centróide alinhado
        x, y = centroide
        x_alinhado = int(x * np.cos(np.radians(-inclinacao_media)) - y * np.sin(np.radians(-inclinacao_media)))
        y_alinhado = int(x * np.sin(np.radians(-inclinacao_media)) + y * np.cos(np.radians(-inclinacao_media)))
        
        # Desenhar o círculo preto na posição alinhada
        cv2.circle(nova_imagem, (y_alinhado, x_alinhado), raio, (0, 0, 0), -1)
    
    return nova_imagem

# Exemplo de uso
centroids = [[10, 20], [30, 40], [50, 60]]  # Lista de centroides de exemplo
shape = (100, 100)  # Formato da imagem de exemplo

# Desenhar os centroides alinhados
imagem_com_centroides_alinhados = desenhar_centroides_alinhados(centroids, shape)

# Exibir a imagem resultante
cv2.imshow("Imagem com Centroides Alinhados", imagem_com_centroides_alinhados)
cv2.waitKey(0)
cv2.destroyAllWindows()
