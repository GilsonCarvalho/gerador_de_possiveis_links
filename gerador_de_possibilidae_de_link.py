import itertools

# Define a lista de caracteres que podem ser usados para preencher o link
caracteres = "0123456789abcdefghijklmnopqrstuvwxyz"

# Define o link incompleto
link_incompleto = "https://mega.nz/folder/&&&uiguigwsiugwgiwu"

# Gera todas as combinações de 3 caracteres possíveis
comb = itertools.product(caracteres, repeat=3)

# Abre um arquivo de texto para escrever os links gerados
with open("links.txt", "w") as arquivo:

    # Escreve cada link possível em uma linha do arquivo de texto
    for c in comb:
        link_completo = link_incompleto.replace("&&&", "".join(c))
        arquivo.write(link_completo + "\n")