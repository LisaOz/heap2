'''
This script demonstrates the creation of a Heap, insertion of elements into it, and extraction of elements from it.
'''

class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    # Function to add the elements to the Heap
    def insert(self, x):
        self.values.append(x) # Append the new element to the Heap
        self.size += 1 # Increase the size of the Heap
        self.sift_up(self.size - 1) # Call sift_up() on the index of the next element

    # Function to move the element up the Heap if it is smaller than the parent
    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1)//2]:
            self.values[i], self.values[(i - 1)//2] = self.values[(i - 1)//2], self.values[i]
            i = (i - 1) // 2  # Move up the parent index

    # Function to extract the elements from the Heap
    def extract_min(self):
        tmp = self.values[0] # Move the root element of the Heap to the tmp variable
        self.values[0] = self.values[-1]  # Move the last element of the Heap to the root
        self.values.pop() # Extract the last element from the list
        self.size -= 1 # Decrease the size of the Heap
        if not self.size:
            return None
        self.sift_down(0)
        return tmp

    # Function to move the element down the Heap
    def sift_down(self, i):
        while  2 * i + 1 < self.size: # Till there is at least one child
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j: # If the children elements are not smaller than parent nodes
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j # Update i to continue shifting down

if __name__ == "__main__":
    min_heap = Heap()  # Initialise the Heap

    # Insert elements into the Heap
    elements = [4, 10, 8, 7, 12, 1, 3]
    for elmt in elements:
        min_heap.insert(elmt)
        print(f"Inserted element {elmt}: {min_heap.values}")

    # Extract the mininum element repeatedly
    extracted_elements = []
    while min_heap.size > 0:
        min_elmt = min_heap.extract_min()
        extracted_elements.append(min_elmt)
        print(f"Extracted minimum  element: {min_elmt}, Remaining Heap: {min_heap.values}")

    print("Extracted elements:", extracted_elements)