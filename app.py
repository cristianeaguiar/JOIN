# lista
campos_endereco = ["Plano Piloto", "Asa Sul", "SQS 210", "Bloco A", "Apartamento 303"]
                   
#  delimitador
delimitador = ", "   

# junta os valores em uma única variável
endereco = delimitador.join(campos_endereco)

# exibe a variável na tela
print(f"Endereço: {endereco}.")