class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width+2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for height in range(0,self.height):
            for width in range(0,self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self,shape):
        return self.get_area()/shape.get_area()//1


class Square(Rectangle):
    def __init__(self,side):
        self.height = side
        self.width = side
        self.side = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self,side):
        self.side = side
        self.width = self.side
        self.height = self.side
    

    def set_height(self,side):
        self.side = side
        self.height = self.side
        self.width = self.side

    def set_side(self,side):
        self.side = side
        self.height = self.side
        self.width = self.side