import sys
from collections import Counter
import heapq
from functools import total_ordering
from typing import List


@total_ordering
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(data: str):
    hf_tree = build_huffman_tree(data)


def generate_encoded_data(hf_tree: list):
    pass


def build_huffman_tree(data: str) -> list:
    priority_queue = []
    for char, freq in Counter(data).items():
        heapq.heappush(priority_queue, Node(char, freq))

    while len(priority_queue) > 1:
        lowest = heapq.heappop(priority_queue)
        sec_lowest = heapq.heappop(priority_queue)

        new_node = Node(None, lowest.freq+sec_lowest.freq)
        heapq.heappush(new_node)
    
    return priority_queue[0]


def huffman_decoding(data, tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))