import grid as gr
from tkinter import Tk, Canvas
COLORS = ["khaki2", "ghost white", "green3", "gray26"]
pixel = 10

def fill(matrice, canvas):
    n=len(matrice)
    for line in range(n):
        for col in range(n):
            fill_cell(canvas, matrice, line, col)

def fill_cell(canvas: Canvas, matrice, line, col) :
    x1, y1 = col * pixel, line * pixel
    x2, y2 = (col + 1) * pixel, (line + 1) * pixel
    case = matrice[line][col]
    color = COLORS[case]
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

