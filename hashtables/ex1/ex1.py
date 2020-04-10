#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    # loop through weights and see if entry for limit - weight exists
    for i in range(len(weights)):
        retrieved = hash_table_retrieve(ht, limit - weights[i])
        if retrieved is not None:
            # figure out which value is bigger and put it first in a tuple
            if i > retrieved:
                return (i, retrieved)
            else:
                return (retrieved, i)
    
    return None



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
