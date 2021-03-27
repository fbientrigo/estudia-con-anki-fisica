#Libreria para utilizar en automation.ipynb
# aqui todas las funciones ocupadas para hacerlo mas ordenado


# Objeto Principal
# Toda linea se guarda dentro de una clase, de esa manera
# podemos sumarlas (que las concatena con un salto de linea)
# y dejar espacios en blancos para modificarlas a gusto
class Linea:
    #inicializa
    def __init__(self,pregunta, solucion = '' , tags = ''):
        self.pregunta = pregunta
        self.solucion = solucion
        self.tags = tags
        self.linea = self.pregunta + " , " + self.solucion + " , " + self.tags
    
    #esto nos permtie imprimirla de manera que tenga sentido
    def __repr__(self):
        return self.linea

    #Aqui ocurre la magia, agregamos un salto de linea entre cada suma
    def __add__(self,other):
        #en el caso de que sea la suma con un string y no objeto clase
        if (type(other) == str):
            return self.linea + "\n" + other

        else: 
            return self.linea + "\n" + other.linea



def copy(source, destiny):
    """
    Crea una copia del archivo source a destiny, se hace con una sola
    variable, asi que ojo a que sucede con archivos grandes
    """
    #Copy
    fs = open(source, "r")
    _ = fs.read()
    
    #Paste, sobreescribira
    fd = open(destiny,"w")
    fd.write(_)
    fd.close()

    print("Copia realizada con exito")

def escribir(destino, texto, opt = "w"):
    """
    Escribe en el fichero, nos ahorra sintaxis, opt controla
    que sucede con el fichero
    'w' es para sobreescribir y crear
    'a' es para agregar al final sin borrar lo anterior
    """
    f = open(destino,opt)
    f.write(texto)
    f.close()
    print("Escritura realizada con exito")