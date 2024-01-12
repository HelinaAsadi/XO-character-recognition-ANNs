# Helina Asadi           5th practice
# X O Character Recognition , Learning Algorithm : Single-layer, MultiCategory Perceptron
# Bipolar Encoding , Threshold Activation Function
# alpha (learning rate) = 1     ,     theta (threshold) = 0.2

import XOdataSet
import numpy as np

# INITIALIZING WEIGHTS & BIAS
xweights = [0] * 25
oweights = [0] * 25
xbias = 0
obias = 0
# SETTING LEARNING RATE
alpha = 1
# SETTING THE THRESHOLD
theta = 0.2


# LEARNING ALGORITHM : MultiCategory PERCEPTRON
def MCperceptron(XOsamples) :
    global xweights, oweights, xbias, obias
    flag = True
    while flag :
        compareXweights = xweights
        compareOweights = oweights
        compareXbias = xbias
        compareObias = obias
        for i in (XOsamples):
            sample = i.get("sample")
            target = i.get("target")
            if target == -1:
                xtarget = +1
                otarget = -1
            else:
                xtarget = -1
                otarget = +1
            # Calculating Y NetInput and f(YNI) with threshold (for both output units)
            xYNI = np.dot(xweights, sample) + xbias
            # X output unit
            if xYNI > theta:
                xfYNI = 1
            elif -theta <= xYNI <= theta:
                xfYNI = 0
            else:
                xfYNI = -1  # for YNI less than theta
            # O output unit
            oYNI = np.dot(oweights, sample) + obias
            if oYNI > theta:
                ofYNI = 1
            elif -theta <= oYNI <= theta:
                ofYNI = 0
            else:
                ofYNI = -1
            # Updating weights ONLY if there is a mismatch
            # X
            if xfYNI != xtarget:
                for i in range(len(sample)):
                    xweights[i] += alpha * sample[i] * xtarget
                xbias += alpha * xtarget
            # O
            if ofYNI != otarget:
                for i in range(len(sample)):
                    oweights[i] += alpha * sample[i] * otarget
                obias += alpha * otarget

        # TERMINATION CONDITION :
        # if there is no change in weights through one whole epoch, then terminate learning
        changeinWeights = False
        for i in range(len(compareXweights)):
            if compareXweights[i] != xweights[i] :
                changeinWeights = True
        if compareXbias != xbias :
            changeinWeights =  True
        for i in range(len(compareOweights)):
            if compareOweights[i] != oweights[i] :
                changeinWeights = True
        if compareObias != obias :
            changeinWeights =  True

        if changeinWeights :
            flag = False

    print("Just Finished Learning !")


# TESTING
def test(matrix) :
    testArray = [element for row in matrix for element in row]  # storing gui matrix values in an array
    # X
    xYNI = np.dot(testArray, xweights) + xbias
    if xYNI > theta:
        xfYNI = 1
    elif -theta <= xYNI <= theta:
        xfYNI = 0
    else:
        xfYNI = -1
    # O
    oYNI = np.dot(testArray, oweights) + obias
    if oYNI > theta:
        ofYNI = 1
    elif -theta <= oYNI <= theta:
        ofYNI = 0
    else:
        ofYNI = -1
    # combining results to get one
    if xfYNI == +1:
        testResult = -1
    if ofYNI == +1:
        testResult = +1
    # assigning result to a character
    if testResult == -1:
        character = "X"
    else:
        character = "O"
    print("Your pattern is : ", character)



# ------------------------------------------------------------------------------

# GUI

import tkinter as tk

def toggleValue(row, col):   # to toggle the value of matrix element when the corresponding button is clicked
    matrix[row][col] *= -1
    updateButtons()

def updateButtons():
    # to change text
    for i in range(5):
        for j in range(5):
            value = matrix[i][j]
            buttons[i][j].config(text=str(value))
            # to change color
            color = "lightpink" if value == 1 else "SystemButtonFace"
            buttons[i][j].config(bg=color)

# creating the corresponding matrix for the graphic pattern
matrix = [[-1] * 5 for _ in range(5)]

# creating a window
root = tk.Tk()
root.title("X or O ???")

# creating 25 buttons corresponding the matrix
buttons = []
for i in range(5):
    row_buttons = []
    for j in range(5):
        btn = tk.Button(root, text=str(matrix[i][j]), width=5, height=2,
                        command=lambda row=i, col=j: toggleValue(row, col))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row_buttons.append(btn)

    buttons.append(row_buttons)

# LEARN button to call the learning function
learnButton = tk.Button(root, text="LEARN!", command=lambda: MCperceptron(XOdataSet.XOsamples))
learnButton.grid(row=5, column=2, pady=10)

# TEST button to test the pattern that user has indicated
testButton = tk.Button(root, text="TEST!", command=lambda: test(matrix))
testButton.grid(row=6, column=2, pady=10)

# to always show the window
root.mainloop()