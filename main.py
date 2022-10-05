import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("1900x1000")

# Frame for the title bar across the top
titleFrame = Frame(win, width=1600, height=100)
titleFrame.pack(side='top', fill='x')
titleFrame.pack_propagate(False)

# Frame for the order going down the right side
orderFrame = Frame(win, width=300, height=600)
orderFrame.pack(side='right', anchor=N)
orderFrame.pack_propagate(False)

# Frame for the menu image on top of the order frame
orderTitleFrame = Frame(orderFrame, width=300, height=100)
orderTitleFrame.pack(side='top')
orderTitleFrame.pack_propagate(False)

# Frame for the menu filling the space under the title and left of the menu
menuFrame = Frame(win, width=1600, height=900)
menuFrame.pack(fill='both')
menuFrame.pack_propagate(False)

# adds labels for the title
mario = tk.PhotoImage(file="marios.png")
marioLabel = Label(titleFrame, image=mario)
marioLabel.pack(side="left", ipadx=20)
orderLabel = Label(titleFrame, text="Order", font=("Lora", 50), borderwidth=5, relief="sunken")
orderLabel.pack(side='left', padx=20)
contactLabel = Label(titleFrame, text="Contact", font=("Lora", 50), borderwidth=5, relief="raised")
contactLabel.pack(side='left', padx=20)
locationLabel = Label(titleFrame, text="Location", font=("Lora", 50), borderwidth=5, relief="raised")
locationLabel.pack(side='left', padx=20)

# Creates a section for the drinks
drinksFrame = Frame(menuFrame, width=1600, height=260)
drinksFrame.pack(side='top')
drinksFrame.pack_propagate(False)
drinksLabel = Label(drinksFrame, text="Drinks", font=("Lora", 25), bg="grey", anchor=W)
drinksLabel.pack(padx=20, pady=20, fill="x")

# frame to hold redwine widgets
redwineFrame = Frame(drinksFrame, width=300, height=260)
redwineFrame.pack(side='left')
redwineFrame.pack_propagate(False)
redwine = tk.PhotoImage(file="redwine.png")
redwine = redwine.subsample(10, 10)
redwineLabel = Label(redwineFrame, image=redwine)
redwineLabel.pack(side="left")
drink1label = Label(redwineFrame, text="Red Wine, $20", font=("Lora", 20))
drink1label.pack(anchor=NW)
redwinevar = StringVar()
redwinelabel2 = Message(redwineFrame, textvariable=redwinevar, relief=RAISED)
redwinevar.set("A fruity and bold red wine.")
redwinelabel2.pack(anchor=NW)
redwineSpinbox = Spinbox(redwineFrame, from_=0, to=10)
redwineSpinbox.pack(anchor=NW)
redwineText = Text(redwineFrame, height=1, width=20)
redwineText.pack(anchor=NW)

# frame to hold white wine widgets
whitewineFrame = Frame(drinksFrame, width=300, height=260)
whitewineFrame.pack(side='left')
whitewineFrame.pack_propagate(False)
whitewine = tk.PhotoImage(file="whitewine.png")
whitewine = whitewine.subsample(25, 25)
whitewineLabel = Label(whitewineFrame, image=whitewine)
whitewineLabel.pack(side="left")
drink2label = Label(whitewineFrame, text="White Wine, $15", font=("Lora", 20))
drink2label.pack(anchor=NW)
whitewinevar = StringVar()
whitewinelabel2 = Message(whitewineFrame, textvariable=whitewinevar, relief=RAISED)
whitewinevar.set("A crisp and refreshing white wine.")
whitewinelabel2.pack(anchor=NW)
whitewineSpinbox = Spinbox(whitewineFrame, from_=0, to=10)
whitewineSpinbox.pack(anchor=NW)
whitewineText = Text(whitewineFrame, height=1, width=20)
whitewineText.pack(anchor=NW)

