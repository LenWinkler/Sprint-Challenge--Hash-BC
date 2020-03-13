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

    # create current ticket var
    # loop through tickets
    # look for the ticket whose source is None
    # add that ticket to hashtable storage and also set that ticket as current ticket
    # while current.destination is not None
    # loop through again
    # look for ticket whose source is current ticket's destination
    # add that ticket to hashtable storage and set that ticket as current ticket

    # when that's done
    # create current var
    # loop through hashtable.storage
    # while current destination is not None
    # route.append(current.destination)

    # return route