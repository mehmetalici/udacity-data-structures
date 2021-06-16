import sys
from collections import Counter
import heapq
from functools import total_ordering


LEFT_BIT = "0"
RIGHT_BIT = "1"

@total_ordering
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.bit = None

        self.left = left
        self.right = right
        

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(data: str):
    hf_tree = build_huffman_tree(data)
    codes = generate_encoded_data(hf_tree)
    encoded = "".join(map(lambda ch: codes[ch], data))
    return encoded, hf_tree


def generate_encoded_data(hf_tree: Node):     
    codes = _get_codes(hf_tree, str())
    return dict(codes)


def _get_codes(node: Node, accumulating_code: str):
    # Traverse preorder
    if node.bit is not None:
        accumulating_code += node.bit

    if node.char is not None:
        return [(node.char, accumulating_code)]

    codes = []
    codes.extend(_get_codes(node.left, accumulating_code))  
    codes.extend(_get_codes(node.right, accumulating_code))  
    return codes


def build_huffman_tree(data: str) -> list:
    # Construct the tree
    priority_queue = []
    for char, freq in Counter(data).items():
        heapq.heappush(priority_queue, Node(freq=freq, char=char))

    
    while len(priority_queue) > 1:
        lowest = heapq.heappop(priority_queue)
        sec_lowest = heapq.heappop(priority_queue)

        new_node = Node(freq=lowest.freq+sec_lowest.freq, left=lowest, right=sec_lowest)

        heapq.heappush(priority_queue, new_node)
    
    
    # BFS the tree and assign bits
    nodes_in_level = []
    nodes_in_level.append(priority_queue[0])
    while len(nodes_in_level):
        node = nodes_in_level.pop()
        for child, bit in zip([node.left, node.right], [LEFT_BIT, RIGHT_BIT]):
            if child is not None:
                child.bit = bit
                nodes_in_level.append(child)
    
    return priority_queue[0]


def huffman_decoding(data: str, tree: Node):
    decoded = ""

    node = tree
    for bit in data:
        if node.char is not None:
            decoded += node.char
            node = tree
        if bit == LEFT_BIT:
            node = node.left
        elif bit == RIGHT_BIT:
            node = node.right
        else:
            raise Exception(f"Expected {LEFT_BIT} or {RIGHT_BIT}, got {bit}")
    
    decoded += node.char # Account for the last character
    return decoded
    

if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))