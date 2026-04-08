"""Method overloading (Python way)

Python does not support traditional overloading, but we simulate it.
"""
class Math:

    def add(self,a,b,c=0):
        print(a+b+c)

m = Math()

m.add(2,3)
m.add(2,3,4)