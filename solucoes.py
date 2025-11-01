def sao_anagramas(string1, string2):
    
    string1_normalizada = string1.replace(" ", "").lower()
    string2_normalizada = string2.replace(" ", "").lower()

    sorted_string1 = sorted(string1_normalizada)
    sorted_string2 = sorted(string2_normalizada)
    
    return sorted_string1 == sorted_string2

def cifra_de_cesar(texto, deslocamento):

    resultado = ""
    
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for c in texto:
        # Verifica se é uma letra minúscula
        if c in alfabeto_minusculo:

            posicao_atual = alfabeto_minusculo.index(c)         
            nova_posicao = (posicao_atual + deslocamento) % 26     
            resultado = resultado + alfabeto_minusculo[nova_posicao]
       
        elif c in alfabeto_maiusculo:
            
            posicao_atual = alfabeto_maiusculo.index(c)
            nova_posicao = (posicao_atual + deslocamento) % 26
            
            resultado = resultado + alfabeto_maiusculo[nova_posicao]
        
        else:
            resultado = resultado + c
    
    return resultado

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
