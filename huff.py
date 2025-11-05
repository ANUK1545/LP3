# Huffman Encoding using Greedy Algorithm

class Node:
    def __init__(self, char, freq):
        self.char = char      # character
        self.freq = freq      # frequency
        self.left = None      # left child
        self.right = None     # right child

def print_codes(node, code=""):
    # Base case: if node is None
    if node is None:
        return
    
    # If it's a leaf node, print the code
    if node.left is None and node.right is None:
        print(node.char, ":", code)
        return

    # Traverse left as '0' and right as '1'
    print_codes(node.left, code + "0")
    print_codes(node.right, code + "1")

def huffman_encoding(chars, freqs):
    nodes = []

    # Step 1: Create list of nodes
    for i in range(len(chars)):
        nodes.append(Node(chars[i], freqs[i]))

    # Step 2: Repeat until one node remains
    while len(nodes) > 1:
        # Sort nodes by frequency (ascending)
        nodes = sorted(nodes, key=lambda x: x.freq)

        # Pick two smallest nodes
        left = nodes[0]
        right = nodes[1]

        # Create a new merged node
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        # Remove the two smallest and add the new node
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    # Step 3: Print Huffman Codes
    print("Huffman Codes are:")
    print_codes(nodes[0])

# Example
chars = ['A', 'B', 'C', 'D', 'E', 'F']
freqs = [5, 9, 12, 13, 16, 45]

huffman_encoding(chars, freqs)
