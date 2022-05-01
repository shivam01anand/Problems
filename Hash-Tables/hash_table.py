class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def key_to_hash(self, key):
        VAL = 0
        for el in key:
            VAL += ord(el)
        return VAL % self.MAX

    def hash_to_value(self, key, val):
        h = self.key_to_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.key_to_hash(key)
        return self.arr[h]


t = HashTable()

t.hash_to_value("march 1", 120)
t.arr
t.get("march 1")

# moreover can use class operators...
# getitem setitem can replace custom fucntions

# Thus,
# the hash output was used as position in index
# but what if two different strings %100 came to be same?

# aka Collision

# Same Hash, Diff Value..

# Need to store it as [(march1, 10),(march 104,43)] -> tuple of key value
# instead of only one single val in hash location
# -> change data structure to

# other approach, linear probing...
# if found filled... go to next..
# keep probing until empty


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def key_to_hash(self, key):
        VAL = 0
        for el in key:
            VAL += ord(el)
        return VAL % self.MAX

    def __setitem__(self, key, val):
        h = self.key_to_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.key_to_hash(key)
        return self.arr[h]


t = HashTable()
t["march 6"] = 130
t["fnf"] = 142
t["fnf"]


class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def key_to_hash(self, key):
        VAL = 0
        for el in key:
            VAL += ord(el)
        return VAL % self.MAX

    def __setitem__(self, key, val):
        h = self.key_to_hash(key)
        found = False
        for idx, el in enumerate(self.arr[h]):
            if (
                len(el) == 2 and el[0] == key
            ):  # if already exists... need to replace tuple itself, cant mutate tuple
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.key_to_hash(key)
        return [el[1] for el in self.arr[h] if el[0] == key][0]

    def __delitem__(self, key):
        h = self.key_to_hash(key)
        for idx, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h][idx]


t = HashTable()
t["march 6"] = 120
t["fnf"] = 142
t["march 6"] = 130
t["march 17"] = 130

t["march 17"]
t.arr

t["march 17"]

del t["march 17"]

t.arr
