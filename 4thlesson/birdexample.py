class Bird():
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("wanna eat")
            self.hungry = False
        else:
            print("No, I am full")


class SingBird(Bird):
    def __init__(self):
        super().__init__()
        self.song = "God is girl"

    def sing(self):
        print(self.song)


sib = SingBird()
sib.sing()

sib.eat()
sib.eat()

