# Loli Clicker by @ElopingDev
# Credits TokyoEdTech
import turtle

wn = turtle.Screen()
wn.title("Loli Clicker by @ElopingDev")
wn.bgcolor("#422b40")

wn.register_shape("loli2.gif")

cookie = turtle.Turtle()
cookie.shape("loli2.gif")
cookie.speed(0)
clicks = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 300)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)

wn.mainloop()