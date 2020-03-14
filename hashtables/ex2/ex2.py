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
    current = "None"

    # insert each ticket into hashtable
    for ticket in tickets:
        print(ticket.source, ticket.destination)
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # add first ticket to route and set new current var
    route.append(hash_table_retrieve(hashtable, None))
    first = hash_table_retrieve(hashtable, current)
    print('first', first)
    current = first.destination
    # while loop to append items to route
    while current is not None:
        # append value of hash_table_retrieve(current) to route
        route.append(hash_table_retrieve(hashtable, current))
        # set value to current var
        new = hash_table_retrieve(hashtable, current)
        current = new
        # continue until current is None
    print('route', route)
    return route