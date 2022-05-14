# Carlos Fernando Ramos Mena A01197622
## Funciones Añadidas
### def puntuacion():
  - Autor: Carlos Fernando Ramos Mena
  - Calcula los puntos de las celdas descubiertas y despliega el mensaje ganador
  - Código:
  ```python
    def puntuacion():
        if points == 32:
                writer=Turtle()
                writer.hideturtle()
                writer.up()
                writer.goto(-180,0)
                writer.color("White")
                writer.write("felicidades ganaste un auto",font=('Arial', 20, 'normal'))
  ```
### def alumnos_info():
  - Autor: Carlos Fernando Ramos Mena
  - Despliega los datos del autor dentro del programa
  - Código:
  ```python
    def alumnos_info():
        writer=Turtle()
        writer.hideturtle()
        writer.up()
        writer.goto(0,190)
        writer.color("blue")
        writer.write("Carlos Fernando Ramos Mena A01197622")
  ```
  ### def tapCount()::
  - Autor: Carlos Fernando Ramos Mena
  - Cuenta el número de Taps dentro del programa
  - Código:
  ```python3
    def tapCount():
        global count
        writer=Turtle()
        writer.hideturtle()
        writer.up()
        writer.goto(-100,190)
        writer.color("blue")
        writer.write("# taps: "+ str(count))
  ```
  
  ## Funciones Actualizadas:
  ### def draw():
    - Autor: Carlos Fernando Ramos Mena
    - Se le añadio el llamado a la funcion alumnos info() y puntuacion() y se cambio el tamaño de letra a 10
    - Codigo:
    ```python3
      def draw():
          """Draw image and tiles."""
          clear()
          goto(0, 0)
          shape(car)
          stamp()

          for count in range(64):
              if hide[count]:
                  x, y = xy(count)
                  square(x, y)

          mark = state['mark']

          if mark is not None and hide[mark]:
              x, y = xy(mark)
              up()
              goto(x + 2, y)
              color('black')
              write(tiles[mark], font=('Arial',10, 'normal'))


          update()
          ontimer(draw, 100)
          tapCount()
          alumnos_info()
          puntuacion()
    ```
   ### def tap():
    - Autor: Carlos Fernando Ramos Mena
    - Se agrego la variable count para contar el numero de tapas y la variable points que suma los puntos
    - Código:
    ```python3
      def tap(x, y):
          """Update mark and hidden tiles based on tap."""
          spot = index(x, y)
          mark = state['mark']

          if mark is None or mark == spot or tiles[mark] != tiles[spot]:
              state['mark'] = spot        
          else:
              hide[spot] = False
              hide[mark] = False
              state['mark'] = None
              global points
              points = points +1        
          global count
          count = count + 1
    ```
    
