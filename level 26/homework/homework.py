from turtle import*
def triangle():
    color("red")
    begin_fill()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    end_fill()
    
    left(30)
    penup()
    forward(100)
    pendown()
    left(90)
    for i in range(120):
        triangle()
    exitonclick()
    


def hello_world():
    print("hello_world")
hello_world()

def even_or_odd(num):
    if num % 2 == 0:
        print("არ არის კენტი")
    else: 
        print("კი არის კენტი")


def function_name():
    for i in range(120):
        print("******")
        print("******")
        print("******")

        print("      *")
        print("     ***")
        print("   *******")
        print(" ***********")
        print("      * ")
        print("      * ")

        print("*******")
        print(" ******")
        print("  ********")
        print("   ********")
function_name()


