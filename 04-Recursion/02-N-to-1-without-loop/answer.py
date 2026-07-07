from typing import List

def printNos(x: int) -> List[int]:
    result = []

    while x > 0:
        result.append(x)
        x -= 1

    return result