class Convert:
    
    def getDecimal(self, string, base):
        
        #Variáveis
        total = 0
        hex = False
        negative = False
        string = string.upper()
        position = len(string)-1
        
        
        #Negative
        negative = True if string.startswith("-") else False 
        if(string.startswith("-")):
            string = string.replace("-", "")
        
                
        #Laço e conta
        for char in string:
            
            #Base
            match(base):
                case 2: 
                    if(char in "98765432"):
                        return print("Esse número não é de base 2!")
                case 8: 
                    if(char in "98"):
                        return print("Esse número não é de base 8!")
                case 16: 
                    hex = True
                case _:
                    return print("Base não reconhecida!")
                
                
            if hex == True and char not in "9876543210":
                    match(char):
                        case 'A':
                            total += int(10)*(base**position)
                        case 'B':
                            total += int(11)*(base**position)
                        case 'C':
                            total += int(12)*(base**position)
                        case 'D':
                            total += int(13)*(base**position)
                        case 'E':
                            total += int(14)*(base**position)
                        case 'F':
                            total += int(15)*(base**position)
                        case _:
                            return print("Esse número não é de base 16!")
            else:
                total += int(char)*(base**position)
            
            position-=1
            
        #print negative
        if negative:
            return -total
        else: 
            return total
        

    def getFromBase(self, decimal, base):

        string = ""
        bases = [16, 2, 8]
        while(decimal>=base):
            if base==16 and decimal%base>9:
                string += str(self.getHex(decimal%base))
            else:
                string += str(int(decimal%base))
            
            decimal//= base 
        if base==16:
            string += str(self.getHex(decimal))
        else:
            string += str(decimal)
        #reverter string
        #:: = começa do último índice
        #-1 = a leitura será feita de 1 em um índice ao contrário
        string = string[::-1]
        
        if base not in bases:
            return print("Base não reconhecida")
        return string

    
    def getHex(self, num):

            match(num):
                case 10:
                    return "A"
                case 11:
                    return "B"
                case 12:
                    return "C"
                case 13:
                    return "D"
                case 14:
                    return "E"
                case 15:
                    return "F"
                case _:
                    return num