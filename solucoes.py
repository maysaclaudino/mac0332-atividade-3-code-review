def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

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

def encontrar_maior_palavra(frase):
    palavras = frase.split(" ")
    
    x = palavras[0]
    for p in palavras:
        if len(p) > len(x):
            x = p
    
    return x
