#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#pyparsing: libreria para ayudar en la identificación de los elementos que 
#pertenecen a una expresión regular
###Word: identifica y retonra una palabra concreta dentro de una línea
###Regex: identifica y retorna la cadena que cumpla con una expresión regular dada
###Literal: identifica y retorna la cadena que cumpla exactamente con la descripción dada
from pyparsing import Word, Regex, Literal, OneOrMore, ParseException, MatchFirst
#uso de la consola como metodo de entrada
import sys
#uso de expresiones regulares
import re

def main(index,line):
  
          
   # Do something with this data.
   if line is not None:
      try:
	
	operator = Regex(r'(?<![\+\-\^\*/%])[\+\-]|[\^\*/%!]')
	function = Regex(r'[a-zA-Z_][a-zA-Z0-9_]*(?=([ \t]+)?\()')
	variable = Regex(r'[+-]?[a-zA-Z_][a-zA-Z0-9_]*(?!([ \t]+)?\()')
	number = Regex(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')
	lbrace = Word('(')
	rbrace = Word(')')
	assign = Literal(':=')
	linebreak = Word('\n')
	skip = Word(' \t')
           
	lexOnly = operator | function | variable | number | lbrace \
            | rbrace | assign | linebreak | skip
	
        lexAllOnly = OneOrMore(lexOnly)
         
        print lexAllOnly.parseString(line)
        print '\n------------------------------\n'
      except ParseException, err:
         print err.line
         print " "*(err.column-1) + "^"
         print "Error en la linea, {index}, columna: {e.col} elemento no identificado".format(e=err,index=index)
         print '\n------------------------------\n'
   else:
      print 'Invalid parameters.\n'
      sys.exit(1)
    
#función main    
if __name__ == "__main__":
  #se captura la dirección del archivo donde se encuentra el código a evaluar
  FILENAME=sys.argv[1:]
  #se abre el archivo 
  f = open(''.join(FILENAME))
  #se guarda una lista con cada una de las líneas
  content_file = f.readlines()
  f.close()
  for index, line in enumerate(content_file):
    print '('+str(index)+')'+'->', line
    main(index,line)
