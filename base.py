# handle string

from error import RediskException

# start with *
def handleArrays(rawList:list) -> list:
    times = int(rawList[0][1:])
    rawList.pop(0)
    result = []
    for _ in range(times):
        flag = rawList[0][0]
        if flag == "+":
            result.append(handleSimpleStrings(rawList))
        elif flag == "-":
            result.append(handleErrorsStr(rawList))
        elif flag == ":":
            result.append(handleIntegers(rawList))
        elif flag == "$":
            result.append(handleBulkStrings(rawList))
        elif flag == "*":
            result.append(handleArrays(rawList))

    return result
    
# start with +
def handleSimpleStrings(rawList:list) -> str:
    temp = rawList[0][1:]
    rawList.pop(0)
    return temp

# start with $
def handleBulkStrings(rawList:list) -> str:
    flag = int(rawList[0][1:])
    if flag == -1:
        temp = None
        rawList.pop(0)
    else:
        temp = rawList[1]
        rawList.pop(0)
        rawList.pop(0)
    return temp

# start with -
def handleErrors(rawList:list):
    temp = rawList[0][1:]
    rawList.pop(0)
    raise RediskException(temp)

def handleErrorsStr(rawList:list) -> RediskException:
    temp = rawList[0][1:]
    rawList.pop(0)
    return RediskException(temp)

# start with :
def handleIntegers(rawList:list) -> int:
    temp = rawList[0][1:]
    rawList.pop(0)
    return int(temp)

def handle(string:str) -> object:
    flag = string[0]
    rawList = string.strip().split("\r\n")
    if flag == "*":
        return handleArrays(rawList)
    elif flag == "+":
        return handleSimpleStrings(rawList)
    elif flag == "$":
        return handleBulkStrings(rawList)
    elif flag == "-":
        return handleErrors(rawList)
    elif flag == ":":
        return handleIntegers(rawList)
    else:
        return ""


if __name__ == "__main__":
    ...