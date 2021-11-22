# Anki Fisica
Utilizando la aplicacion Anki para repeticion espaciada,
puedes estudiar de manera ordenada, ya sea recordar ecuaciones
que son populares en el campo, pequeños ejercicios y problemas

La repeticion espaciada demuestra ser una de las mejores maneras
de memorizar cosas, vease [`La Curva del Olvido`](https://youtu.be/mlWHKuN47YQ)

<hr/>

# Codigo para Decorar Tarjetas

Siguiendo el video, pega en cada apartado lo que corresponde

_________________ Front Template _________________
```html
<div class=frontback>
  <div class=texto>
    {{Front}}
  </div>
</div>
```

_________________ Back Template __________________
```html
{{FrontSide}}

<hr id=answer>
<div class=frontback>
  <div class=texto>
    {{Back}}
  </div>
</div>
```

____________________ Styling _____________________
```css
card {
 font-family: arial; /*tipo de letra*/
 font-size: 20px; /*tamaño de letra en pixeles*/
}
body {
  background: transparent;  
}

/*______________ Aqui es donde quieres modificar ______________*/
/*Esta seccion te permite modificar todo lo del background*/
html {
  background-color: #454545;
}

.texto{
  text-align: center;  /*left, right, center son configuraciones posibles*/
  color: black; /* para un color en hexadecimal #nnnnnn <-son 6 numeros luego de un '#'*/
}

.frontback{
  padding: 20px;
  /*controla el color de la carta*/
  background-color: white;
  border-radius:30px;
}

/*Config para Ecuaciones de Mates*/
.MathJax {
   /*color de la letra*/
   color: white;
}
/*__________________________________________________________*/

```

## Webs habladas

[Paletas de Colores](https://colorhunt.co/palettes/popular)

[Gradiente para tu fondo](https://cssgradient.io/)

## Fondo para resaltar ecuaciones

Aqui te dejo preparado algo de codigo por si quieres explorar

### Atardecer

![image](https://user-images.githubusercontent.com/42480199/142807698-510880d2-f9a4-48d3-ba5d-93de465336d6.png)


```css
.MathJax {
    /*color de la letra*/
    color: white;

    /*esto es para darle un fondo a las ecuaciones para resaltarlas*/
    padding: 0 12px 7px 12px; /*deja espacio extra*/
    border-radius: 15px;
    
    /*gradiente Atardecer*/
    background: rgb(131,58,180);
    background: linear-gradient(9deg, rgba(131,58,180,1) 42%, rgba(253,29,29,1) 84%, rgba(252,176,69,1) 100%);
}
```
### Azulito

![image](https://user-images.githubusercontent.com/42480199/142807733-88b8b05d-b1c4-406f-a7bd-62f13396b701.png)

```css
/*Config para Ecuaciones de Mates*/
.MathJax {
    /*color de la letra*/
    color: white;

    /*esto es para darle un fondo a las ecuaciones para resaltarlas*/
    padding: 0 12px 7px 12px; /*deja espacio extra*/
    border-radius: 15px;

    /*gradiente Azulito*/
    background: rgb(119,228,212);
    background: linear-gradient(356deg, rgba(119,228,212,1) 13%, rgba(132,193,221,1) 25%, rgba(153,140,235,1) 59%);
}
```


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
