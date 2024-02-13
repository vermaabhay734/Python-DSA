class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie1 = Cookie('blue')
cookie2 = Cookie('pink')

print('Color of cookie1 is : ', cookie1.color)
print('Color of cookie2 is : ', cookie2.color)