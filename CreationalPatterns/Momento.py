import pickle

class Originator:
    def __init__(self):
        self._state = None

    def create_momento(self):
        return pickle.dumps(vars(self))

    def set_momento(self, momento):
        previous_state = pickle.loads(momento)
        vars(self).clear()
        vars(self).update(previous_state)


def main():

    originator = Originator()

    print(vars(originator))

    momento = originator.create_momento()

    originator._state = True

    print(vars(originator))

    originator.set_momento(momento)

    print(vars(originator))


if __name__ == "__main__":
       main()