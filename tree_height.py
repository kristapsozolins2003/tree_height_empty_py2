
import sys
import threading
import numpy


def compute_height(n, parents):
    heights = [0] * n

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

    return max(heights)


def main():
    input_type = input("Enter input type (F for file, K for keyboard): ")
    while input_type not in ["F", "f", "K", "k"]:
        input_type = input("Invalid input. Please enter F or K: ")
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
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents of nodes (space-separated): ").split()))
    height = compute_height(n, parents)

    print("Height of tree:", height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
