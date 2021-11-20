# Anki Fisica
Utilizando la aplicacion Anki para repeticion espaciada,
puedes estudiar de manera ordenada, ya sea recordar ecuaciones
que son populares en el campo, pequeños ejercicios y problemas

La repeticion espaciada demuestra ser una de las mejores maneras
de memorizar cosas, vease [`La Curva del Olvido`](https://youtu.be/mlWHKuN47YQ)

<hr/>

# Codigo para Decorar Tarjetas

Siguiendo el video, pega en cada apartado lo que corresponde

<hr> Front Template <hr>
```html
<div class=frontback>
  <div class=texto>
    {{Front}}
  </div>
</div>
```

--- Back Template ---
```html









<hr/>

# Carpetas

### decks
Contiene mazos exportados en formato de anki, listos para utilizar y modificar dentro de anki
### csv
Outputs de CSV funcionales, listos para utilizar y sin errores.
### automation
Contiene jupyternotebooks que nos permite facilitar un poco la sintaxis de latex si te cuesta

## Mazos
    submazo

## Ecuaciones para Memorizar
> Ecuaciones que te ayudara memorizar en fisica

## Escencial para Fisica
> Todo de Fisica Introductoria y algunas utilidades
    Mecanica + Torque
    Unidades
    Algebra, Trionometria Importante y Usada

## Ondas

## Vectores
    Vectores Basico
    Vectores Avanzado

## Algebra
    Logaritmos

## Algebra Lineal
    1 - Sistema de Ecuaciones
    3 - Eigenvalue Problem

## Articulos y Escribirlos
    Citas APPA
    LaTex

## Calculo
    Derivadas
    Integrales
    Ecuaciones Diferenciales
        Series de Potencias y Bessel
        Transformada de Laplace
    Fourier Analysis (incluye ED. Paricales)

## Computacion
    Adobe After Fx Shortcuts
    Algoritmos
    C++
    JavaScript y FrontEnd
    Jupyter Notebook
    Python
        Data Science
        Listas
        Plotly
        Sympy
    Regular Expressions

## Electrodinamica
    1 - Electroestatica
    2 - Circuitos
    3 - Magnetoestatica
    Metodo de Green > Este es mas avanzado

## Estadistica
    Probabilidad y Estadistica

## Fisica de Gases
    Termodinamica

## Fisica Moderna

## Mecanica Cuantica

## Mecanica Intermedia

## Metodos Matematicos 2

## Metodos Matematicos Libro Boas


### Tags presentes en todo el proyecto
Ver el archivo .txt de Tags existentes (es algo extenso)

## Deseo Contribuir
Genial! Debes, puedes modificar los formatos .CSV, los cuales los exporte usando la extension de anki:
https://ankiweb.net/shared/info/1478130872

Todo lo que es `LaTex` dentro de Anki se hace con `MathJax`, debes de usar `\( tu ecuacion \)` cada vez que quieras escribir una ecuacion. A mi me ayuda ver en tiempo real como va quedando, asi que utilizo esto:

http://www.texrendr.com/

Renderiza en tiempo real codigo de LaTex, por tanto es escencial para mejorar el flujo de trabajo.

Este proyecto se nutre de distintas fuentes, algunos cursos en YouTube y otras de mis notas personales.
Dejo adjunta algunas fuentes que utilizo

## Referencias

[1] Zetilli, N. (2009). Quantum Mechanics: Concepts and Applications (2da ed.). Wiley.
[2] Griffiths, D. (1999). Introduction to electrodynamics (3ra ed.). Prentice-Hall.
[3] Vargas, L. (2010). Apuntes de Electromagnetismo. https://www.u-cursos.cl/usuario/e7fc0ba9bcbf9574ec297b783608d078/mi_blog/r/electro_vargas.pdf
[4] FreecodeCamp. https://www.youtube.com/c/Freecodecamp
