# ...existing code...
# Loop para garantir que o usuário escolha uma opção válida

# lê peso em kg (float para permitir casas decimais)
peso = float(input("Qual seu peso (kg)?:"))
# lê altura em cm (float); a conversão para metros é feita apenas na saída
altura = float(input("Qual sua altura (cm)?:"))
# lê idade em anos (inteiro)
idade = int(input("Qual sua idade?:"))

# pergunta o sexo até receber 1 (Homem) ou 2 (Mulher)
while True:
    print("\nHomem ou mulher?")
    print("1. Homem \n2. Mulher")
    i = int(input(""))  # lê a opção do usuário

    # fórmula de Mifflin–St Jeor aplicada conforme sexo
    if i == 1:
        # homem: +5 no final da equação
        TMB = 10 * peso + 6.25 * altura - 5 * idade + 5
        break
    elif i == 2:
        # mulher: -161 no final da equação
        TMB = 10 * peso + 6.25 * altura - 5 * idade - 161
        break
    else:
        # entrada inválida — repete o menu
        print("Opção inválida!!!")
        print("Escolha um dos números disponíveis")

# Cria uma string formatada para exibir os dados do usuário
# observa: altura/100 converte cm para metros apenas na exibição
saida_formatada = f"Peso: {peso}\nAltura: {altura/100:.2f} m\nIdade: {idade}"

# Exibe os dados e a TMB formatada (kcal/dia)
print("\n" + saida_formatada)
print(f"Taxa Metabólica Basal: {TMB:.2f} kcal/dia")
