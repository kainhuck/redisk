# handle string

from error import RediskException

# start with *
def handleArrays(string:str) -> [str]:
    parts = string.strip().split("\r\n")[1:]
    return [item for i, item in enumerate(parts) if i%2==1]
    
# start with +
def handleSimpleStrings(string:str) -> str:
    return string.strip()[1:]

# start with $
def handleBulkStrings(string:str) -> str:
    parts = string.strip().split("\r\n")
    if len(parts) > 1:
        return parts[1]
    else:
        return ""

# start with -
def handleErrors(string:str) -> str:
    raise RediskException(string.strip()[1:])

# start with :
def handleIntegers(string:str) -> int:
    return int(string.strip()[1:])

def handle(string:str) -> object:
    flag = string[0]
    if flag == "*":
        return handleArrays(string)
    elif flag == "+":
        return handleSimpleStrings(string)
    elif flag == "$":
        return handleBulkStrings(string)
    elif flag == "-":
        return handleErrors(string)
    elif flag == ":":
        return handleIntegers(string)
    else:
        return ""


if __name__ == "__main__":
    r = handleArrays("*2\r\n$3\r\nage\r\n$4\r\nname\r\n")
    print(r)
    # handleErrors("sadsad")
    handle("-dasdasd")