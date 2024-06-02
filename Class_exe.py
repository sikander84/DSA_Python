class Cookie:
    def __init__(self, color):
        self.color = color

    def  get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color    



cookie_one = Cookie("Green")
cookie_two = Cookie("blue")
print("The color if the cookie one is ",cookie_one.get_color())
print("The color if the cookie one is ",cookie_two.get_color())

cookie_two.set_color("Yellow")

print("Now, The color if the cookie one is ",cookie_one.get_color())
print("Now, The color if the cookie two is ",cookie_two.get_color())
