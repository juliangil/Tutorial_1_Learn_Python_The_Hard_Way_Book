print "Hello World!" #El elmemento mas basico que es el imprimir por consola
print "Roosters", 100 - 25 * 3 % 4 #Operacion Basica, utilizando axiomas basicos
print "Is it greater or equal?", 5 >= -2 #Inecuacion

cars = 100
space_in_a_car = 4.0 #Inicializacion de variables (pueden serenteras o booleanas)
my_name = 'Zed A. Shaw' #Variable tipo string
print "Let's talk about %s." % my_name #Impresion de una variable utilizando %s
my_height = 74 #Variable de tipo entero
print "He's %d inches tall." % my_height  #Impresion de una variable utilizando %d

'''
	%s => cadena
	%d => entero
	%u => Entero unsigned 
	%o => Octal 
	%x => Hexadecimal 
	%f => Real
	%ld => Long 
	%lu => Long unsigned
'''

x = "There are %d types of people." % 10 #Varable combinada
print "I said: %r." % x #convierte la variable en string
#percent r (%r) repet the line of the variable x but with one variation, pone entre comillas
hilarious = False #variable booleana

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
print end1 + end2 + end3 + end4 + end5 + end6, #concatenation

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

print "How old are you?",
age = raw_input() #metodo de entrada por consola
age = raw_input("How old are you? ")

from sys import argv #argumentos
script, user_name = argv
print "Hi %s, I'm the %s script." % (user_name, script)

#ARCHIVOS
from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
print "Type the filename again:"
file_again = raw_input("> ") #vuelve a escribir el archivo, solo insertando el nombre
txt_again = open(file_again)
print txt_again.read()
'''
COMANDS BY FILES
close -- Closes the file. Like File->Save.. in your editor.
read -- Reads the contents of the file. You can assign the result to a variable.
readline -- Reads just one line of a text file.
truncate -- Empties the file. Watch out if you care about the file.
write(stuff) -- Writes stuff to the file.
'''

in_file = open(from_file) #Abre
indata = in_file.read( )#lee

print "The input file is %d bytes long" % len(indata) #determina su longitud

print "Does the output file exist? %r" % exists(to_file) #pregunta si existe
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input() #espera respuesta

#FUNCIONES
def print_two(*args): #puede recibir varios argumentos
    arg1, arg2, arg3 = args
    print "arg1: %r, arg2: %r arg3: %r" % (arg1, arg2, arg3)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b #retornamos un valor