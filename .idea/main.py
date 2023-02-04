import random
class Stud:
    def __init__(self, name):
        self.name = name
        self.hun = 50
        self.glad = 10
        self.progres = 0.5
        self.mon = 100
        self.alive = True
    def study(self):
        print("time to study")
        self.hun -= 3
        self.glad -= 3
        self.progres += 0.5
        self.mon -= 1
    def sleep(self):
        print("time to sleep")
        self.glad += 3
        self.progres += 0.15
    def chill(self):
        self.glad += 5
        self.progres -= 0.1
        self.hun += 2
        self.mon -= 10
    def work(self):
        self.glad-= 1
        self.progres -= 0.1
        self.hun += 1
        self.mon += 10

    def is_alive(self):
        if self.progres < 0.5:
           self.alive = False
           print("cast out")
        elif self.glad <= 0:
            print("ahhh i have depresion")
        elif self.mon <= 0:
            print("ahhh i don't have money")
            self.alive = False
        elif self.progres > 5:
            print("passed")
            self.alive = False
    def day(self):
            print(f"progres", {self.progres})
            print(f"gladnes", {self.glad})
            print(f"money", {self.mon})
            print(f"hungry", {self.hun})
            if self.mon <= 80:
                print('sssssssssssssssssssssssssss')
                self.work()
            if self.progres <= 3:
                print('ychi ypoki debil')
                self.study()
                self.mon += 1
            if self.glad <=10:
                self.chill()
    def live(self, day):
            day = "Day"+str(day)+"of"+"live"
            print(f"{day:=^50}")
            cube = random.randint(1,3)
            if cube == 1:
                self.study()
            if cube == 2:
                self.sleep()
            if cube == 3:
                self.chill()

            self.day()
            self.is_alive()


nick = Stud(name = "Nick")
for day in range(365):
    if nick.alive == False:
        print(nick.live(day))
        break
    nick.live(day)



