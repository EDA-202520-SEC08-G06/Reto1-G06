#Codigos para single linked lists

def new_list():
    newlist={"first":None, "last":None, "size":0}
    return newlist

def get_element(my_list, pos):
    searchpos=0
    node=my_list["first"]
    while searchpos<pos:
        node=node["next"]
        searchpos+=1
    return node["info"]
    
def is_present(my_list, element, cmp_function):
        is_in_array=False
        temp=my_list["first"]
        count=0
        while not is_in_array and temp is not None:
            if cmp_function(element,temp["info"])==0:
                is_in_array= True
            else:
                temp=temp["next"]
                count+=1
        if not is_in_array:
            count=-1
        return count 
    
from DataStructures.List.list_node import new_single_node 

#add first
def add_first(my_list, element):
    newnode=new_single_node(element)
    if my_list["size"] == 0:   
        my_list["first"] = newnode
        my_list["last"] = newnode      
    else:
        newnode["next"] = my_list["first"]  
        my_list["first"] = newnode
    
    my_list["size"] += 1
    return my_list

#add last
def add_last(my_list, element):
    newnode=new_single_node(element)
    if my_list["size"]>0:
        my_list["last"]["next"]=newnode
    else:
        my_list["first"]=newnode
    my_list["last"]=newnode
    my_list["size"]+=1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]["info"]

def is_empty(my_list):
    return my_list["size"]==0

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"]

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if my_list["size"] > 0:
        if pos == 0:
            my_list["first"] = my_list["first"]["next"]
            
            if my_list["size"] == 1:
                my_list["last"] = None
                
            my_list["size"] -= 1
        
        else:
            temp = my_list["first"]
            count = 0
            
            while count < pos - 1:
                temp = temp["next"]
                count += 1
            
            if pos == my_list["size"] - 1:
                temp["next"] = None
                my_list["last"] = temp
            else:
                temp["next"] = temp["next"]["next"]
            
            my_list["size"] -= 1
    
    return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    element=my_list["first"]["info"]
    my_list["first"]=my_list["first"]["next"]
    if my_list["size"]==1:
        my_list["last"]=None
    my_list["size"]-=1    
    return element

def remove_last(my_list):
    if my_list["size"] == 0: 
        raise Exception('IndexError: list index out of range')
    
    element = my_list["last"]["info"]        
    
    if my_list["size"] == 1:      
        my_list["first"] = None
        my_list["last"] = None
    else:
        temp = my_list["first"]
        while temp["next"]["next"] is not None:  
            temp = temp["next"]
        temp["next"] = None
        my_list["last"] = temp
    
    my_list["size"] -= 1
    return element
def insert_element(my_list, element, pos):
    newnode=new_single_node(element)
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    if pos==0:
        newnode["next"]=my_list["first"]
        my_list["first"]=newnode
        my_list["size"]+=1
    else:
        temp=my_list["first"]
        count=0
        while count<pos-1:
            temp=temp["next"]
            count+=1
        newnode["next"]=temp["next"]
        temp["next"]=newnode
        my_list["size"]+=1
    return my_list

def change_info(my_list, pos, element):
    if pos < 0 or pos >= my_list["size"]: 
        raise Exception('IndexError: list index out of range')
    temp=my_list["first"]
    count=0
    while count<pos:
        temp=temp["next"]
        count+=1
    temp["info"]=element
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    if pos2 < 0 or pos2 >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    if pos1 == pos2:
        return my_list
    
    temp = my_list["first"]
    for i in range(pos1):
        temp = temp["next"]
    element1 = temp["info"]
    
    temp = my_list["first"]
    for i in range(pos2):
        temp = temp["next"]
    element2 = temp["info"]
    
    temp = my_list["first"]
    for i in range(pos1):
        temp = temp["next"]
    temp["info"] = element2
    
    temp = my_list["first"]
    for i in range(pos2):
        temp = temp["next"]
    temp["info"] = element1
    
    return my_list

def sub_list(my_list, pos, num_elements): 
    if pos < 0 or pos >= my_list["size"]:   
        raise Exception('IndexError: list index out of range')
    
    
    if pos + num_elements > my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    sub_list_result = new_list()          
    
    temp = my_list["first"]
    for i in range(pos):                     
        temp = temp["next"]
    
    for i in range(num_elements):    
        add_last(sub_list_result, temp["info"])
        temp = temp["next"]
    
    return sub_list_result