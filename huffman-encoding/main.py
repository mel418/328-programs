# Define a Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Function to build the Huffman tree
def build_huffman_tree(freq_table):
    nodes = [Node(char, freq) for char, freq in freq_table.items()]
    
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        nodes.append(merged)
    
    return nodes[0]

# Function to calculate the Huffman encoding length
def huffman_encoding_length(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Create a frequency table of characters in the file
    freq_table = {}
    for char in text:
        if char in freq_table:
            freq_table[char] += 1
        else:
            freq_table[char] = 1
    
    # Build the Huffman tree
    root = build_huffman_tree(freq_table)
    
    # Calculate the length of the Huffman encoding
    length = 0
    stack = [(root, 0)]
    
    while stack:
        node, depth = stack.pop()
        if node.char is not None:
            length += depth * freq_table[node.char]
        if node.left is not None:
            stack.append((node.left, depth + 1))
        if node.right is not None:
            stack.append((node.right, depth + 1))
    
    return length

# Example usage

file_paths = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt","6.txt", "7.txt", "8.txt", "9.txt", "10.txt"]

for file_path in file_paths:
    encoding_length = huffman_encoding_length(file_path)
    print(f'Length of Huffman Encoding ({file_path}) is: {encoding_length} bits')
