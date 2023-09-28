class Cat():
    def __init__(self, breed, color, age):
        self._breed = breed
        self._color = color
        self._age = age
        #self._purr()
        #self.meow()

    def meow(self):
        print('Мяу !')

    def _purr(self):
        print('Мрррр')
       # return '9'
    @property
    def breed(self):
        return self._breed
    @property
    def color(self):
        return self._color
    @property
    def age(self):
        return self._age
    #@age.setter
    def ageSR(self, new_age):
        if new_age > self._age:
            self._age = new_age
        return self._age
d = Cat(12,4,6)
f = Cat._purr
print(d.ageSR(2))
print(f)
#c = d.age
#print(d.ageSR())