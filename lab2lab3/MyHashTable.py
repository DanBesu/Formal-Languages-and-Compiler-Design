CAPACITY = 50

class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None
    
class MyHashTable:
    def __init__(self):
        self.__size = 0
        self.__capacity = CAPACITY
        self.__items = [None] * CAPACITY

    def __hash_func(self, key):
        # generates a hash for a given key
        # params: key(string)
        # return: hash value

        hash_sum = 0
        for i, c in enumerate(key):
            hash_sum = hash_sum + (i + len(key)) ** ord(c)
            hash_sum = hash_sum % self.__capacity
        return hash_sum

    def add_item(self, key, value):
        # insert and item into the hash table
        # params: key (string), value

        if self.find_item(key) is not None: 
            return

        self.__size = self.__size + 1
        _hash = self.__hash_func(key)
        _node = self.__items[_hash]

        if _node is None:
            self.__items[_hash] = Node(key, value)
        else:
            previous_node = _node
            while _node is not None:
                previous_node = _node
                _node = _node.next_node
            previous_node.next_node = Node(key, value)

    def delete_item(self, key):
        # removes an item from the hash table
        # params: key (string)
        # return: the value of the given key

        _hash = self.__hash_func(key)
        _node = self.__items[_hash]
        previous_node = None

        # search node to the end of the list or until find its key
        while _node is not None and _node.key != key:
            previous_node = _node
            _node = _node.next_node

        # it was not found
        if _node is None:
            return None

        self.__size = self.__size - 1
        old_value = _node.value

        if previous_node is None:
            self.__items[_hash] = _node.next_node
        else:
            previous_node.next_node = previous_node.next_node.next_node

        return old_value

    def find_item(self, key):
        # find an item using its key
        # params: key(string)
        # return: the value of the node if found

        _hash = self.__hash_func(key)
        _node = self.__items[_hash]

        while _node is not None and _node.key != key:
            _node = _node.next_node

        if _node is None:
            return None
        else:
            return _node.value
