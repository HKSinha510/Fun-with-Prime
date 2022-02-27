from turtle import bgcolor, forward, hideturtle, left, speed, getscreen, screensize, title
from tkinter import *
from PIL import Image, EpsImagePlugin

def init():
    bgcolor()
    title("Prime Spiral")
    screensize(2000, 1500)
    hideturtle()
    speed(0)

def saveFile(screen) -> None:
    screen.getcanvas().postscript(file="prime_spiral.eps")
    EpsImagePlugin.gs_windows_binary = r"C:\Program Files\gs\gs9.55.0\bin\gswin64c.exe"
    im = Image.open("prime_spiral.eps")
    fig = im.convert('RGB')
    image_png= 'prime.png'
    fig.save(image_png, lossless = True)

def findingPrimeNumber():
    prime_numbers = []

    for number in range(900):
        if number>1:
            for i in range(2,number):
                if (number%i)==0:
                    break
            else:
                prime_numbers.append(number)

    return prime_numbers

def draw():
    init()
    for prime_number in findingPrimeNumber():
        forward(prime_number)
        left(90)

    return getscreen()

canvas = draw()
saveFile(canvas)