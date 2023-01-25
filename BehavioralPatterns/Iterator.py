def count_to(count):

    numbers_in_nihonjin = ["ichi", "ni", "san", "yon", "go", "ryoko"]

    iterator = zip(range(count), numbers_in_nihonjin)



    for position, number in iterator:

        yield number


for num in count_to(3):
    print("{}".format(num))