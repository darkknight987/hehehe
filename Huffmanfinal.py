class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.name = data[1]
        self.freq = data[0]
        self.codeword = ""

    def __lt__(self, value):
        return self.freq < value[0]

    def __getitem__(self, index):
        return self.freq

    def __str__(self):
        return self.name + ":" + str(self.freq) + "-->" + self.codeword

    def generatecodewords(self, codeword = ""):
        if self.left and self.right:
            self.left.codeword = codeword + '0'
            self.right.codeword = codeword + '1'
            self.left.generatecodewords(self.left.codeword)
            self.right.generatecodewords(self.right.codeword)

def createhuffmanheap(char_list) -> Node:
    char_list = char_list[:]
    char_list.sort()
    while len(char_list) != 1:
        pnode = Node((char_list[0][0] + char_list[1][0], "iNode"))
        pnode.left = char_list.pop(0)
        pnode.right = char_list.pop(0)
        char_list.append(pnode)
        char_list.sort()
    char_list[0].generatecodewords()
    return char_list[0]

leaves = [Node((int(i[i.find(':') + 1:]), i[:i.find(':')])) for i in input('Enter (character:frequency): ').split()]
createhuffmanheap(leaves)
for i in leaves:
    print(str(i),"\n")