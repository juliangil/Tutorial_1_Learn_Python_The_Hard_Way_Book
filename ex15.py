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