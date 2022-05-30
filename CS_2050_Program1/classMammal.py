"""
Title: Assignment 1
Description: This program creates a parent class and child classes to
accomplish a couple different objectives. These objectives were to exhibit
inheritance, polymorphism, use accessors, and override an operator.
"""

class Mammal(object):
    """
    This is the parent class that the two child classes will inherit from
    """
    def __init__(self, Genus, Noise):
        """
        Mammal class constructor initializing needed values
        """
        self.Genus = Genus
        self.Noise = Noise
     
    def __eq__(self,other):
        """ 
        operator override for bear == gorilla
        """
        return(self.Genus == other.Genus)
    
    def getGenus(self):
        """ 
        accessor method for getGenus
        """
        return self.Genus

    def makeNoise(self):
        """ 
        define sound for each animal 
        """
        return self.Noise
    
class Gorilla(Mammal):
    """
    This is a child class of the class Mammal
    """
    def __init__(self):
        """ 
        Gorilla class constructor setting the values 
        for genus and noise 
        """
        self.Genus = 'Gorilla'
        self.Noise = 'grunting'
    def makeNoise(self):
        """
        This method overrides the makeNoise method 
        in the Parent class of Mammal. This method is special 
        to the Elephant class and can only be used by objects
        that are elephants.
        """
        return "Gorilla is " + self.Noise
    
class Bear(Mammal):
    """
    This is a child class of the class Mammal
    """
    def __init__(self):
        """ 
        Bear class constructor setting the values for 
        genus and noise 
        """
        self.Genus = 'Bear'
        self.Noise = 'roaring'
    def makeNoise(self):
        """
        This method overrides the makeNoise method 
        in the Parent class of Mammal. This method is special 
        to the Elephant class and can only be used by objects
        that are elephants.
        """    
        return "Bear is " + self.Noise

def main():
    """ 
    create instances of child classes
    """
    b = Bear()
    g = Gorilla()

    """
    compare two classes with overridden == operator, 
    and call accessor method
    """
    if b == g:
        print(b.getGenus() + " and " + g.getGenus() + " are of the same genus")
    else:
        print(b.getGenus() + " and " + g.getGenus() + " are *not* of the same genus")

    """
    a function to help demonstrate polymorphism
    """
    def listenToMammal(Mammal):
        print(Mammal.makeNoise())

    """
    now call the function to show child class's specific implementations
    """
    listenToMammal(b)
    listenToMammal(g)

if __name__ == '__main__':
    main()