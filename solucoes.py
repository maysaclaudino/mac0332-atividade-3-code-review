def sao_anagramas(string1, string2):
    
    string1_normalizada = string1.replace(" ", "").lower()
    string2_normalizada = string2.replace(" ", "").lower()

    sorted_string1 = sorted(string1_normalizada)
    sorted_string2 = sorted(string2_normalizada)
    
    return sorted_string1 == sorted_string2

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
