import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte

def alinhar_pontos_braille(centroids, imagem):
    # Aplicar Canny para detectar bordas (opcional, melhora detecção de linhas)
   # bordas = cv2.Canny(imagem, 50, 150, apertureSize=3)
    import cv2
    import numpy as np

    # Ordenar os pontos por coordenadas (y, x)
    centroids = sorted(centroids, key=lambda p: (p[1], p[0]))  # Ordena por y, depois por x

    # Critérios de proximidade
    vertical_threshold = 7 # Proximidade em x para alinhamento vertical
    horizontal_threshold = 7 # Proximidade em y para alinhamento horizontal

    # Separar pontos por coordenadas similares em x (vertical) ou y (horizontal)
    for i in range(len(centroids) - 1):
        for j in range(i + 1, len(centroids)):
            dx = abs(centroids[i][0] - centroids[j][0])  # Diferença em x
            dy = abs(centroids[i][1] - centroids[j][1])  # Diferença em y

            # Desenhar linhas verticais (x próximo, mas y distante)
            if dx < vertical_threshold and dy > vertical_threshold:
                imagem = cv2.line(imagem, tuple(centroids[i]), tuple(centroids[j]), (128, 128, 128), 2)

            # Desenhar linhas horizontais (y próximo, mas x distante)
            if dy < horizontal_threshold and dx > horizontal_threshold:
                imagem = cv2.line(imagem, tuple(centroids[i]), tuple(centroids[j]), (128, 128, 128), 2)

    cv2.imshow('linhas?', imagem)
    cv2.waitKey(0)
    # Detectar linhas com a Transformada de Hough
    linhas = cv2.HoughLines(imagem, 1, np.pi/180, 200)
    
    angulos = []
    
    # Desenhar as linhas detectadas na imagem
    if linhas is not None:
        for rho, theta in linhas[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * a)
            
            # Adiciona a linha na imagem
            imagem3=cv2.line(imagem, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
            # Calcular o ângulo em graus (conversão de radianos para graus)
            angulo = np.degrees(theta)
            angulos.append(angulo)
            
    cv2.imshow('alinhando?', imagem3)
    cv2.waitKey(0)
    # Calcular o ângulo de rotação para alinhar a imagem
    if angulos:
        # Considerar apenas ângulos que correspondem a linhas horizontais ou verticais
        angulos_filtrados = [angulo for angulo in angulos if 70 < angulo < 100 or -10 < angulo < 10]
        if angulos_filtrados:
            angulo_medio = np.mean(angulos_filtrados)
            
            # Rotacionar a imagem para alinhar
            altura, largura = imagem3.shape[:2]
            matriz_rotacao = cv2.getRotationMatrix2D((largura // 2, altura // 2), angulo_medio, 1.0)
            imagem_alinhada = cv2.warpAffine(imagem3, matriz_rotacao, (largura, altura))
            
            # Mostrar a imagem alinhada
            cv2.imshow('Imagem Alinhada', imagem_alinhada)
            cv2.waitKey(0)
            
        else:
            print("Nenhuma linha horizontal ou vertical detectada.")
            imagem_alinhada = imagem
    else:
        print("Nenhuma linha detectada.")
        imagem_alinhada = imagem

    return imagem_alinhada