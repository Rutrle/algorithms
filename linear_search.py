def linear_search(list, target):
    """
    returns position of target if found, if not return None
    """

    for index, value in list:
        if value == target:
            return index

    return None        
        

