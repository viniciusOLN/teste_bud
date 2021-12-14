def transformarString(lista):
    listaFormatada = list()
    for item in lista:        
            listaFormatada.append(''.join(item))
    return listaFormatada

def recuperarSequencias(sequencia):
    maiorSeq = list()
    menorSeq = list()
    i = 0       
    while(i < len(sequencia)):                             
        if (i + 1) >= len(sequencia):
            if len(menorSeq) == 0:
                sequencia = [str (i) for i in sequencia]
                return transformarString(sequencia)            
            break 
        elif sequencia[i] == 9 and sequencia[i + 1] == 0:
            if len(menorSeq) > 0:
                if int(menorSeq[len(menorSeq) - 1]) == sequencia[i] - 1:                     
                    menorSeq.append(str(sequencia[i]))
                    menorSeq.append(str(sequencia[i + 1]))
                    maiorSeq.append(menorSeq)
                else:
                    menorSeq = list()
                    menorSeq.append(str(sequencia[i]))
                    menorSeq.append(str(sequencia[i + 1]))            
            else:
                menorSeq.append(str(sequencia[i]))
                menorSeq.append(str(sequencia[i + 1]))
            i = i + 2
        elif sequencia[i] == sequencia[i + 1] - 1 or sequencia[i] - 1 == sequencia[i - 1]: 
            if len(menorSeq) > 0:
                if int(menorSeq[len(menorSeq) - 1]) == sequencia[i] - 1:                     
                    menorSeq.append(str(sequencia[i]))
                    maiorSeq.append(menorSeq)
                else:
                    menorSeq = list()
                    menorSeq.append(str(sequencia[i]))            
            else:
                menorSeq.append(str(sequencia[i]))
            i = i + 1                  
        else:
            if len(menorSeq) > 0:
                maiorSeq.append(menorSeq)
                menorSeq = list()
                menorSeq.append(str(sequencia[i]))                                   
            i = i + 1   
    if len(maiorSeq) == 0:
        maiorSeq.append(menorSeq)   
              
    return transformarString(maiorSeq)

def maiorSequencia(sequencia):
    if not type(sequencia) is int:
        print('por favor, digite somente números')
    else:
        sequencia =  [int (i) for i in str(sequencia)]        
        sequencias = [int (i) for i in recuperarSequencias(sequencia)]                          
        print(max(sequencias))

def main():
    maiorSequencia(53590)
    maiorSequencia(674030098567819)
    maiorSequencia(9012364509789)
    maiorSequencia('adadadadd')
    maiorSequencia(129458987)
    maiorSequencia(1239012390)
    maiorSequencia(859)

if __name__ == '__main__':
    main()

