def getLines(ANIMATION_FILE: str):
    f = "".join(open(ANIMATION_FILE).readlines()).replace("\\next\n", "")
    result: list = []
    for i in f.split('\n'):
        result.append(i.strip())
    return result

def splitWithBrackets(s: str) -> list[str]:
    """Разделяет строку по пробелам, игнорируя те, что находятся внутри скобок."""
    
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    open_brackets = set(matching_bracket.values())
    
    stack = []
    result = []
    last_split_index = 0

    for i, char in enumerate(s):
        if char in open_brackets:
            stack.append(char)
        elif char in matching_bracket:
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
        elif char == ' ' and not stack:
            token = s[last_split_index:i]
            if token:
                result.append(token)
            last_split_index = i + 1
            
    last_token = s[last_split_index:]
    if last_token:
        result.append(last_token)
        
    return result

#resutn list[processed list, tokens with border str]
def processString(line: str)->list[list, str]:
    processed = []
    toBorder = ""
    
    splited = splitWithBrackets(line)
    
    i = 0
    while(i < len(splited)):
        if (splited[i].startswith('#')):
            break
        if (splited[i] == r"\border"):
            if(i + 1 < len(splited)):
                toBorder = '$' + splited[i + 1] + '$'
        elif (splited[i] == r"\\"):
            processed.append(splited[i])
        else:
            processed.append('$'+splited[i]+'$')
        i+=1

    return processed, toBorder

if(__name__ == "__main__"):
    print("begin")
    print(splitWithBrackets(r"D_{1,2} = 3b^{2} - 8ac - b^2 + 4ac + 4at \pm 2bS - 8at \mp 8\frac{abt - 2a^{2} d}{S}"))


# def splitByText(s: str)->list[str]:
#         subSplit: list = []

#         if(r"\text" not in s):
#             return s.split()

#         lastInd = 0
#         nextInd = s.index(r"\text")
        
#         while nextInd != None:
#             subSplit.append(s[lastInd:nextInd])
#             lastInd = s.index('}', nextInd) + 1
#             subSplit.append(s[nextInd:lastInd])

#             if(r"\text" in s[lastInd::]):
#                 nextInd = s.index(r"\text", lastInd)
#             else:
#                 subSplit.append(s[lastInd::])
#                 break
#         result = []
#         for i in subSplit:
#             if(i.startswith(r"\text")):
#                 result.append(i)
#             else:
#                 result += i.split()
#         return result

# def isOpenBracket(s: str)->bool:
#     return s == '(' or s == '[' or s == '{'
# def isCloseBracket(s: str)->bool:
#     return s == ')' or s == ']' or s == '}'

# def getNetxInd(s: str, ind: int)->int:
#     count = 1
#     ind += 1
#     while count != 0:
#         count += isOpenBracket(s[ind])
#         count -= isCloseBracket(s[ind])
#         ind += 1
#     if(ind < len(s) and isOpenBracket(s[ind])):
#         print(s[ind::])
#         return getNetxInd(s, ind)
#     return ind

# def isAlphaOnly(s: str)->bool:
#     for i in s:
#         if(not i.isalpha() and i != '_'): return False
#     return True

# def getNearestBack(s: str, i: int, func):
#     while i >= 0:
#         if(func(s[i])):
#             break
#         i-=1
#     return i

# def splitWithLaTex(s: str)->list[str]:

#     subList: list = []

#     i = 0
#     last = 0
#     while i < len(s):
#         if(isOpenBracket(s[i])):
#             begin: int = i
#             prInd = getNearestBack(s, i, lambda char: char == '\\')
#             if (prInd != -1 and isAlphaOnly(s[prInd+1:i])):
#                 begin = prInd
#             elif (i != 0 and s[i - 1] == '_'):
#                 begin = getNearestBack(s, i - 2, lambda char: not char.isalpha())

#                 # pass 

#             subList += s[last:begin].split()
#             last = getNetxInd(s, i)
#             subList.append(s[begin:last])
#             i = last
#         i+=1

#     if(last < len(s)):
#         subList += s[last::].split()

#     return subList


# def isInBrackets(s: str, ind: int) -> bool:
#     """
#     Проверяет, находится ли символ по индексу `ind` внутри скобок любого типа: (), [], {}.

#     Использует стек для корректной обработки вложенных и разнотипных скобок.
#     Этот метод является самым надежным, чистым и эффективным.

#     Args:
#         s: Входная строка.
#         ind: Индекс символа для проверки.

#     Returns:
#         True, если символ в скобках, иначе False.
#     """
#     if not (0 <= ind < len(s)):
#         raise IndexError("Индекс вне диапазона строки")

#     # Словарь для быстрого поиска парных скобок
#     matching_bracket = {')': '(', ']': '[', '}': '{'}
#     open_brackets = set(matching_bracket.values()) # {'(', '[', '{'}
#     close_brackets = set(matching_bracket.keys())  # {')', ']', '}'}

#     stack = []  # Используем список как стек

#     # Проходим по строке СЛЕВА от нашего индекса
#     for i in range(ind):
#         char = s[i]
        
#         if char in open_brackets:
#             # Если символ - открывающая скобка, добавляем в стек
#             stack.append(char)
#         elif char in close_brackets:
#             # Если символ - закрывающая скобка, и стек не пуст,
#             # и на вершине стека парная ей открывающая скобка...
#             if stack and stack[-1] == matching_bracket[char]:
#                 # ...то "схлопываем" пару, убирая открывающую из стека.
#                 stack.pop()

#     # Если после прохода по префиксу стек не пуст, значит есть
#     # незакрытые скобки, и наш символ находится внутри них.
#     return len(stack) > 0

# def splitWithBrackets(s: str)->list[str]:
#     result = []

#     last = 0
#     i = 0
#     while (i < len(s)):
#         if (s[i] == ' ' and not isInBrackets(s, i)):
#             prS = s[last:i]
#             if(len(prS) > 0):
#                 result.append(prS)
#             last = i + 1
#         i += 1
        
#     if (last < len(s)):
#         prS = s[last::]
#         if(len(prS) > 0):
#             result.append(prS)

#     return result