# frame to hold soda widgets
sodaFrame = Frame(drinksFrame, width=300, height=260)
sodaFrame.pack(side='left')
sodaFrame.pack_propagate(False)
soda = tk.PhotoImage(file="soda.png")
soda = soda.subsample(4, 4)
sodaLabel = Label(sodaFrame, image=soda)
sodaLabel.pack(side="left")
drink3label = Label(sodaFrame, text="Soda, $5", font=("Lora", 20))
drink3label.pack(anchor=NW)
sodavar = StringVar()
sodalabel2 = Message(sodaFrame, textvariable=sodavar, relief=RAISED)
sodavar.set("A delicious cola soda.")
sodalabel2.pack(anchor=NW)
sodaSpinbox = Spinbox(sodaFrame, from_=0, to=10)
sodaSpinbox.pack(anchor=NW)
sodaText = Text(sodaFrame, height=1, width=20)
sodaText.pack(anchor=NW)

appFrame = Frame(menuFrame, width=1600, height=260)
appFrame.pack(side='top')
appFrame.pack_propagate(False)
appLabel = Label(appFrame, text="Appetizers", font=("Lora", 25), bg="grey", anchor=W)
appLabel.pack(padx=20, pady=20, fill="x")

calamariFrame = Frame(appFrame, width=350, height=260)
calamariFrame.pack(side='left')
calamariFrame.pack_propagate(False)
calamari = tk.PhotoImage(file="calamari.png")
calamari = calamari.subsample(5, 5)
calamariLabel = Label(calamariFrame, image=calamari)
calamariLabel.pack(side="left")
app1label = Label(calamariFrame, text="Calamari, $13", font=("Lora", 20))
app1label.pack(anchor=NW)
calamarivar = StringVar()
calamarilabel2 = Message(calamariFrame, textvariable=calamarivar, relief=RAISED)
calamarivar.set("Crispy fried squid with a marinara sauce.")
calamarilabel2.pack(anchor=NW)
calamariSpinbox = Spinbox(calamariFrame, from_=0, to=10)
calamariSpinbox.pack(anchor=NW)
calamariText = Text(calamariFrame, height=1, width=20)
calamariText.pack(anchor=NW)

garlicknotsFrame = Frame(appFrame, width=350, height=260)
garlicknotsFrame.pack(side='left')
garlicknotsFrame.pack_propagate(False)
garlicknots = tk.PhotoImage(file="garlicknots.png")
garlicknots = garlicknots.subsample(4, 4)
garlicknotsLabel = Label(garlicknotsFrame, image=garlicknots)
garlicknotsLabel.pack(side="left")
app2label = Label(garlicknotsFrame, text="Garlic Knots, $9", font=("Lora", 20))
app2label.pack(anchor=NW)
garlicknotsvar = StringVar()
garlicknotslabel2 = Message(garlicknotsFrame, textvariable=garlicknotsvar, relief=RAISED)
garlicknotsvar.set("Flakey garlicky bread, you will need a breath mint after this one.")
garlicknotslabel2.pack(anchor=NW)
garlicknotsSpinbox = Spinbox(garlicknotsFrame, from_=0, to=10)
garlicknotsSpinbox.pack(anchor=NW)
garlicknotsText = Text(garlicknotsFrame, height=1, width=20)
garlicknotsText.pack(anchor=NW)

saladFrame = Frame(appFrame, width=350, height=260)
saladFrame.pack(side='left')
saladFrame.pack_propagate(False)
salad = tk.PhotoImage(file="salad.png")
salad = salad.subsample(6, 6)
saladLabel = Label(saladFrame, image=salad)
saladLabel.pack(side="left")
app3label = Label(saladFrame, text="Cesar Salad, $7", font=("Lora", 20))
app3label.pack(anchor=NW)
saladvar = StringVar()
saladLabel2 = Message(saladFrame, textvariable=saladvar, relief=RAISED)
saladvar.set("A light and refreshing salad to start a heavy meal.")
saladLabel2.pack(anchor=NW)
saladSpinbox = Spinbox(saladFrame, from_=0, to=10)
saladSpinbox.pack(anchor=NW)
saladText = Text(saladFrame, height=1, width=20)
saladText.pack(anchor=NW)

