from sys import stdin

from graphviz import Graph

num_node = 0


class Node:
    def __init__(self, ch, freq, left, right):
        global num_node
        self.id = str(num_node)
        num_node += 1
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __eq__(self, other):
        return type(self) == type(other) and self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:
    def __init__(self, ch_freq):
        self.h = []
        self.last = None
        self.tree = Graph()
        self.code = {}

        for ch, freq in ch_freq:
            self.h.append(Node(ch, freq, None, None))

        while len(self.h) >= 2:
            left = min(self.h)
            ind1 = self.h.index(left)
            del self.h[ind1]

            right = min(self.h)
            ind2 = self.h.index(right)
            del self.h[ind2]

            self.last = Node(None, left.freq + right.freq, left, right)
            self.h.append(self.last)
        self.traverse(self.last, "")

    def traverse(self, node, c):
        if node.left is None:
            self.tree.node(node.id, label=node.ch + "/" + str(node.freq))
            self.code[node.ch] = c
        else:
            self.tree.node(node.id, label=str(node.freq))
            self.tree.edge(node.id, node.left.id, label="0")
            self.tree.edge(node.id, node.right.id, label="1")
            self.traverse(node.left, c + "0")
            self.traverse(node.right, c + "1")

    def showTree(self):
        self.tree.view()

    def getCode(self):
        return self.code

    def avgCode(self, ch_freq):
        charlength = 0
        for ch, freq in ch_freq:
            charlength += (freq * len(self.code[ch]))

        return f"{charlength}/{self.last.freq}"


def main():
    ch_freq = []
    for line in stdin:
        ch, freq = line.split()
        ch_freq.append((ch, int(freq)))

    huffman = Huffman(ch_freq)
    huffman.showTree()
    print(huffman.getCode())
    print(f"Average character length of those huffman code: {huffman.avgCode(ch_freq)}")


if __name__ == "__main__":
    main()
