# Helina Asadi           4th practice
# X O Character Recognition , Learning Algorithm : Single-layer Perceptron
# Bipolar Encoding , Threshold Activation Function
# alpha (learning rate) = 1     ,     theta (threshold) = 0.2

import XOdataSet
import numpy as np

# INITIALIZING WEIGHTS & BIAS
weights = [0] * 25
bias = 0
# SETTING LEARNING RATE
alpha = 1
# SETTING THE THRESHOLD
theta = 0.2

# LEARNING ALGORITHM : SINGLE-LAYER PERCEPTRON
def SLperceptron(XOsamples) :
    global weights, bias
    flag = True
    while flag :
        compareweights = weights
        comparebias = bias
        for i in (XOsamples):
            sample = i.get("sample")
            target = i.get("target")
            # Calculating Y NetInput and f(YNI) with threshold
            YNI = np.dot(weights, sample) + bias
            if YNI > theta:
                fYNI = 1
            elif -theta <= YNI <= theta:
                fYNI = 0
            else:
                fYNI = -1  # for YNI less than theta
            # Updating weights ONLY if there is a mismatch
            if fYNI != target:
                for i in range(len(sample)):
                    weights[i] += alpha * sample[i] * target
                bias += alpha * target

        # TERMINATION CONDITION :
        # if there is no change in weights through one whole epoch, then terminate learning
        changeinWeights = False
        for i in range(len(compareweights)):
            if compareweights[i] != weights[i] :
                changeinWeights = True
        if comparebias != bias :
            changeinWeights =  True
        if changeinWeights :
            flag = False

    print("Just Finished Learning !")


# TESTING
def test(matrix) :
    testArray = [element for row in matrix for element in row]  # storing gui matrix values in an array
    YNI = np.dot(testArray, weights) + bias
    if YNI > theta:
        fYNI = 1
    elif -theta <= YNI <= theta:
        fYNI = 0
    else:
        fYNI = -1  # for YNI less than theta
    testResult = fYNI
    if testResult == -1:
        character = "X"
    else:
        character = "O"
    print("Your pattern is : ", character)
    return YNI


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
learnButton = tk.Button(root, text="LEARN!", command=lambda: SLperceptron(XOdataSet.XOsamples))
learnButton.grid(row=5, column=2, pady=10)

# TEST button to test the pattern that user has indicated
testButton = tk.Button(root, text="TEST!", command=lambda: test(matrix))
testButton.grid(row=6, column=2, pady=10)

# to always show the window
root.mainloop()