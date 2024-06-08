class Libro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    #Setters y Getters
    
    def imprimirAtributos(self):
        print("El titulo es: " + self.__titulo)
        print("El autor es: " + self.__autor)
        print("Tengo " + str(self.__paginas) + " páginas")

libro1 = Libro(
    "La Edad de Oro",
    "Jose Marti",
    800
)
libro1.imprimirAtributos()