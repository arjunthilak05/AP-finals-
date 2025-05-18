# Polymorphism Example - Same method name behaves differently in each class

# Base class
class Instrument:
    def play(self):
        print("Playing some instrument")

# Derived class
class Guitar(Instrument):
    def play(self):
        print("Strumming guitar strings")

# Derived class
class Piano(Instrument):
    def play(self):
        print("Pressing piano keys")

# List of instruments
instruments = [Guitar(), Piano()]

# Loop through instruments and call play method
# Each class has its own version of 'play'
for ins in instruments:
    ins.play()

'''
Output:
Strumming guitar strings
Pressing piano keys
'''
