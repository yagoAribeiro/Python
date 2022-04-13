import convert as Conversor

conversor = Conversor.Convert()

while(True):

    op = input("\nDigite a operação:\n1 - Converter de outras bases para decimal\n2 - Converter de decimal para outras bases\n3 - Encerrar\n")
    
    match(op):
        case "1":
            num = input("Digite um número: \n")
            base = int(input("Digite a base desse número: \n"))
            num_decimal = conversor.getDecimal(num, base)
            if num_decimal!= None:
                print(f"\nO valor de {num} na base {base} em decimal é: {num_decimal}")
        
        case "2":
            num = int(input("Digite um número decimal: \n"))
            base = int(input("Digite a base para conversão: \n"))
            new_num = conversor.getFromBase(num, base)
            if new_num!= None:
                print(f"\nO valor de {num} decimal na base {base} é: {new_num}")
        
        case "3":
            break
print("Programa encerrado!")