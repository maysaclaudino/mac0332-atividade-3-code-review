def sao_anagramas(string1, string2):
    
    string1_normalizada = string1.replace(" ", "").lower()
    string2_normalizada = string2.replace(" ", "").lower()
    
    contagem1 = {}
    contagem2 = {}
    
  
    for letra in string1_normalizada:
        if letra in contagem1:
            contagem1[letra] = contagem1[letra] + 1
        else:
            contagem1[letra] = 1
    
    
    for letra in string2_normalizada:
        if letra in contagem2:
            contagem2[letra] = contagem2[letra] + 1
        else:
            contagem2[letra] = 1
    
   
    return contagem1 == contagem2

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
