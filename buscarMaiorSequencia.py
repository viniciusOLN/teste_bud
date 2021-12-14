#retorna uma lista formatada com strings
def transformarString(lista):
    listaFormatada = list()
    for item in lista:        
            listaFormatada.append(''.join(item))
    return listaFormatada

#função responsável por recuperar todas as sequências do número passado por parâmetro
def recuperarsequences(sequence):
    listFinal = list()
    listPartial = list()
    i = 0       
    while(i < len(sequence)):
        #verifica se chegou ao final da lista                             
        if (i + 1) >= len(sequence):
            #verifica se não possui nenhuma sequência no número
            if len(listPartial) == 0:
                sequence = [str (i) for i in sequence]
                return transformarString(sequence)            
            break 
        #verifica se o numero atual e o próximo são 9 e 0 e fazem parte da sequência
        elif sequence[i] == 9 and sequence[i + 1] == 0:
            #verifica o tamanho da lista parcial de números
            if len(listPartial) > 0:
                #verifica se o numero atual corresponde ao próximo na sequência,
                #se for: adiciona os dois(9 e 0) na listFinal de sequências
                #se não: limpa a lista com os números que estavam antes e adiciona os dois(9 e 0)
                if int(listPartial[len(listPartial) - 1]) == sequence[i] - 1:                     
                    listPartial.append(str(sequence[i]))
                    listPartial.append(str(sequence[i + 1]))
                    listFinal.append(listPartial)
                else:
                    listPartial = list()
                    listPartial.append(str(sequence[i]))
                    listPartial.append(str(sequence[i + 1]))            
            #adiciona na listFinal os dois números
            else:
                listPartial.append(str(sequence[i]))
                listPartial.append(str(sequence[i + 1]))
                listFinal.append(listPartial)
            i = i + 2
        #verifica se o número atual corresponde a sequência
        elif sequence[i] == sequence[i + 1] - 1 or sequence[i] - 1 == sequence[i - 1]: 
            if len(listPartial) > 0:
                #verifica se o número atual corresponde a sequência na listPartial
                if int(listPartial[len(listPartial) - 1]) == sequence[i] - 1:                     
                    listPartial.append(str(sequence[i]))
                    listFinal.append(listPartial)
                else:
                    listPartial = list()
                    listPartial.append(str(sequence[i]))            
            else:
                listPartial.append(str(sequence[i]))
            i = i + 1                          
        else:
            #verifica se a listPartial é maior que 0,
            #se for: adiciona na listFinal a sequência que existe na listPartial
            #limpa a listPartial e logo após adiciona o número do momento nela para
            # ser verificado novamente
            if len(listPartial) > 0:
                listFinal.append(listPartial)
                listPartial = list()
                listPartial.append(str(sequence[i]))                                   
            i = i + 1   
    #retorna a listFinal de números formatada para string                 
    return transformarString(listFinal)

#retorna a maior sequência dentro do número passado
def maiorsequence(sequence):
    if not type(sequence) is int:
        print('por favor, digite somente números')
    else:
        #transforma o número passado em uma lista contendo os dígitos do número
        sequence =  [int (i) for i in str(sequence)]
        #retorna uma lista com as sequências do número        
        sequences = [int (i) for i in recuperarsequences(sequence)]  
        #retorna a maior sequência                        
        print(max(sequences))

def main():
    #casos teste

    maiorsequence(53590)
    maiorsequence(674030098567819)
    maiorsequence(9012364509789)
    maiorsequence('adadadadd')
    maiorsequence(129458987)
    maiorsequence(1239012390)
    maiorsequence(859)

if __name__ == '__main__':
    main()