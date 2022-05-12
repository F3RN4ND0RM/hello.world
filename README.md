# hello.world
Repositorio de trabajos para semana tec

# Carlos Fernando Ramos Mena
## Carlos Fernando Ramos Mena
### Carlos Fernando Ramos Mena

# Estilo
- Negrita **Este texto es negrita**
- Cursiva *Este texto es cursiva*
- Tachado ~Este texto es tachado~
- Negrita y anidad **Este texto es _extremadamente_ imprtante **
- Todo en negrita y cursiva, ***Este texto es importante***

# Emojis
- 🐊
- 🎱
- 🎇

# Citas de Texto
>ITESM

# LISTA PLATILLO
1.  Tacos
2.  Enchiladas suizas
3.  Entomatadas
4.  Costra de queso
5.  Carne Asada

# Lista Desordenada de sus momentos del día de la madre
- Una pintura hecha con dedos
- Comida espacial con sus mejores amigas
- Viaje todo pagado sorpresa
- Un vestido que le gustaba mucho
- Bailar el ratón vaquero


```python
from turtle import *
from freegames import vector
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()
def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO
def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO
def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']
    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None
def store(key, value):
    """Store value in state at key."""
    state[key] = value
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
```
# Enlace
[GitHub Pages](https://www.markdownguide.org/cheat-sheet/)

# Imagen
![GitHub pages](https://tec.mx/sites/default/files/repositorio/Home/tec-de-monterrey-newsroom.jpg)

# Tabla
| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

#Actividades
- [x] Rutina Circulo
- [ ] Rutina Triangulo
- [ ] Rutina Rectangulo

