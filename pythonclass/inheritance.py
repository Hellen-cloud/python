#parent class
class Dad:
    def __init__(self, color,hobby):
        self.color = color
        self.hobby = hobby

class Mum:
    def __init__(self, color, hobby):
        self.color = color
        self.hobby = hobby
#child class
class Boy(Dad):
    def boyinherit(self):
        print(f"Boy inherits {self.hobby} and the {self.color}")

#instance
myobj=Boy("African descent","Watching football")
myobj.boyinherit()

#another child class
class Girl(Mum):
    def girlinherit(self):
        print(f"Girl inherits {self.hobby} and the {self.color}")

#instance
inhrt=Girl("Indian descent","Swimming ")
inhrt.girlinherit()


