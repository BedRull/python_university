from Programming_Labs.starter_pack import descriptors as desc
from Programming_Labs.starter_pack import generators as gen
from Programming_Labs.starter_pack import iterators as it
from Programming_Labs.starter_pack import decorators as dec

from time import sleep


# generators
# genCountDown = gen.countdown(200)
# print(*genCountDown, sep='\n')


# descriptors
# temp = desc.Temperature()
# temp.celcius = 2200
# nex = temp.fahrenheit
# del temp.celcius


# iterators
# CD_rev = reversed(it.countdown(200))
# for i in CD_rev:
#     print(i)


@dec.decTime()
def oneFunction():
    it_countdown = it.countdown(200000)
    for i in it_countdown:
        x = i**4


oneFunction(True)
