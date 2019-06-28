import sys

class HuffNode:

    def __init__(self, char, frequency):
        self.char = char
        self.freq = frequency
        self.left = None
        self.right = None

class HuffMan:
    '''define a node as huff tree node'''
    def __init__(self):
        self.encode = {}
        self.decode = {}
        self.huff_list = []
        self.data = None

    def caculate_frequency(self):
        frequency = {}
        for char in self.data:
            if not char in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def create_node(self):
        frequency = self.caculate_frequency()
        for char in frequency:
            node = HuffNode(char, frequency[char])
            self.huff_list.append(node)
    
    def huff_tree(self):
        '''build huffman tree'''
        self.create_node()
        self.huff_list.sort(key=lambda x : x.freq)
        while len(self.huff_list) > 1:
            node1 = self.huff_list[0]
            node2 = self.huff_list[1]
            self.huff_list = self.huff_list[2:]
            fsum = HuffNode(None, node1.freq + node2.freq)
            fsum.left = node1
            fsum.right = node2
            self.huff_list.append(fsum)
        return self.huff_list[0]
    
    def huff_code_rec(self, root, current_code):
        if root == None:
            return
        if root.char != None:
            self.encode[root.char] = current_code #store code for each char
            self.decode[current_code] = root.char
        self.huff_code_rec(root.left, current_code + '0')
        self.huff_code_rec(root.right, current_code + '1')

    def huff_code(self, huff_tree):
        current_code = ''
        self.huff_code_rec(huff_tree, current_code)

    def huffman_encoding(self, data):
        self.data = data
        if self.data == None:
            return None
        if len(self.data) == 1:
            self.decode = {'0': data}
            return '0', self.decode
        huff_tree = self.huff_tree()
        self.huff_code(huff_tree)
        result = ''
        for char in self.data:
            result += self.encode[char]
        return result, self.decode


    def huffman_decoding(self, data, decode_dict):
        current_bit = ""
        decode_data = ""
        for bit in data:
            current_bit += bit
            if current_bit in decode_dict:
                decode_data += decode_dict[current_bit]
                current_bit = ""
        return decode_data

if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    huffman = HuffMan()
    encoded_data, dict_ = huffman.huffman_encoding(a_great_sentence)
    # encode data size should less than origin data size.
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #should print encode data like 0101.
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.huffman_decoding(encoded_data, dict_)
    #the size of the decoded data should be equal to the size of the origin data.
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #the content of the encoded data should equal to the origin content.
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    single_string = "a"
    print ("The size of the data is: {}\n".format(sys.getsizeof(single_string)))
    print ("The content of the data is: {}\n".format(single_string))
    huffman = HuffMan()
    encoded_data, dict_ = huffman.huffman_encoding(single_string)
    # encode data size should less than origin data size.
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #should print encode data like 0101.
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.huffman_decoding(encoded_data, dict_)
    #the size of the decoded data should be equal to the size of the origin data.
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #the content of the encoded data should equal to the origin content.
    print ("The content of the encoded data is: {}\n".format(decoded_data))
