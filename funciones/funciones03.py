def menu():
        opcion=' '
        while not ('a'<= opcion <= 'c'):
            print("cajero automatico")
            print("a) ingresar dinero")
            print("b) sacar dinero")
            print("c) consultar saldo")
            opcion = input("escoja una opcion > ")
            if not (opcion >= 'a' and opcion <= 'c'):
                print("solo se pueden elegir las opciones a, b y c  ")
            return opcion

menu()
