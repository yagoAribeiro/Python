import convert as Conversor

conversor = Conversor.Convert()
num_bin = input("Digite um número: \n")
base = int(input("Digite a base desse número: \n"))
num_decimal = conversor.getDecimal(num_bin, base)

if num_decimal!= None:
    print(f"O valor de {num_bin} na base {base} em decimal é: {num_decimal}")