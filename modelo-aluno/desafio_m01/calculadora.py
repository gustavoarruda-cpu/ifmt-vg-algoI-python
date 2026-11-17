
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

op = input("Digite a opção: ")

if op == "1":
    print("Resultado:", num1 + num2)

elif op == "2":
    print("Resultado:", num1 - num2)

elif op == "3":
    print("Resultado:", num1 * num2)

elif op == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Não é possível dividir por zero!")

else:
    print("Opção inválida!")
