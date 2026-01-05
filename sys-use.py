import sys
if __name__ == "__main__":
    print("Nombre del script:", sys.argv[0])
    print("Número de argumentos:", len(sys.argv) - 1)
    print("Los argumentos que se pasaron son:", sys.argv[1:])