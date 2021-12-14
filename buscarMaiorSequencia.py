#retorna uma lista formatada com strings
def transformarString(lista):
    listaFormatada = list()
    for item in lista:        
            listaFormatada.append(''.join(item))
    return listaFormatada

#função responsável por recuperar todas as sequências do número passado por parâmetro
def recuperarSequencias(sequencia):
    listaFinal = list()
    listaParcial = list()
    i = 0       
    while(i < len(sequencia)):
        #verifica se chegou ao final da lista                             
        if (i + 1) >= len(sequencia):
            #verifica se não possui nenhuma sequência no número
            if len(listaParcial) == 0:
                sequencia = [str (i) for i in sequencia]
                return transformarString(sequencia)            
            break 
        #verifica se o numero atual e o próximo são 9 e 0 e fazem parte da sequência
        elif sequencia[i] == 9 and sequencia[i + 1] == 0:
            #verifica o tamanho da lista parcial de números
            if len(listaParcial) > 0:
                #verifica se o numero atual corresponde ao próximo na sequência,
                #se for: adiciona os dois(9 e 0) na listaFinal de sequências
                #se não: limpa a lista com os números que estavam antes e adiciona os dois(9 e 0)
                if int(listaParcial[len(listaParcial) - 1]) == sequencia[i] - 1:                     
                    listaParcial.append(str(sequencia[i]))
                    listaParcial.append(str(sequencia[i + 1]))
                    listaFinal.append(listaParcial)
                else:
                    listaParcial = list()
                    listaParcial.append(str(sequencia[i]))
                    listaParcial.append(str(sequencia[i + 1]))            
            #adiciona na listaFinal os dois números
            else:
                listaParcial.append(str(sequencia[i]))
                listaParcial.append(str(sequencia[i + 1]))
                listaFinal.append(listaParcial)
            i = i + 2
        #verifica se o número atual corresponde a sequência
        elif sequencia[i] == sequencia[i + 1] - 1 or sequencia[i] - 1 == sequencia[i - 1]: 
            if len(listaParcial) > 0:
                #verifica se o número atual corresponde a sequência na listaParcial
                if int(listaParcial[len(listaParcial) - 1]) == sequencia[i] - 1:                     
                    listaParcial.append(str(sequencia[i]))
                    listaFinal.append(listaParcial)
                else:
                    listaParcial = list()
                    listaParcial.append(str(sequencia[i]))            
            else:
                listaParcial.append(str(sequencia[i]))
            i = i + 1                          
        else:
            #verifica se a listaParcial é maior que 0,
            #se for: adiciona na listaFinal a sequência que existe na listaParcial
            #limpa a listaParcial e logo após adiciona o número do momento nela para
            # ser verificado novamente
            if len(listaParcial) > 0:
                listaFinal.append(listaParcial)
                listaParcial = list()
                listaParcial.append(str(sequencia[i]))                                   
            i = i + 1   
    #retorna a listaFinal de números formatada para string                 
    return transformarString(listaFinal)

#retorna a maior sequência dentro do número passado
def listaFinaluencia(sequencia):
    if not type(sequencia) is int:
        print('por favor, digite somente números')
    else:
        #transforma o número passado em uma lista contendo os dígitos do número
        sequencia =  [int (i) for i in str(sequencia)]
        #retorna uma lista com as sequências do número        
        sequencias = [int (i) for i in recuperarSequencias(sequencia)]  
        #retorna a maior sequência                        
        print(max(sequencias))

def main():
    #casos teste
    
    listaFinaluencia(53590)
    listaFinaluencia(674030098567819)
    listaFinaluencia(9012364509789)
    listaFinaluencia('adadadadd')
    listaFinaluencia(129458987)
    listaFinaluencia(1239012390)
    listaFinaluencia(859)

if __name__ == '__main__':
    main()