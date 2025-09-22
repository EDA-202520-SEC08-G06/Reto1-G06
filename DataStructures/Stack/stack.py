# PILAS

from DataStructures.List import array_list as list 
#from DataStructures import single_linked_list as list



def new_stack():
    
    my_stack = list.new_list()

    return my_stack



def push(my_stack, element): 
    
    return  list.add_last(my_stack, element)



def pop(my_stack):
    
    return list.remove_last(my_stack)



def is_empty(my_stack) -> bool: 
    
    return list.is_empty(my_stack) 



def top(my_stack): 
    
    return list.last_element(my_stack)



def size(my_stack) -> int: 
    
    return list.size(my_stack) 

