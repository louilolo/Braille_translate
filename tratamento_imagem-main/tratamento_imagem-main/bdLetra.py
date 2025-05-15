def bdLetra(snap,flag):
    a = [1, 0, 0, 0, 0, 0]
    b = [1, 1, 0, 0, 0, 0]
    c = [1, 0, 0, 1, 0, 0]
    d = [1, 0, 0, 1, 1, 0]
    e = [1, 0, 0, 0, 1, 0]
    f = [1, 1, 0, 1, 0, 0]
    g = [1, 1, 0, 1, 1, 0]
    h = [1, 1, 0, 0, 1, 0]
    i = [0, 1, 0, 1, 0, 0]
    j = [0, 1, 0, 1, 1, 0]
    k = [1, 0, 1, 0, 0, 0]
    l = [1, 1, 1, 0, 0, 0]
    m = [1, 0, 1, 1, 0, 0]
    n = [1, 0, 1, 1, 1, 0]
    o = [1, 0, 1, 0, 1, 0]
    p = [1, 1, 1, 1, 0, 0]
    q = [1, 1, 1, 1, 1, 0]
    r = [1, 1, 1, 0, 1, 0]
    s = [0, 1, 1, 1, 0, 0]
    t = [0, 1, 1, 1, 1, 0]
    u = [1, 0, 1, 0, 0, 1]
    v = [1, 1, 1, 0, 0, 1]
    w = [0, 1, 0, 1, 1, 1]
    x = [1, 0, 1, 1, 0, 1]
    y = [1, 0, 1, 1, 1, 1]
    z = [1, 0, 1, 0, 1, 1]
    cedilha =[1, 1, 1, 1, 0, 1]
    espaco = [0, 0, 0, 0, 0, 0]
    ag = [1, 1, 1, 0, 1, 1]
    eg = [1, 1, 1, 1, 1, 1]
    ig = [0, 0, 1, 1, 0, 0]
    og = [0, 0, 1, 1, 0, 1]
    ug = [0, 1, 1, 1, 1, 1]
    acr = [1, 1, 0, 1, 0, 1]
    ecr = [0, 1, 1, 1, 0, 1]
    icr = [1, 0, 0, 1, 0, 1]
    ocr = [0, 1, 0, 1, 1, 1]
    ucr = [1, 0, 0, 0, 1, 1]
    ac = [1, 0, 0, 0, 0, 1]
    ec = [1, 1, 0, 0, 0, 1]
    oc = [1, 0, 0, 1, 1, 1]
    at = [0, 0, 1, 1, 1, 0]
    ot = [0, 1, 0, 1, 0, 1]
    
    virg  = [0, 1, 0, 0, 0, 0]
    doisp = [0, 1, 0, 0, 1, 0]
    ponto = [0, 1, 0, 0, 1, 1]
    excla = [0, 1, 1, 0, 1, 0]
    inte = [0, 1, 0, 0, 0, 1]
    pontvirg = [0, 1, 1, 0, 0, 0]
    maiuscula = [0, 0, 0, 1, 0, 1]
    
    abP = [1, 1, 0, 0, 0, 1]
    feP = [0, 0, 1, 1, 1, 0]
    mais = [0, 1, 1, 0, 1, 0]
    hif = [0, 0, 1, 0, 0, 1]
    aster = [0, 0, 1, 0, 1, 0]
    divisao = [0, 1, 0, 0, 1, 1]
    igual = [0, 1, 1, 0, 1, 1]
    
    mult = [0, 1, 1, 0, 0, 1]
    numero = [0, 0, 1, 1, 1, 1] 
   
    
    if(a == snap):
        if (flag==1):
            letter='A'
            flag = 0
        else:
            letter='a'   
        
    elif(b==snap):
        if (flag==1):
            letter='B'
            flag=0
        else:
            letter='b'
        
    elif(c==snap):
        if (flag==1):
            letter='C'
            flag=0
        else:
            letter='c'
        
    elif(d == snap):
        if (flag==1):
            letter='D'
            flag=0
        else:
            letter='d'
        
    elif(e == snap):
        if (flag==1):
            letter='E'
            flag=0
        else:
            letter='e'
        
    elif(f == snap):
        if (flag==1):
            letter='F'
            flag=0
        else:
            letter='f'
        
    elif(g == snap):
        if (flag==1):
            letter='G'
            flag=0
        else:
            letter='g'
        
    elif(h == snap):
        if (flag==1):
            letter='H'
            flag=0
        else:
            letter='h'
        
    elif(i == snap):
        if (flag==1):
            letter='I'
            flag=0
        else:
            letter='i'
        
    elif(j == snap):
        if (flag==1):
            letter='J'
            flag=0
        else:
            letter='j'
        
    elif(k == snap):
        if (flag==1):
            letter='K'
            flag=0
        else:
            letter='k'
        
    elif(l == snap):
        if (flag==1):
            letter='L'
            flag=0
        else:
            letter='l'
        
    elif(m == snap):
        if (flag==1):
            letter='M'
            flag=0
        else:
            letter='m'
        
    elif(n == snap):
        if (flag==1):
            letter='N'
            flag=0
        else:
            letter='n'
        
    elif(o == snap):
        if (flag==1):
            letter='O'
            flag=0
        else:
            letter='o'
        
    elif(p == snap):
        if (flag==1):
            letter='P'
            flag=0
        else:
            letter='p'
        
    elif(q == snap):
        if (flag==1):
            letter='Q'
            flag=0
        else:
            letter='q'
        
    elif(r == snap):
        if (flag==1):
            letter='R'
            flag=0
        else:
            letter='r'
        
    elif(s == snap):
        if (flag==1):
            letter='S'
            flag=0
        else:
            letter='s'
        
    elif(t == snap):
        if (flag==1):
            letter='T'
            flag=0
        else:
            letter='t'
        
    elif(u == snap):
        if (flag==1):
            letter='U'
            flag=0
        else:
            letter='u'
        
    elif(v == snap):
        if (flag==1):
            letter='V'
            flag=0
        else:
            letter='v'
        
    elif(w == snap):
        if (flag==1):
            letter='W'
            flag=0
        else:
            letter='w'
        
    elif(x == snap):
        if (flag==1):
            letter='X'
            flag=0
        else:
            letter='x'
        
    elif(y == snap):
        if (flag==1):
            letter='Y'
        else:
            letter='y'
        
    elif(z == snap):
        if (flag==1):
            letter='Z'
            flag=0
        else:
            letter='z'
        
    elif(cedilha == snap):
        letter='ç'
        
    elif(espaco == snap):
        letter=' '
            
    elif(ag == snap):
        letter="á"
    elif(eg == snap):
        letter='é'
    elif(ig == snap):
        letter='í'
    elif(og == snap):
        letter='ó'
    elif(ug == snap):
        letter='ú'
    elif(acr == snap):
        letter='à'
    elif(ecr == snap):
        letter='è'
    elif(icr == snap):
        letter='ì'
    elif(ocr == snap):
        letter='ò'
    elif(ucr == snap):
        letter='ù'
    elif(ac == snap):
        letter='â'
    elif(ec == snap):
        letter='ê'
    elif(oc == snap):
        letter='ô'
    elif(at == snap):
        letter='ã'
    elif(ot == snap):
        letter='õ'
    elif(virg == snap):
        letter=','
    elif(doisp == snap):
        letter=':'
    elif(ponto == snap):
        letter='.'
    elif(inte == snap):
        letter='?'
    elif(excla == snap):
        letter='!'
    elif(pontvirg == snap):
        letter=';'
    elif(hif == snap):
        letter='-'
    elif(abP == snap):
        letter='('
    elif(feP == snap):
        letter=')'
    elif(mais == snap):
        letter='+'
    elif(aster == snap):
        letter='*'
    elif(divisao == snap):
        letter='/'
    elif(igual == snap):
        letter='='
        
    elif(maiuscula == snap):
        flag=1
        letter=''
    elif(numero == snap):
        num = 1
        letter=''
        
    else:
        letter = '#'
    
    return letter, flag
