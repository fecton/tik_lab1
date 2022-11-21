def unique(s: str) -> str:
    """
    Gets unique values from a string and returns it
    @param s - string
    @return string of unique elements
    """
    a = ""
    for i in s:
        if i not in a:
            a += i
    return a


