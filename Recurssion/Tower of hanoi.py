# 7. Tower of Hanoi
# Move n disks from source to destination using auxiliary peg
# Recursive step:
#   Move n-1 disks from source to auxiliary
#   Move last disk from source to destination
#   Move n-1 disks from auxiliary to destination

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Example: tower_of_hanoi(3, 'A', 'B', 'C')
# Output shows moves to transfer 3 disks from A to C using B as auxiliary
