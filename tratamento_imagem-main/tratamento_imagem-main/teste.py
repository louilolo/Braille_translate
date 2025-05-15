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
    raio = 4
    
    # Desenhar um círculo preto em cada centróide
    for centroide in centroids:
        cv2.circle(nova_imagem, tuple(centroide[::-1]), raio, (0, 0, 0), -1)  # Inverte a ordem (y, x) para (x, y)
    
    return nova_imagem



def verificao(VLine, VCol, centroids):
    for _ in range(1):  #Coluna
        remCol = [0]   
        for i in range(0,len(VLine)-3,3):  #linha                         
            vLetras = [0,0,0,0,0,0]
            vCent = [0,0,0,0,0,0]
            cnt = 0
                
            for n in range(2): #Coluna
                for m in range(3): #linha
                    for k in range(len(centroids)):
                        if(centroids[k][0] >= VLine[i+m] and centroids[k][0] <= VLine[(i+m)+1] and  centroids[k][1] >= VCol[n] 
                           and centroids[k][1] <= VCol[n+1]):                    
                            vLetras[cnt] = 1
                            vCent[cnt] = k
                    cnt = cnt+1                

            dist = DistanceMetric.get_metric('euclidean')
            if(vLetras[0] == vLetras[2] and vLetras[0] != vLetras[1]):
                r1=0 
                r2=0 
                r3=0 
                r4=0 
                if(vLetras[0] == vLetras[3]):    
                    X = [ centroids[vCent[0]], centroids[vCent[3]] ]
                    r1 = dist.pairwise(X)[0][1]
                    
                if(vLetras[2] == vLetras[5]):    
                    X = [ centroids[vCent[2]], centroids[vCent[5]] ]
                    r2 = dist.pairwise(X)[0][1]
                    
                if(vLetras[0] == vLetras[4]):    
                    X = [ centroids[vCent[0]], centroids[vCent[4]] ]
                    r3 = dist.pairwise(X)[0][1]

                if(vLetras[2] == vLetras[4]):    
                    X = [ centroids[vCent[2]], centroids[vCent[4]] ]
                    r4 = dist.pairwise(X)[0][1]
                    
                if(r1 >= 12 or r2 >= 12 or r3 >= 14 or r4 >=14 ):
                    remCol.append(1)
                else:
                    remCol.append(0)
    
    if(np.max(remCol) == 1):
        VCol.remove(VCol[0])

    return VCol

def processGrid(centroids, VLine, VCol, imagem):
    # Buscar Cela
    flag = 0
    text = ''
    
    for i in range(0, len(VLine) - 3, 3):  # Linha
        for j in range(0, len(VCol) - 2, 2):  # Coluna
            vLetras = [0, 0, 0, 0, 0, 0]
            cnt = 0      
            
            # Retira a sub_imagem        
            sub_img = imagem[VLine[i]:VLine[i + 3], VCol[j]:VCol[j + 2]]
            
            # Verifica se a sub_imagem é válida
            if sub_img.size == 0:
                continue
                    
            for n in range(2): # Coluna
                for m in range(3): # Linha
                    for k in range(len(centroids)):
                            if(centroids[k][0] >= VLine[i + m] and centroids[k][0] <= VLine[(i + m) + 1] 
                               and centroids[k][1] >= VCol[j + n] and centroids[k][1] <= VCol[(j + n) + 1]):                    
                                vLetras[cnt] = 1
                    cnt = cnt + 1
            
            # print(vLetras)
            [carac, flag] = bdLetra(vLetras, flag)
            text += carac
            # if sub_img.size > 0: 
            #     #Plotar a sub-imagem
            #     plt.figure()
            #     plt.imshow(sub_img, cmap='gray')
            #     plt.title('Sub-Imagem')
            #     plt.axis('off')
            #     plt.show()
    
    return text


def trueRotate():
     
    
    image = cv2.imread('imagesTratadas/im 8.jpg', cv2.IMREAD_GRAYSCALE) #TESTES DAS IMAGEMS COM IMG 8
    
    limiarizadaOTUS = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    mediana1 = cv2.medianBlur(limiarizadaOTUS, 3)
    
    # Aplicar erosão e dilatação para remover pequenos ruídos e preencher lacunas
    kernel = np.ones((3, 3), np.uint8)
    erosao = cv2.erode(mediana1, kernel, iterations=1)
    dilatacao = cv2.dilate(erosao, kernel, iterations=1)
    mediana = cv2.medianBlur(dilatacao, 3)
    
    # Encontrar contornos na imagem limiarizada
    contornos, _ = cv2.findContours(mediana, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
    
    centroids = []
    cx = []
    cy =[]
    for contorno in contornos:
        M = cv2.moments(contorno)
        if M['m00'] != 0: #garantindo que não havera divisão por 0
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            cx.append(x)
            cy.append(y)
            centroids.append([y,x]) # linha, coluna
        
    #criar nova imagem com os centroides achados
    nova_imagem_centroides = desenhar_centroides(centroids, mediana.shape)
    
    #remove a primeira linha pois ele retorna o centroid da imagem.
    cx.remove(cx[0])
    cy.remove(cy[0])
    centroids.remove(centroids[0])
    
    #ordenar as listas com os valores de X e Y (crescente)
    cx.sort(reverse=False)
    cy.sort(reverse=False)
    
    limiar_gride = 20
    cor = 200
    
    # inserir grade coluna
    VCol = []
    cv2.line(nova_imagem_centroides,(cx[0]-limiar_gride, 0), (cx[0]-limiar_gride,nova_imagem_centroides.shape[0]),cor)
    VCol.append(cx[0]-limiar_gride)
    p_aux = 0
    for i in range(len(cx)):
        if(cx[i] >= (p_aux+limiar_gride)): 
            cv2.line(nova_imagem_centroides,(cx[i]+limiar_gride, 0), (cx[i]+limiar_gride,nova_imagem_centroides.shape[0]),cor)
            p_aux = cx[i]
            VCol.append(cx[i]+limiar_gride)


    # inserir grade linha
    VLine = []
    cv2.line(nova_imagem_centroides,(0, cy[0]-limiar_gride), (nova_imagem_centroides.shape[1],cy[0]-limiar_gride),cor)
    VLine.append(cy[0]-limiar_gride)
    p_aux = 0
    for i in range(len(cy)):
        if(cy[i] >= (p_aux+limiar_gride)): 
            cv2.line(nova_imagem_centroides,(0, cy[i]+limiar_gride), (nova_imagem_centroides.shape[1],cy[i]+limiar_gride),cor)
            p_aux = cy[i]
            VLine.append(cy[i]+limiar_gride)
    
           
    # Desenhar os contornos na imagem original
    imagem_contornos = image.copy()
    cv2.drawContours(imagem_contornos, contornos, -1, (0, 255, 0), 2)
    VCol = verificao(VLine, VCol, centroids)
    texto = processGrid(VCol=VCol, VLine=VLine, centroids=centroids, imagem=nova_imagem_centroides)
    print(texto)


    plt.figure(figsize=(8, 6))
    plt.imshow(limiarizadaOTUS, cmap='gray')
    plt.title('Imagem Limiarizada')
    plt.axis('off')
    
    plt.figure(figsize=(8, 6))
    plt.imshow(nova_imagem_centroides, cmap='gray')
    plt.title('Noa Imagem')
    plt.axis('off')
  
    
    plt.show()


trueRotate()
