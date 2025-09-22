# COLAS 

from DataStructures.List import array_list as list 
#from DataStructures import single_linked_list as list



def new_queue ():

    return list.new_list() 



def size (my_queue) -> int: 

    return list.size(my_queue)



def is_empty (my_queue) -> bool:

    return list.is_empty(my_queue)



def enqueue (my_queue, element): 

    return list.add_last(my_queue, element)



def dequeue (my_queue):

    return  list.remove_first(my_queue)



def peek (my_queue): 

    return list.first_element(my_queue) 
        


