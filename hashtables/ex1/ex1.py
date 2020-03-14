#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if len(weights) > 1:

        for i in range(len(weights)):
            hash_table_insert(ht, weights[i], i)

        for i in range(len(weights)):
               
            if hash_table_retrieve(ht, limit - weights[i]):
                
                answer_tuple = (i, hash_table_retrieve(ht, limit - weights[i]))
                if answer_tuple[0] < answer_tuple[1]:
                    new_tuple = (answer_tuple[1], answer_tuple[0])
                    return new_tuple
                
                return answer_tuple

    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
