#Easy to ask forgiveness than permission since permissions will always make object calls which might take most of our code running
#time.

class Duck:
    def quack(self):
        print('Quack, quack')
    def fly(self):
        print('Flap, Flap')
        
class Person:
    def quack(self):
        print('I am quacking like a duck.')
    def fly(self):
        print('I am flapping my arms like a duck.')
        
def quack_and_fly(thing):
    if isinstance(thing, Duck):
        thing.fly()
        thing.quack()
    else:
        print('This has to be a duck')

def quackAndFly(thing):
    if hasattr(thing, 'quack'):
        if callable(thing.quack):    #we need to ask these two permissions 
            thing.quack()
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
            
#alternative to quackAndFly
def qnf(thing):
    try:
        thing.fly()
        thing.quack()
        thing.bark()
        
    except AttributeError as e:
            print(e)
    
    

print('First')
d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

            
print('\nSecond')            
d = Duck()
quackAndFly(d)

p = Person()
quackAndFly(p)

print('\nThird')
d = Duck()
qnf(d)

p = Person()
qnf(p)

    
    