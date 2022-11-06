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

def reverse(string): 
    """
        Reverses a string 
        arg string: string to reverse
        returns: reversed string
    """

    # Base case
    # No more chars in string 
    if len(string) == 0:
        return ""

    # Recursive case
    # returning the last char of the string and calling the function again with the string minus the last char.
    return string[-1] + reverse(string[:-1:])


assert reverse("hello") == "olleh"
assert reverse("") == ""

def multiply(num, multiplier):
    """
        multiplies num multiplier amount of times and returns the result.
        arg num: number to multiply
        arg multiplier: how many times to multiply num.
        returns: result of the multiplication
    """

    # base case:
    # no more multiplications have to be done (multiplier == 0)
    # number to multiply is 0 0 * anything = 0
    if multiplier == 0 or num == 0:
        return 0;

    # recursive case:
    # we return the num (so it gets added to the total at the end)
    # and we add the next multiplication to it, we decrement the multiplier.
    return num + multiply(num, multiplier - 1)

    # so 3 * 4 = 3 + multiply(3, 3) -> (one multi finished) -> 3 + multiply(3, 2) -> 3 + multiply(3, 1) -> 3 + multiply(3, 0) -> base case ret 0.

assert multiply(4, 4) == 16
assert multiply(3, 4) == 12

def getIndexOf(item, listToCheck):
    """
        Returns the index of the first occurence of item in list, 
        if not found returns the length of list. (NOT ALLOWED TO USE INDEX FUNC ofc)

        arg item: item to find index of in list
        arg listToCheck: list try to find item in.
        returns: index of num or length of 
    """

    # Base case:
    # list is empty
    if len(listToCheck) == 0:
        return 0

    # recursive case:
    # If we found the item we do not add 1 to the  count since that would mean we get the position not the index.
    # remember the count is basically the length since we do +1 for each char,
    if listToCheck[0] == item:
        return 0
    else:
        return 1 + getIndexOf(item, listToCheck[1::])
     
assert getIndexOf(42, [55, 77, 42, 12, 42, 100]) == 2
assert getIndexOf(1, [3, 2, 5]) == 3
assert getIndexOf(22, [0, 0, 1, 2, 3, 22]) == 5
assert getIndexOf(42, [55, 77, 42, 12, 42, 100]) == 2
assert getIndexOf(42, list(range(0, 100))) == 42

def isSubstringOf(subString, string):
    """"""

    # Base case

    # If len subString == 0 it means we checked every char of the substring and we found all of them in order so returning true.
    if len(subString) == 0:
        return True

    # If we still need to find a part of the substring but checked all of the string we can return false.
    if len(string) == 0 and len(subString) != 0:
        return False

    # Recursive case:
    
    # If cur char of substring is current char of string.
    if subString[0] == string[0]:

        # Use it
        return isSubstringOf(subString[1::], string[1::])

    # If cur char of substring is not current char of string 
    else:

        # Lose it, we continue with the rest of string to check for the substring
        return isSubstringOf(subString, string[1::])

assert isSubstringOf("to", "toto") == True 
assert isSubstringOf("send", "sendhelp") == True 
assert isSubstringOf("ri", "erik") == True 

def getMaxUsableSpace(availableSpace, books):
    """
        Given a int availableSpace and a list of booksizes we determine
        how much of the space we can max utilize.
        The goal is to use as much of the available size, not place as many books.

        arg int availableSpace: space available on the bookshelf.
        arg int[] books: list of book sizes.
        returns: max usable space.
    """

    # We want to use the use it or lose it principle. 
    # So this means that for each book size we will check if we can place it. 
    # If not we forget it (lose it). 

    # We want to go from big to small for the book sizes.
    books = sorted(books, reverse=True)

    # Base case:

    # Is there available space? 
    if availableSpace <= 0:
        return 0

    # Are there books, if not we can utilize 0 of the space.
    if len(books) == 0:
        return 0

    # Recursive case:

    # Can we use the current book?
    if availableSpace >= books[0]:

        spaceUtilized = books[0]
        newAvailableSpace = availableSpace - spaceUtilized

        # Use the book (use it)
        return spaceUtilized + getMaxUsableSpace(newAvailableSpace, books[1::])
    
    # If we cant use the current book we lose it.
    else:

        return 0 + getMaxUsableSpace(availableSpace, books[1::])

assert getMaxUsableSpace(25, [25]) == 25
assert getMaxUsableSpace(25, [1, 20, 2]) == 23
assert getMaxUsableSpace(25, [6, 1, 1, 2, 2]) == 12