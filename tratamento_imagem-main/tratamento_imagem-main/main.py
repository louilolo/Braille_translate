import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte
from alinhar import alinhar_pontos_braille
from deenhar_centroids import desenhar_centroides
from grade import grid_appl
from process_grid import processGrid
from transformar import transformarImagem
from vcol import verificao
from vect_centroid import centroid_vect

from skimage import img_as_ubyte
def main():

    # Carregar imagem
    image = io.imread('C:\\Users\\louis\\OneDrive\\Documentos\\GitHub\\Braille_translat_learner\\tratamento_imagem-main\\tratamento_imagem-main\\imagesTratadas\\im 1.jpg', as_gray=True)
    cv2.imshow('img',image)
    cv2.waitKey(0)
    print(image.shape)
# Cimonverte para uint8

    # Supondo que filtered_image seja a imagem que você quer salvar

    # Aplicar filtro de contraste e remoção de ruído
    filtered_image = filters.gaussian(image, sigma=1)
    filtered_image_uint8 = img_as_ubyte(filtered_image)
    cv2.imshow('filtrada',filtered_image_uint8)
    cv2.waitKey(0)
    io.imsave('filtered_image.png', filtered_image_uint8)
    escala_de_cinza_processada3, imagem_limiarizada = transformarImagem('D:/Users/Louise/Braille_translat_learner/filtered_image.png')
    #cv2.imshow('escalas',img)
    #cv2.waitKey(0)# Converte para uint8

    print("saiu da função")

    #escala_de_cinza_processada3 = cv2.imread('tratamento_imagem-main\\tratamento_imagem-main\\imagesTratadasescala_de_cinza_processada3.jpg')
    #cv2.imshow("escala",escala_de_cinza_processada3)
    #cv2.waitKey(0)# Converte para uint8

    if escala_de_cinza_processada3 is not None:
        print(f"Imagem carregada com sucesso: shape {escala_de_cinza_processada3.shape}")
    else:
        print("Erro ao carregar a imagem.")
    
    if escala_de_cinza_processada3.dtype != np.uint8:
        print(type(escala_de_cinza_processada3))
        
    escala_de_cinza_processada3 = img_as_ubyte(escala_de_cinza_processada3)
    centroids, cx , cy, contornos = centroid_vect(escala_de_cinza_processada3)
    nova_imagem_centroides = desenhar_centroides(centroids, escala_de_cinza_processada3.shape)
    
    print(type(nova_imagem_centroides))
    cv2.imshow("passou?", nova_imagem_centroides)
    cv2.waitKey(0) 
    
    correcao_geometrica = alinhar_pontos_braille(centroids, nova_imagem_centroides)
    type(correcao_geometrica)
    cv2.imshow("corrigir", correcao_geometrica)
    cv2.waitKey(0)
    #remove a primeira linha pois ele retorna o centroid da imagem.
    cx.remove(cx[0])
    cy.remove(cy[0])
    centroids.remove(centroids[0])

    #ordenar as listas com os valores de X e Y (crescente)
    cx.sort(reverse=False)
    cy.sort(reverse=False)
    VLine, VCol, imagem_com_grade = grid_appl( cy, cx, nova_imagem_centroides)    
    # Desenhar os contornos na imagem original
    imagem_contornos = image.copy()
    cv2.drawContours(imagem_contornos, contornos, -1, (0, 255, 0), 2)
    
    VCol = verificao(VLine, VCol, centroids)
    texto = processGrid(VCol=VCol, VLine=VLine, centroids=centroids, imagem=imagem_com_grade)
    print(texto)
    # Aplicar filtro de contraste e remoção de ruído
    
    # Exibir a imagem original, a imagem processada e a imagem com contornos
    cv2.imshow("Imagem Original", image)
    cv2.imshow("Filtros", filtered_image)
    cv2.imshow("Correcão Geometrica", correcao_geometrica)
    cv2.imshow("Contornos", imagem_contornos)
    cv2.imshow("Rotated", imagem_limiarizada)
    cv2.imshow("Grade", imagem_com_grade)
    

    # cv2.imshow("Imagem Processada", imagem_limiarizada)
    # cv2.imshow("Imagem com Centroides", nova_imagem_centroides)
    # cv2.imshow("Imagem com Contornos", imagem_contornos)
    cv2.waitKey(0)


#main("C:\\Users\\louis\\OneDrive\\Documentos\\GitHub\\Braille_translat_learner\\tratamento_imagem-main\\tratamento_imagem-main\\imagesTratadas\\im 1.jpg")
# main#imagens braille/WhatsApp Image 2022-11-03 at 14.43.13 (6).jpeg
main()