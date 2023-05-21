import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data):
    frequency_table = defaultdict(int)
    for char in data:
        frequency_table[char] += 1
    return frequency_table

def build_huffman_tree(frequency_table):
    heap = []
    for char, freq in frequency_table.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        parent_node = HuffmanNode(None, left_node.freq + right_node.freq)
        parent_node.left = left_node
        parent_node.right = right_node
        heapq.heappush(heap, parent_node)

    return heap[0]

def build_encoding_table(root):
    encoding_table = {}

    def traverse(node, code):
        if node.char:
            encoding_table[node.char] = code
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(root, "")
    return encoding_table

def huffman_encode(data):
    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)
    encoded_data = "".join(encoding_table[char] for char in data)

    return encoded_data, encoding_table

# Example usage:
data = "Hello, World! Anmol is here"
encoded_data, encoding_table = huffman_encode(data)

print("Original data:", data)
print("Encoded data:", encoded_data)
