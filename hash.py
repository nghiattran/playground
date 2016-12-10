capacity = 5

class Delete:
    pass

deleted = Delete()

def hash(key, offset = 0):
    return (key % capacity + offset) % capacity


def hash_insert(arr, key):
    i = 0
    stop = False
    condition = True

    while condition:
        j = hash(key, i)

        if arr[j] is None or arr[j] == deleted:
            arr[j] = key
            stop = True
        else:
            i += 1

        condition = not stop and i != capacity

    if i == capacity:
        print("Overflow")


def hash_search(arr, key):
    i = 0
    rval = None
    condition = True

    while condition:
        j = hash(key, i)
        if arr[j] == key:
            rval = j
        i+=1
        condition = (arr[j] is not None and arr[j] != key and i != capacity)

    return rval

def hash_delete(arr, key):
    index = hash_search(arr, key)
    if index is not None:
        arr[index] = deleted

arr = [None] * (capacity)

hash_insert(arr, 1)
hash_insert(arr, 2)
hash_insert(arr, 3)
hash_insert(arr, 3)
hash_insert(arr, 3)
hash_delete(arr, 3)
hash_delete(arr, 3)
print(arr)
hash_insert(arr, 16)

print(arr)

print(hash_search(arr, 3))