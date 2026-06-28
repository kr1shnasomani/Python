from typing import List

def printNos(x: int) -> List[int]: 
    # Write your code here
    result = []

    if x == 1:
        return [1]

    for i in range(1, x + 1):
        result = result + [i]
        i += 1
    
    return result