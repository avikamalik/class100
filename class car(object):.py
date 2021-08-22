class car(object):
    def __init__(self,model,color,speed,company):
        self.model=model
        self.color=color
        self.speed=speed
        self.company=company
    def start(self):
        print("car started")

    def accelertate(self,speed2):
        print("car will acccelerate")

car1=car(1,'white',300,'tesla')
car2=car(2,'black',300,'honda')

car2.start()
car2.accelertate(3000)