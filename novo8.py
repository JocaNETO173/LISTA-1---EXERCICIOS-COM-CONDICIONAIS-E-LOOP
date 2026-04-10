# 8. Escreva um algoritmo que recebe uma sequência de DNA e que percorre essa sequência imprimindo, para cada posição, 
# qual é o nome do nucleotídeo da posição. Por exemplo: dada a sequência AGGTC, o seu algoritmo deve imprimir a seguinte saída:

# 1 – A: Adenina
# 2 – G: Guanina
# 3 – G: Guanina
# 4 – T: Timina
# 5 – C: Citosina

# Caso a sequência possua algum caractere diferente dos descritos acima, o seu algoritmo deve escrever: “Nucleotídeo inválido!”

sequencia = input('Digite a sequência de DNA: ').upper()
index = 0
SequenciaValida = True

while(index < len(sequencia)):
    if(sequencia[index] not in ['A','C','G','T']):
        print('Nucleotídeo Inválido!')
        SequenciaValida = False
        break
    index += 1

if(SequenciaValida == True):
    index = 0
    while(index < len(sequencia)):
        if(sequencia[index] == 'A'):
            print(f"{index + 1} - A: Adenina")
        elif(sequencia[index] == 'C'):
            print(f"{index + 1} - C: Citosina")
        elif(sequencia[index] == 'G'):
            print(f"{index + 1} - G: Guanina")
        elif(sequencia[index] == 'T'):
            print(f"{index + 1} - T: Timina")
        index += 1
