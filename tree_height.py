
import sys
import threading
import numpy


def compute_height(n, parents):
    # Create an array to store the heights of all nodes, initialized to 0
    heights = [0] * n

    # Traverse the tree bottom-up, updating the height of each node as we go
    for i in range(n):
        if heights[i] == 0:
            height = 0
            node = i
            while node != -1:
                if heights[node] != 0:
                    height += heights[node]
                    break
                height += 1
                node = parents[node]
            heights[i] = height

    # Return the maximum height of any node in the tree
    return max(heights)


def main():
    # Get input from the user
    input_type = input("Enter input type (F for file, K for keyboard): ")
    while input_type not in ["F", "f", "K", "k"]:
        input_type = input("Invalid input. Please enter F or K: ")

    # Get the file name or input values
    if input_type in ["F", "f"]:
        file_name = input("Enter file name (without the letter 'a'): ")
        while "a" in file_name:
            file_name = input("Invalid file name. Please enter again: ")
        try:
            with open("folder/" + file_name, "r") as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            sys.exit()
    else:
        # Input number of nodes
        n = int(input("Enter number of nodes: "))

        # Input parent of each node
        parents = list(map(int, input("Enter parents of nodes (space-separated): ").split()))

    # Call the compute_height function to get the height of the tree
    height = compute_height(n, parents)

    # Output the height of the tree
    print("Height of tree:", height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
