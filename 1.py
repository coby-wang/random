#! -*- encoding=utf-8 -*-
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("{} is eating.".format(self.name))
