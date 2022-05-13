# Carlos Fernando Ramos Mena A01197622

## Autor:
- Carlos Fernando Ramos Mena

##Funciones Agregadas
### def foodMove()
  - Controla Movimiento de la comida
  - Autor: Carlos Fernando Ramos Mena
  - Código:
  '''phyton3
      def foodMove():
        rNumber = randrange(1,5)

        if rNumber == 1 and inside(vector(food.x+10,food.y)):
            food.x = food.x + 10        
        if rNumber == 2 and inside(vector(food.x-10,food.y)):
            food.x = food.x - 10    
        if rNumber == 3 and inside(vector(food.x,food.y+10)):
            food.y = food.y + 10
        if rNumber == 4 and inside(vector(food.x,food.y-10)):
            food.y = food.y - 10
    '''
