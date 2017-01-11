
from tkinter import *
y=750

ventana = Tk()
ventana.title("Prueba1-Segundo bimestre")
canvas= Canvas(ventana, width=1000, height=600)
canvas.pack()
imagen1= PhotoImage(file="idle_left.png")
imagen= PhotoImage(file="fondo.png")
canvas.create_image(750,50,anchor=NW, image=imagen1)
canvas.create_image(10,50,anchor=NW, image=imagen)

def mover(event):
    global y
    if event.keysym == 'Left':
        canvas.move(1,-15,0)
        y=y-3
    else:
        canvas.move(1,3,0)


canvas.bind_all('<KeyPress-Left>',mover)
canvas.bind_all('<KeyPress-Right>',mover)


ventana.mainloop()
