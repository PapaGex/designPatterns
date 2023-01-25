import sys
from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):

        self.__always_do_this()
        self.do_step_1()
        self.do_step_2()
        self.do_this_or()


    def __always_do_this(self):

        name = sys._getframe().f_code.co_name
        print('{}.{}'.format(self.__class__.__name__, name))

    @abstractmethod
    def do_step_1(self):

        pass

    @abstractmethod
    def do_step_2(self):

        pass


    def do_this_or(self):
        print('You can override me but you dont have too.')


class ConcreteClassA(AbstractClass):

    def do_step_1(self):
        print('Doing step one for ConcreteCLass A ...')

    def do_step_2(self):
        print('Doing step two for ConcreteClass A ...')


class ConcreteClassB(AbstractClass):

    def do_step_1(self):
        print('Doing step one for ConcreteClass B ...')

    def do_step_2(self):
        print('Doing step two for ConcreteClass B ...')

    def do_this_or(self):
        print('Doing my own thing mang ....')


def main():
    print('==========ConcreteClassA==================')

    a = ConcreteClassA()
    a.template_method()


    print('==========ConcreteClassB==================')

    b = ConcreteClassB()
    b.template_method()

if __name__ == "__main__":
    main()