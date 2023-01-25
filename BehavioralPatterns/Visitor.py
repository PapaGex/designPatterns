class House(object):
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "Work completed by", hvac_specialist)


    def work_on_electricity(self, electrician):
        print(self, "Work completed by", electrician)

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)

HV_Man = HvacSpecialist()

Sparky = Electrician()

Home = House()

Home.accept(HV_Man)

Home.accept(Sparky)