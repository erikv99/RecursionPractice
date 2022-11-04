def internalProduct(list1, list2): 
    """
        Gives back the internal product of two given lists of integers. 
        So [1, 4] and [3, 5] would be 1 * 3 + 4 * 5 == 3 + 20 == 23
        arg list1, list2: the lists of integers. 
        returns the internal product of these 2 lists.
    """

    # Base case:
    # Lists are not the same size (we cant multiply the coresponding indexes with eachother)
    # OR 
    # One of the lists is empty.
    if len(list1) == 0 or len(list2) == 0 or len(list1) != len(list2):
        return 0;

    # Recusive case
    # We want to multiply the first (index 0) index of each list with eachother and return that + the recursive call for the next indexes
    # We slice both lists so that we only pass the next in line numbers for both lists.
    return list1[0] * list2[0] + internalProduct(list1[1::], list2[1::])

    # The way this works it its returns the outcome lets say 5. then goes to the next. lets say outcome 6. then next lets say 10. then when it hits the base case
    # it will return 0 and go all the way back so 0 + 10 + 6 + 5 end we end up with 21. 

assert internalProduct([1,4], [3,5]) == 23
assert internalProduct([2, 2], [3, 2]) == 10

def sum(x):
    """
        Gives back the sum of all the numbers up to and including x. 
        so if x = 5 it would give the sum of 1 + 2 + 3 + 4 + 5
    """

    # Base case:
    # x is 0
    if x == 0:
        return 0;

    # Recursive case:
    # return current num (x) + x -1 
    # if we start with x 5 it would go like this:
    # 5 + sum(4) -> 4 + sum(3) -> 3 + sum(2) -> 2 + sum(1) -> 1 + sum(0) -> base case return 0.
    # 5 + 4 + 3 + 2 + 1 + 0;
    return x  + sum(x - 1)

assert sum(5) == 15
assert sum(4) == 10

