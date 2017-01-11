from tkinter import *
import time
import sys

tk = Tk()
canvas = Canvas(tk,width=1024,heigh=768) #ancho-alto
canvas.pack()
img2 = PhotoImage(file = "F.png") #fondo Ancho1024 Alto 768
#label1 = Label(tk, image=img2)
#label1.grid(row=1,column=1)
#print(img2.size)
img = PhotoImage(file = "M.png") #personaje
canvas.create_image(0,0,anchor=NW,image=img2)
canvas.create_image(1100-(481),768-(600),anchor=NW,image = img)

print("Coordenas Iniciales: " , 0,0)

x = 619
y = 168

def movetriangle(event):    
    global x 
    global y
    if event.keysym == 'Up':
        canvas.move(2, 0, -3) #id grafico,x,y      #ventana=0
        y = y-3
    elif event.keysym == 'Down':
        canvas.move(2, 0, 3)
        y = y+3
    elif event.keysym == 'Left':
        canvas.move(2, -3, 0)
        x = x -3
    else:
        canvas.move(2, 3, 0)
        x = x +3             
    print("Coordenadas Actuales:" , x ,y)
    if x <= 20:
        master = Tk()
        w = Message(master, text="Usted ha hecho un Gooooool")
        w.pack()
        sys.exit(0)
    
    
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()
