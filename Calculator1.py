# Importing

from tkinter import*

# GUI interaction 

window = Tk()
window.geometry('500x500')
window.config(bg= "black")
window.title("My Calculator")

# Adding input 
# 👇 Upar text (heading) add karna

heading = Label(window, text=" Calculator App ", font=("Arial", 50, "bold"), bg="black", fg="white" ,)
heading.pack(pady=10)

e = Entry(window , width=77, borderwidth= 8 )
e.place(x = 520 , y = 250)
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result)+str(num))

b = Button(window, text="1", width= 10, command= lambda:click(1))
b.place(x = 530 , y = 310 )

b = Button(window, text="2", width= 10,command= lambda:click(2))
b.place(x = 620 , y = 310 )

b = Button(window, text="3", width= 10,command= lambda:click(3))
b.place(x = 720 , y = 310 )
def add():
    n1 = e.get()
    global math
    math="add"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window, text="+", width= 10,command= add)
b.place(x = 820 , y = 310 )

b = Button(window, text="4", width= 10,command= lambda:click(4))
b.place(x = 530 , y = 350 )

b = Button(window, text="5", width= 10,command= lambda:click(5))
b.place(x = 620 , y = 350)

b = Button(window, text="6", width= 10,command= lambda:click(6))
b.place(x = 720 , y = 350)
def subtract():
    n1 = e.get()
    global math
    math="subtract"
    global i
    i = int(n1)
    e.delete(0,END)


b = Button(window, text="-", width= 10,command= subtract)
b.place(x = 820 , y = 350 )

def percentage():
    n1 = e.get()
    global math
    math="percentage"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window, text="%", width= 10,command= percentage)
b.place(x = 920 , y = 350 )


b = Button(window, text="7", width= 10,command= lambda:click(7))
b.place(x = 530 , y = 390)

b = Button(window, text="8", width= 10,command= lambda:click(8))
b.place(x = 620 , y = 390)

b = Button(window, text="9", width= 10,command= lambda:click(9))
b.place(x = 720 , y = 390)
def multiplication():
    n1 = e.get()
    global math
    math="multiplication"
    global i
    i = int(n1)
    e.delete(0,END)


b = Button(window, text="*", width= 10,command= multiplication)
b.place(x = 820 , y = 390)

def clear_button():
    e.delete(0, END)

b = Button(window, text="X", width= 10,command= clear_button)
b.place(x = 920 , y = 390 )


b = Button(window, text="00", width= 10,command= lambda:click(00))
b.place(x = 530 , y = 430 )

b = Button(window, text="0", width= 10,command= lambda:click(0))
b.place(x = 620 , y = 430)
def divide():
    n1 = e.get()
    global math
    math="divide"
    global i
    i = int(n1)
    e.delete(0,END)


b = Button(window, text="/", width= 10,command= divide)
b.place(x = 720 , y = 430 )

def equal():
    n2 = e.get()
    e.delete(0, END)
    try:
        if math == "add":
            e.insert(0, i + float(n2))
        elif math == "subtract":
            e.insert(0, i - float(n2))
        elif math == "multiplication":
            e.insert(0, i * float(n2))
        elif math == "divide":
            if float(n2) == 0:
                e.insert(0, "Error")   # divide by zero handle
            else:
                e.insert(0, i / float(n2))
        elif math == "percentage":
            e.insert(0, (i * float(n2)) / 100)
        elif math == "power":
            e.insert(0, i ** float(n2))
    except:
        e.insert(0, "Error")



b = Button(window, text="=", width= 10,command= equal)
b.place(x = 820 , y = 430 )

def power():
    n1 = e.get()
    global math
    math="power"
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window, text="^", width= 10,command= power)
b.place(x = 920 , y = 430 )


window.mainloop()