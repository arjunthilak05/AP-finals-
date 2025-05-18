import random

"""
Dice Class Simulation with Custom Probabilities

This class simulates a dice with any number of faces (>=4).
Each face can have a custom probability distribution.
You can "roll" the dice multiple times, and the class tracks:
- The actual counts of each face appearing in the rolls.
- The predicted counts based on the probability distribution.

Key Concepts Used:
- Classes and Objects (OOP)
- Exception handling for input validation
- Probability distributions and random sampling
- Dictionaries for storing distributions and results
"""

class Dice:
    def __init__(self, num):
        """
        Constructor initializes a dice object with 'num' faces.
        Raises an error if 'num' < 4 or not an integer.
        Initializes uniform probabilities by default.
        """
        try:
            if num < 4 or type(num) != int:
                raise ValueError("Number of faces must be an integer >= 4")
        except ValueError as e:
            print("<class 'Exception'>")
            print("Cannot construct the dice:", e)
        else:
            # Initialize uniform probability distribution for faces
            self.faces = [1/num] * num
            self.distribution = {}  # cumulative probability ranges
            self.actual = {}        # counts from rolling dice
            self.predicted = {}     # expected counts based on probabilities
        finally:
            print(f"Dice created with {num} faces")

    def setProb(self, probabilities):
        """
        Sets the custom probability distribution for the dice faces.
        The input 'probabilities' must be a tuple/list with the same length as faces.
        Also builds cumulative probability ranges for sampling.
        """
        try:
            if len(probabilities) != len(self.faces):
                raise ValueError("Length of probabilities does not match number of faces")
        except ValueError as e:
            print("<class 'Exception'>")
            print("Invalid probability distribution:", e)
        else:
            # Update the probabilities
            for i, prob in enumerate(probabilities):
                self.faces[i] = prob
            
            # Build cumulative probability ranges for each face
            cumulative = 0
            for i, prob in enumerate(self.faces):
                start = cumulative
                cumulative += prob
                self.distribution[i + 1] = [start, cumulative]
        finally:
            print("New probability has been updated")

    def roll(self, rolls):
        """
        Simulates rolling the dice 'rolls' times.
        For each roll, generates a random number and finds which face it maps to.
        Updates the actual counts.
        Also calculates predicted counts based on probabilities.
        Prints actual counts, predicted counts, face probabilities, and cumulative ranges.
        """
        for _ in range(rolls):
            k = random.uniform(0, 1)  # Random number between 0 and 1
            for face, (start, end) in self.distribution.items():
                if start < k <= end:
                    self.actual[face] = self.actual.get(face, 0) + 1
                    break
        
        # Calculate predicted counts
        for i, prob in enumerate(self.faces):
            self.predicted[i + 1] = prob * rolls
        
        # Print results
        print(f"Actual counts after {rolls} rolls: {self.actual}")
        print(f"Predicted counts (expected): {self.predicted}")
        print(f"Face probabilities: {self.faces}")
        print(f"Cumulative distribution ranges: {self.distribution}")


# Example usage:
if __name__ == "__main__":
    d = Dice(4)  # Create a dice with 4 faces
    d.setProb((0.1, 0.2, 0.3, 0.4))  # Set custom probabilities
    d.roll(100)  # Roll the dice 100 times
    d.roll(400)  # Roll the dice another 400 times
