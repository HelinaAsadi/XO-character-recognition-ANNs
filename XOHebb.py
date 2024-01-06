# Helina Asadi
# X O Character Recognition , Hebbian Learning Algorithm , BiPolar Encoding

import numpy as np
import XOdataSet

# INITIALIZING WEIGHTS & BIAS
weights = [0] * 25
bias = 0


# LEARNING ALGORITHM : HEBB
def hebb(XOsamples) :
    global weights, bias
    # START LEARNING
    # updating weights with XOdata
    for i in(XOsamples) :
        sample = i.get("sample")
        target = i.get("target")
        # updating bias
        bias += target
        # updating weights
        for j in range(len(sample)) :
            weights[j] += sample[j]*target
    print("Just Finished Learning !")


# CALCULTING Y NetInput & TEST RESULT
def test(matrix) :
    testArray = [element for row in matrix for element in row]   # storing gui matrix values in an array
    YNI = 0
    for i in range(len(weights)) :
        YNI += weights[i]*testArray[i]      # YNI = Y NetInput
    YNI += bias
    testResult = sign(YNI)
    if testResult == -1:
        character = "X"
    else:
        character = "O"
    print("Your pattern is : ", character)
    return YNI


# ACTIVATION FUNCTION : HEAVISIDE STEP
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def heavisideSFunction(YNI) :
    return 0 if YNI < 0 else 1

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
learnButton = tk.Button(root, text="LEARN!", command=lambda: hebb(XOdataSet.XOsamples))
learnButton.grid(row=5, column=2, pady=10)

# TEST button to test the pattern that user has indicated
testButton = tk.Button(root, text="TEST!", command=lambda: test(matrix))
testButton.grid(row=6, column=2, pady=10)

# to always show the window
root.mainloop()
