# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_base = float(input("Digite o primeiro número: "))
numero_expoente = float(input("Digite o segundo número: "))

calculo_exponenciacao = numero_base**numero_expoente

print(f"{numero_base} elevado a {numero_expoente} é: {calculo_exponenciacao}")
