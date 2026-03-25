historico = []

while True:
    print("\n--- SISTEMA DE SAÚDE ---")

    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura ** 2)

    # Classificação
    if imc < 18.5:
        categoria = "Abaixo do peso"
        dica = "Tente melhorar a alimentação."
    elif imc < 25:
        categoria = "Peso normal"
        dica = "Continue mantendo hábitos saudáveis."
    elif imc < 30:
        categoria = "Sobrepeso"
        dica = "Atenção na alimentação e exercícios."
    else:
        categoria = "Obesidade"
        dica = "Procure orientação de saúde."

    historico.append(imc)

    print(f"\nIMC: {imc:.2f}")
    print(f"Categoria: {categoria}")
    print(f"Dica: {dica}")

    opcao = input("\nDeseja calcular novamente? (s/n): ")
    if opcao.lower() != "s":
        break

# Mostrar histórico
print("\n--- HISTÓRICO DE IMC ---")
for i, valor in enumerate(historico):
    print(f"{i+1}ª medição: {valor:.2f}")