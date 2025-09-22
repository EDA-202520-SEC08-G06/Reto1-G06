#Codigos para array list

def new_list():
    newlist={"elements":[], "size":0}
    return newlist


def get_element(my_list, index):
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    size=my_list["size"]
    if size>0:
        keyexist=False
        for keypos in range (0, size):
            info=my_list["elements"][keypos]
            if cmp_function(element,info)==0:
                keyexist=True
                break
        if keyexist:
            return keypos
    return -1



def add_first(my_list, element): 

    my_list["elements"] = [element] + my_list["elements"]
    my_list["size"] = my_list["size"] + 1 

    return my_list



def add_last(my_list, element):

    my_list["elements"] = my_list["elements"] + [element]
    my_list["size"] = my_list["size"] + 1 

    return my_list 



def size(my_list) -> int: 

    return my_list["size"]



def is_empty(my_list) -> bool:

    return my_list["size"] == 0



def first_element(my_list): 

    if is_empty(my_list): 
        raise Exception('IndexError: list index out of range')
    
    else:
        return get_element(my_list, 0)



def last_element(my_list): 

    if is_empty(my_list): 
        raise Exception('IndexError: list index out of range')
    
    else:
        return get_element(my_list, my_list["size"]-1)



def delete_element(my_list, index:int): 

    
    if index >= my_list["size"] or index < 0: 
        raise Exception('IndexError: list index out of range')
            
    else:
        my_list["elements"] = my_list["elements"][:index] + my_list["elements"][index+1:] 
        my_list["size"] = my_list["size"] - 1
        
        return my_list



def remove_first (my_list):

    if is_empty(my_list): 
        raise Exception('IndexError: list index out of range')

    else:
        my_list["size"] = my_list["size"] - 1
        
    return my_list["elements"].pop(0)




def remove_last (my_list):

    if is_empty(my_list): 
        raise Exception('IndexError: list index out of range')

    else: 
        my_list["size"] = my_list["size"] - 1
    
    return my_list["elements"].pop(my_list["size"])




def insert_element (my_list, element, index):

    if index > my_list["size"] or index < 0:  
        raise Exception('IndexError: list index out of range')

    else:  
        my_list["elements"] = my_list["elements"][:index] + [element] + my_list["elements"][index:]
        my_list["size"] = my_list["size"] + 1 
        return my_list



def change_info (my_list, index, new_info): 

    if index > my_list["size"] or index < 0:  
        raise Exception('IndexError: list index out of range')

    else: 
         my_list["elements"][index] = new_info
         return my_list



def exchange (my_list, index1:int, index2:int):

    if (index1 >= my_list["size"] or index1 < 0) or (index2 >= my_list["size"] or index2 < 0):
        raise Exception('IndexError: list index out of range')

    elif index1 == index2: 
        return my_list

    else:
        
        temp_index1 = my_list["elements"][index1]
        
        my_list["elements"][index1] = my_list["elements"][index2]
        my_list["elements"][index2] = temp_index1
        
        return my_list



def sub_list (my_list, index:int, num_elements:int):   

    if index >= my_list["size"] or index < 0:  
        raise Exception('IndexError: list index out of range')

    else: 
        
        sub_list = new_list()
        sub_list["elements"] = my_list["elements"][index:index+num_elements]
        sub_list["size"] = len(sub_list["elements"])
        return sub_list



