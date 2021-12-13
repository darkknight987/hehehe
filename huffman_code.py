from heapq import heappop, heapify, heappush

class Node:
    def __init__(self, freq, char = None):
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ""
        self.char = char

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

def create_heap(char_freq):
    node_q = [ Node(freq, char) for char, freq in char_freq.items()]
    heapify(node_q)
    while len(node_q) > 1:
        lft_child, rt_child = heappop(node_q), heappop(node_q)
        new_node = Node(lft_child.freq + rt_child.freq)
        new_node.left, new_node.right = lft_child, rt_child
        heappush(node_q, new_node)
    return heappop(node_q)

huff_codes = {}
def generate_codes(node):
    global huff_codes
    # As each node will either have 0 or 2 child, we need to check only if a single child exists
    if node.left:
        node.left.code = node.code + "0"
        node.right.code = node.code + "1"
        generate_codes(node.left)
        generate_codes(node.right)
    else:
        huff_codes[node.char] = node.code

print("\nEnter characters and frequencies. Enter -d when done: ")
char_freq = {}
while True:
    data = input().split(',')
    if data[0] == '-d':
        break
    char_freq[data[0]] = int(data[1])

root_node = create_heap(char_freq)
generate_codes(root_node)

print("\nChar\tHuffman code")
for char, code in huff_codes.items(): print("{}\t{}".format(char, code))

#char_freq = {'a': 10, 'e': 15, 'i': 12, 'o': 3, 'u': 4, 's': 13, 't': 1}
