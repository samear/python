#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1():
    def f2():
        print('this is f2')
    return f2

x = f1()
x()
