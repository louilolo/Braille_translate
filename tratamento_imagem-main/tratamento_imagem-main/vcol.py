import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte
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
                    
                if(r1 >= 12 or r2 >= 12 or r3 >= 14 or r4 >=14 ):#parametrizar
                    remCol.append(1)
                else:
                    remCol.append(0)
    
    if(np.max(remCol) == 1):
        VCol.remove(VCol[0])
    print("rodou vcol")
    return VCol