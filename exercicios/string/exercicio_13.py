# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Escreva uma frase: ")

frase_limpa_espacos = frase.strip()

print(frase_limpa_espacos)
