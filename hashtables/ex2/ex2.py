#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # var for current source
    curr_source = "NONE"

    # add tickets to hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    counter = 0

    # use while loop to look for hashtable[curr_source]
    while counter < len(tickets) - 1:
        destination = hash_table_retrieve(hashtable, curr_source)
        # if it exists
        if destination is not None:
            # add its destination to route
            route[counter] = destination
            # curr_source becomes destination
            curr_source = destination
            
            counter += 1

    # comprehension to take the None off the end of the list
    return [dest for dest in route if dest]