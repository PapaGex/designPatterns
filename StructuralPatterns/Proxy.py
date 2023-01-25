import time

class Producer:

    def produce(self):
        print("Producer is hard at work!")

    def meet(self):
        print("Producer has time to meet you!")

class Proxy:

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        print("Artist is checking the producers availability ...")

        if self.occupied == "No":
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()

        else:
            time.sleep(2)
            print("Producer is busy!")

p = Proxy()

p.produce()

p.occupied = 'Yes'

p.produce()