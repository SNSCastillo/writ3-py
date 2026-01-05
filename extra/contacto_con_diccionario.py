
### Extra
print('=*' * 30)

def agenda_cont():
    
    agenda = {}

    def ins_contac():
        telef = input('Introducir telefono: ')
        if telef.isdigit() and len(telef) <= 10:
            agenda[nom] = telef
        else:
            print('El telefono no puede tener  mas de 9 igitos')

    while True:
        print('')
        print('Menu Opciones')
        print('1. Buscar contacto')
        print('2. Insertar contacto')
        print('3. Actualizar contacto')
        print('4. Eliminar contacto')
        print('5. Salir')

        option = input('\nSeleccione una opcion: ')

        match option:
            case '1':
                nom = input('Introduce el nombre del contacto a buscar: ')
                if nom in agenda:
                    print(f'El telefono de {nom} es {agenda[nom]}.')
                else:
                    print(f'El contacto {nom} no existe.')
            case '2':
                nom = input('Introduce el nombre del contacto: ')
                ins_contac()
            case '3':
                nom = input('introduce nombre del contacto a actulizar: ')
                if nom in agenda:
                    ins_contac()
                else:
                    print(f'El contacto {nom} no existe debes crearlo.')
            case '4':
                nom = input('Introduce el nombre del contacto a borrar: ')
                if nom in agenda:
                    del agenda[nom]
                else:
                    print(f'El contacto {nom} no existe no se puede borrar.')
            case '5':
                print('Hasta pronto')
                break
            case _:
                print('Opcion no valida elije una opcion entre el 1 y el 5')

agenda_cont()