foodFrame = Frame(menuFrame, width=1600, height=260)
foodFrame.pack(side='top')
foodFrame.pack_propagate(False)
foodLabel = Label(foodFrame, text="Mains", font=("Lora", 25), bg="grey", anchor=W)
foodLabel.pack(padx=20, pady=20, fill="x")

pizzaFrame = Frame(foodFrame, width=350, height=200)
pizzaFrame.pack(side='left')
pizzaFrame.pack_propagate(False)
pizza = tk.PhotoImage(file="pizza.png")
pizza = pizza.subsample(5, 5)
pizzaLabel = Label(pizzaFrame, image=pizza)
pizzaLabel.pack(side="left")
main1label = Label(pizzaFrame, text="Pizza, $23", font=("Lora", 20))
main1label.pack(anchor=NW)
pizzavar = StringVar()
pizzaLabel2 = Message(pizzaFrame, textvariable=pizzavar, relief=RAISED)
pizzavar.set("Fresh stone oven pizza, add your toppings in the text below.")
pizzaLabel2.pack(anchor=NW)
pizzaSpinbox = Spinbox(pizzaFrame, from_=0, to=10)
pizzaSpinbox.pack(anchor=NW)
pizzaText = Text(pizzaFrame, height=1, width=20)
pizzaText.pack(anchor=NW)

pastaFrame = Frame(foodFrame, width=350, height=200)
pastaFrame.pack(side='left')
pastaFrame.pack_propagate(False)
pasta = tk.PhotoImage(file="pasta.png")
pasta = pasta.subsample(5, 5)
pastaLabel = Label(pastaFrame, image=pasta)
pastaLabel.pack(side="left")
main2label = Label(pastaFrame, text="Pasta, $17", font=("Lora", 20))
main2label.pack(anchor=NW)
pastavar = StringVar()
pastaLabel2 = Message(pastaFrame, textvariable=pastavar, relief=RAISED)
pastavar.set("Fresh made pasta in a delicious tomato sauce, with a moist meatball.")
pastaLabel2.pack(anchor=NW)
pastaSpinbox = Spinbox(pastaFrame, from_=0, to=10)
pastaSpinbox.pack(anchor=NW)
pastaText = Text(pastaFrame, height=1, width=20)
pastaText.pack(anchor=NW)

lasFrame = Frame(foodFrame, width=350, height=200)
lasFrame.pack(side='left')
lasFrame.pack_propagate(False)
las = tk.PhotoImage(file="lasagna.png")
las = las.subsample(5, 5)
lasLabel = Label(lasFrame, image=las)
lasLabel.pack(side="left")
main3label = Label(lasFrame, text="Lasagna, $19", font=("Lora", 20))
main3label.pack(anchor=NW)
lasvar = StringVar()
lasLabel2 = Message(lasFrame, textvariable=lasvar, relief=RAISED)
lasvar.set("A filling slice of layered sheets of pasta, meat, and cheese")
lasLabel2.pack(anchor=NW)
lasSpinbox = Spinbox(lasFrame, from_=0, to=10)
lasSpinbox.pack(anchor=NW)
lasText = Text(lasFrame, height=1, width=20)
lasText.pack(anchor=NW)

# adds image for the menu section
menu = tk.PhotoImage(file="Menu.png")
menuLabel = Label(orderTitleFrame, image=menu)
menuLabel.pack(side='top')

total = IntVar()
totalString = StringVar(value="Total: $0")
drink1 = IntVar()
drink2 = IntVar()
drink3 = IntVar()
app1 = IntVar()
app2 = IntVar()
app3 = IntVar()
main1 = IntVar()
main2 = IntVar()
main3 = IntVar()


