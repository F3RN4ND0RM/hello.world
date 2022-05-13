# Actividad 2 Modificacón del juego paint
## Autor:
- Carlos Fernando Ramos Mena A01197622

## Funciones agregadas
### def_info_alumnos()
- Despliega información de los alumnos
- Autor: Carlos Fernando Ramos Mena
- Código:
  
  ```python
    def info_alumnos():
      up()
      goto(0,190)
      color("blue")
      write("Carlos Ramos A01197622")
    ```
### def circle(start, end)
- Dibuja un circulo con radio click inicial - click final
- Autor: Carlos Fernando Ramos Mena
- Código:
  
  ```python
      up()
    goto(end.x, end.y)
    down()
    begin_fill()
    left(90)

    for count in range(20):
        forward((end.x - start.x)/3.1416)
        left(18)

    end_fill()
    left(270)
    ```
### rectangle(start, end)
- Dibuja un rectangulo con lados click inicial - click final y altura (click inicial - click final)/2
- Autor: Carlos Fernando Ramos Mena
- Código:
  ```python
  def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()


    forward(end.x - start.x)
    left(90)
    forward((end.x - start.x)/2)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward((end.x - start.x)/2)
    left(90)
    end_fill()
    ```
### rectangle(start, end)
- Dibuja un trignulo equilatero
- Autor: Carlos Fernando Ramos Mena
-Código:
  ```python
  def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()


    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)
    left(120)

    end_fill()
    ```
    ## Ejemplos:
    ![image](https://drive.google.com/uc?export=view&id=<1AOWGJ2ZHkgyffqDzxjbQAgSMzIkndRe3>)
    ![image](https://drive.google.com/uc?export=view&id=<12aCG9Qnr_oEKZTO7r7anvsW71llHk2Iq>)
