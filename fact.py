from tkinter import Tk, Button, font
from random import randint


symbols = ['÷', '※', '™', 'π', 'Δ', 'ø', '☠', '©', '×']

pairsAmount = 4
btnMass = []

root = Tk()
root.geometry('500x500')
lastButton = None


def chooseSymbols(mass, amount):
    chosenSymbols = []
    while len(chosenSymbols) < amount:
        currentSymbol = randint(0, len(mass) - 1)
        if mass[currentSymbol] not in chosenSymbols:
            chosenSymbols.append(mass[currentSymbol])
    return chosenSymbols * 2


def clickButton(button, buttonData):
    global lastButton

    if button.cget("text") != '':
        return
    
    button.config(text=buttonData['symbol'])

    if lastButton == None:
        lastButton = {
            'parent': button,
            'data': buttonData
        }
        return

    if lastButton['data']['symbol'] == buttonData['symbol']:
        lastButton['parent'].config(bg='red')

        button.config(bg='red')

        lastButton = None
        
    else:
        root.after(500, lambda b1 = lastButton['parent'], b2 = button: closeCards(b1,b2))
        lastButton = None


def closeCards(b1, b2):
    b1.config(text='')
    b2.config(text='')

def drawButtons(mass):
    currentID = 1

    availableSymbols = mass.copy()

    for i in range(len(mass)):
        randomIndex = randint(0, len(availableSymbols) - 1)
        currentSymbol = availableSymbols.pop(randomIndex)


        btnData = {
            'id': currentID,
            'symbol': currentSymbol
        }
        btnMass.append(btnData)
        btn = Button(root, text='', width=5, height=2)
        btn.config(command=lambda b = btn, data = btnData: clickButton(b, data))
        btn.pack()

        currentID += 1






gameDeck = chooseSymbols(symbols, pairsAmount)

drawButtons(gameDeck)

root.mainloop() # запуск