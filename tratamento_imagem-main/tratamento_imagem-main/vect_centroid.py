import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from skimage import img_as_ubyte
def centroid_vect(escala_de_cinza_processada3):
        # Encontrar contornos na imagem limiarizada
    contornos, _ = cv2.findContours(escala_de_cinza_processada3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("rodou contornos")

    centroids = []
    cx = []
    cy =[]
    for contorno in contornos:
        M = cv2.moments(contorno)
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        cx.append(x)
        cy.append(y)
        print("ta infinita")
        centroids.append([y,x]) #linha, coluna
    print(cx)
    print(cy)
    print(centroids)
    print("rodou vect_centroid")
    return centroids , cx, cy, contornos


'''
# Dados dos centroids
    cxn = np.array(cx)
    cyn = np.array(cy)

    # 1. Regressão linear para encontrar inclinação
    model_x = LinearRegression().fit(cxn.reshape(-1, 1), cyn)
    model_y = LinearRegression().fit(cyn.reshape(-1, 1), cxn)

    angle_x = np.arctan(model_x.coef_[0])  # Ângulo de inclinação no eixo X
    angle_y = np.arctan(model_y.coef_[0])  # Ângulo de inclinação no eixo Y

    # 2. Calculando a média do ângulo
    theta = (angle_x + angle_y) / 2  # Aproximação média

    # 3. Matriz de rotação
    R = np.array([
        [np.cos(-theta), -np.sin(-theta)],
        [np.sin(-theta),  np.cos(-theta)]
    ])

    # 4. Aplicando rotação
    centroids = np.column_stack((cxn, cyn))
    aligned_centroids = centroids @ R.T

    # Separando coordenadas alinhadas
    cx_aligned, cy_aligned = aligned_centroids[:, 0], aligned_centroids[:, 1]

    # 5. Visualizando os resultados
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(cxn, cyn, color='blue', label='Original')
    plt.title('Pontos Originais')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.scatter(cx_aligned, cy_aligned, color='green', label='Alinhados')
    plt.title('Pontos Alinhados')
    plt.axis('equal')

    plt.show()
'''