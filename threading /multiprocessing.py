import multiprocessing
import time

# Function to calculate and print squares of numbers
def calc_square(numbers):
    for n in numbers:
        print(f"Square: {n * n}")
        time.sleep(1)  # Simulate time-consuming task

# Function to calculate and print cubes of numbers
def calc_cube(numbers):
    for n in numbers:
        print(f"Cube: {n * n * n}")
        time.sleep(1)  # Simulate time-consuming task

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]  # List of numbers to process

    # Create two separate processes for square and cube calculations
    p1 = multiprocessing.Process(target=calc_square, args=(nums,))
    p2 = multiprocessing.Process(target=calc_cube, args=(nums,))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    # Print after both tasks are finished
    print("Done with multiprocessing")
