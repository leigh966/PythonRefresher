from msilib import sequence


def basicDemo():
    add = lambda x, y: x + y
    print("3 + 4 =",add(3,4))
basicDemo()

def mapExample():
    sequence = [1,3,5,9]
    doubled = list(map(lambda x: x*2, sequence))
    print(f"{sequence}*2 = {doubled}")
mapExample()