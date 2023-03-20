import turtle as t
import random
import colorgram

colors = colorgram.extract("images.jpg", 20)
# print(colors)
rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)
print(rgb_color)

tim = t.Turtle()
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
game_is_on = True
count = 0


def draw():
    for i in range(10):
        t.colormode(255)
        tim.pendown()
        tim.hideturtle()
        tim.dot(20, random.choice(rgb_color))
        tim.penup()
        tim.forward(50)


def movement():

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


while game_is_on:
    count += 1
    draw()
    movement()
    if count == 10:
        game_is_on = False

# def random_colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#

# my_turtle = t.Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("red")
# t.colormode(255)
# my_turtle.speed("fast")
# for i in range(int(360/10)):
#     my_turtle.color(random_colors())
#     current_heading = my_turtle.heading()
#     my_turtle.circle(100)
#     my_turtle.setheading(current_heading + 10)
#
# # # colors = ["bisque3", "blue", "cyan", "brown", "coral", "DeepPink", "green", "HotPink", "gold"]
# # direction = [0, 90, 180, 270]
# #
# #
# # def random_colors():
# #     r = random.randint(0, 255)
# #     g = random.randint(0, 255)
# #     b = random.randint(0, 255)
# #     random_color = (r, g, b)
# #     return random_color
# #
# #
# # for i in range(100):
# #     my_turtle.speed("fast")
# #     my_turtle.color(random_colors())
# #     my_turtle.pensize(10)
# #     my_turtle.forward(30)
# #     my_turtle.setheading(random.choice(direction))
#
# # for i in range(5):
# #     my_turtle.forward(100)
# #     my_turtle.left(72)
#
# #
# # def shapes(number_of_sides):
# #     der = 360 / number_of_sides
# #     my_turtle.color(random.choice(colors))
# #     for _ in range(number_of_sides):
# #         my_turtle.forward(100)
# #         my_turtle.right(der)
# #
# #
# # for i in range(3, 10):
# #     shapes(i)
#

screen = t.Screen()
screen.exitonclick()
