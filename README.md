# Anki Fisica
Utilizando la aplicacion Anki para repeticion espaciada,
puedes estudiar de manera ordenada, ya sea recordar ecuaciones
que son populares en el campo, pequeños ejercicios y problemas

La repeticion espaciada demuestra ser una de las mejores maneras
de memorizar cosas, vease `La Curva del Olvido`



## Carpetas

### decks
Contiene mazos exportados en formato de anki, listos para utilizar y modificar dentro de anki

### csv
Outputs de CSV funcionales, listos para utilizar y sin errores.

### automation
Contiene jupyternotebooks que nos permite facilitar un poco la sintaxis de latex si te cuesta

## Por que existen distintos mazos y no solo 1?
La fisica y matematica se divide no solo en ecuaciones que debes de recordar, pero tambien de situaciones
que al ejercitarlas acabas con un conocimiento mayor. 
Los veo como cosas complementarias pero conveniente separarlas si nos vemos debiles en alguna.

### decks/Electrodinamica
Desde la materia de electroestatica, formulas de capacitancia, demostrar propiedades vectoriales
y distintos ejercicios que deben de sernos de 2da naturaleza para el estudio

### decks/LaTex
Desde como construir una tabla a los simbolos y funciones

### ecuaciones
Se concentra en ecuaciones de la fisica que debemos de recordar o saber llegar a ellas de manera rapida

Aqui encontraras:
  * La transformacion de Lorentz
  * Ecuacion de Relatividad Especial
  * Ecuaciones de Maxwell
  * ...
  
### ejericios
Problemas de fisica, se nos da un caso y que aplicar para resolverlo.

Aqui encontraras:
  * Una masa con resortes
  * ...

### calculo
Esto tambien se refiere a ejercicios y derivacion de cosas, pero unicamente
hablamos de calculo.

Aqui encontraras:
  * Ecuaciones diferenciales
  * Teoremas que recordar o demostrar
  * ...

### integrales
Gran parte de la fisica es calculo y gran parte del calculo son integrales

Aqui encontraras:
  * Formulas que uno suele memorizar
  * Ejercicios para ponerte a prueba
  * ...


## Tags presentes en todo el proyecto
### Matematicas
* complex
* integral
* theorem
* physics
* formula
* derivative

### Fisica
* waves
* quantum
* evolution
* operator
* relativity
* transformation

## Deseo Contribuir
Genial! Los documentos a modifcar son los csv, significa comma separated value, osea que todo lo que dejes una coma sera una columna, actualmente por convencion las 3 columnas son: Pregunta, Respuesta, Tags

Todo lo que es `LaTex` dentro de Anki se hace con `MathJax`, debes de usar `\( tu ecuacion \)` cada vez que quieras escribir una ecuacion. A mi me ayuda ver en tiempo real como va quedando, asi que utilizo esto:

http://www.texrendr.com/

Renderiza en tiempo real codigo de LaTex, por tanto es escencial para mejorar el flujo de trabajo.
