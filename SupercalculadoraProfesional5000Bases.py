#ID: 388954
import math
Menu = (" ")
while Menu != ("1000"):
    print ("Este programa hace conversiones escoja la opcion que necesite convertir.")
    print ("*************************************************************************************")
    print ("¨1¨   //Decimal a Binario")
    print ("¨2¨   //Binario//Este tiene mas opciones: ¨Conversiones de binario a las demas bases¨//")
    print ("¨3¨   //Octal a Binario")
    print ("¨4¨   //Hexadecimal a Binario")
    print ("¨5¨   //Para ver una pequeña tabla de conversiones como ejemplo xd")
    print ("¨1000¨//Para terminar la ejecución del programa")
    Menu = input("Digite una opción: ")
    if Menu == ("1"):
        Decimal = int(input("Digite el numero Decimal que quiere convertir a Binario: "))
        Binario = ""
        if (Decimal > 0):
            while(Decimal > 0):
                if (Decimal%2 == 0):
                    Binario = "0" + Binario
                else:
                    Binario = "1" + Binario
                Decimal = int(math.floor(Decimal/2))
        else:
            if (Decimal == 0):
                Binario = "0"
            else:
                Binario = "ERROR404 :v (Asegurese que es un numero decimal y que sea positivo)"
        print ("El Decimal convertido a Binario es: "+Binario)
        print ("//////////////////////////////////////////////////////////////////////////")

    elif Menu == ("2"):
        MenuBin = ""
        while MenuBin != ("1000"):
            print ("/////*****¿A que ¨Base¨ quiere convertir el numero Binario?*****/////")
            print ("¨1¨   //Binario a Decimal^10")
            print ("¨2¨   //Binario a Octal^8")
            print ("¨3¨   //Binario a Hexadecimal^16")
            print ("¨1000¨//Para regresar al Menu de ¨Bases^¨")
            MenuBin = input("Digite respuesta aqui: ")
            if MenuBin == ("1"):
                NumeroDeci=int(input("Ingrese un número en Binario ¨Ejem:110 = 6 O 11 = 3¨ Sin encadenar:"))
                j=NumeroDeci
                Suma=0
                i=0
                Binarioxd=NumeroDeci
                while(i<j):
                    LastNumber=Binarioxd%10
                    Binarioxd=int(Binarioxd/10)
                    if(LastNumber==0 or LastNumber==1):
                        Suma=Suma + 2**i *LastNumber
                    i=i+1
                print(Suma)
            if MenuBin == ("2"):
                print("¨1000¨ Para cerrar el programa");
                BinaryOMG = input("Digite un numero en Binario para convertir a Octal Ejm;¨1001 = 11¨: ");
                if BinaryOMG == '1000':
                    exit();
                else:
                    temp = int(BinaryOMG, 2);
                    print(BinaryOMG,"En octal =",oct(temp));
            elif MenuBin == ("3"):
                print("¨1000¨ Para cerrar el programa");
                BinaryHex = input("Digite un numero en Binario para convertir a Hexadecimal Ejm;¨1100¨ = c: ");
                if BinaryHex == '1000':
                    exit();
                else:
                    temp = int(BinaryHex, 2);
                    print(BinaryHex,"En Hexadecimal =",hex(temp));

    elif Menu == ("3"):
        print("¨1000¨ Para cerrar el programa");
        print ("Base 8 = 0-7. Si se digita un numero con 8 o 9 el programa se cerrara :'c")
        Octal = input("Digite el numero Octal que desee convertir a Binario: ");
        if Octal == '1000':
            exit();
        else:
            dec = str(int(Octal, 8));
            decm = int(dec);
            print(Octal,"En Binario =",bin(decm));

    elif Menu == ("4"):
        print("¨1000¨ Para cerra el programa");
        print ("Si digita por Ejm: 14 el programa mostrara = 10100 Lo ideal es que digite ¨E¨")
        Hexdec = input("Digite el numero Hexadecimal que quiere convertir a Binario: ");
        if Hexdec == '1000':
            exit();
        else:
            dec = int(Hexdec, 16);
            print(Hexdec,"En Binario =",bin(dec));
    
    elif Menu == ("5"):
        Matriz = Matriz = [["1","1","001","001"],["2","2","002","010"],["3","3","003","011"],["4","4","004","100"],["5","5","005","101"],["6","6","006","110"],["7","7","007","111"],["8","8","010","1000"],["9","9","011","1001"],["10","A","012","1010"]]
        for i in range(len(Matriz)):
            for h in range(len(Matriz[i])):
                print(Matriz[i][h],end=" ")
            print ( )
        print ( )
        print ("La Tabla esta arriba---xd-Algunos algoritmos del programa requieren que los binarios se escriban sin encadenar.")