def orderTotal():
    drink1.set(redwineSpinbox.get())
    drink2.set(whitewineSpinbox.get())
    drink3.set(sodaSpinbox.get())
    app1.set(calamariSpinbox.get())
    app2.set(garlicknotsSpinbox.get())
    app3.set(saladSpinbox.get())
    main1.set(pizzaSpinbox.get())
    main2.set(pastaSpinbox.get())
    main3.set(lasSpinbox.get())
    total.set((drink1.get() * 20) + (drink2.get() * 15) + (drink3.get() * 5)
              + (app1.get() * 13) + (app2.get() * 9) + (app3.get() * 7)
              + (main1.get() * 23) + (main2.get() * 17) + (main3.get() * 19))
    totalString.set("Total: $" + str(total.get()))


completeOrderStr = StringVar()


def completeOrder():
    i = int
    if int(redwineSpinbox.get()) != 0:
        i = int(redwineSpinbox.get())
        redwineTotal = i * 20
        redwine = ("Redwine x" + str(i) + " $" + str(redwineTotal) + "\n")
    else:
        redwine = ("")

    if int(whitewineSpinbox.get()) != 0:
        i = int(whitewineSpinbox.get())
        whitewineTotal = i * 15
        whitewine = ("Whitewine x" + str(i) + " $" + str(whitewineTotal) + "\n")
    else:
        whitewine = ("")

    if int(sodaSpinbox.get()) != 0:
        i = int(sodaSpinbox.get())
        sodaTotal = i * 5
        soda = ("Soda x" + str(i) + " $" + str(sodaTotal) + "\n")
    else:
        soda = ("")

    if int(calamariSpinbox.get()) != 0:
        i = int(calamariSpinbox.get())
        calamariTotal = i * 13
        calamari = ("Calamari x" + str(i) + " $" + str(calamariTotal) + "\n")
    else:
        calamari = ("")

    if int(garlicknotsSpinbox.get()) != 0:
        i = int(garlicknotsSpinbox.get())
        garlicknotsTotal = i * 9
        garlicknots = ("Garlic Knots x" + str(i) + " $" + str(garlicknotsTotal) + "\n")
    else:
        garlicknots = ("")

    if int(saladSpinbox.get()) != 0:
        i = int(saladSpinbox.get())
        saladTotal = i * 7
        salad = ("Salad x" + str(i) + " $" + str(saladTotal) + "\n")
    else:
        salad = ("")

    if int(pizzaSpinbox.get()) != 0:
        i = int(pizzaSpinbox.get())
        pizzaTotal = i * 23
        pizza = ("Pizza x" + str(i) + " $" + str(pizzaTotal) + "\n")
    else:
        pizza = ("")

    if int(pastaSpinbox.get()) != 0:
        i = int(pastaSpinbox.get())
        pastaTotal = i * 17
        pasta = ("Pasta x" + str(i) + " $" + str(pastaTotal) + "\n")
    else:
        pasta = ("")

    if int(lasSpinbox.get()) != 0:
        i = int(lasSpinbox.get())
        lasTotal = i * 19
        las = ("Lasagna x" + str(i) + " $" + str(lasTotal) + "\n")
    else:
        las = ("")
    completeOrderStr.set(redwine + whitewine + soda + calamari + garlicknots + salad + pizza + pasta + las)


completeOrderLabel = Label(orderFrame, font=("Lora", 20), textvariable=completeOrderStr)
totalLabel = Label(orderFrame, font=("Lora", 20), textvariable=totalString)
completeOrderButton = Button(orderFrame, text='Complete Order', font=("Lora", 15), bg="green",
                             command=lambda: [orderTotal(), completeOrder()], height=3, width=20)
submitButton = Button()
completeOrderButton.pack(side="bottom")
totalLabel.pack(anchor=SE, side="bottom")
completeOrderLabel.pack(side="top")

win.title("Menu")
win.mainloop()
