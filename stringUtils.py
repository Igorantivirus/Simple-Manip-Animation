def splitByText(s: str)->list[str]:
        subSplit: list = []

        if(r"\text" not in s):
            return s.split()

        lastInd = 0
        nextInd = s.index(r"\text")
        
        while nextInd != None:
            subSplit.append(s[lastInd:nextInd])
            lastInd = s.index('}', nextInd) + 1
            subSplit.append(s[nextInd:lastInd])

            if(r"\text" in s[lastInd::]):
                nextInd = s.index(r"\text", lastInd)
            else:
                subSplit.append(s[lastInd::])
                break
        result = []
        for i in subSplit:
            if(i.startswith(r"\text")):
                result.append(i)
            else:
                result += i.split()
        return result

def getLines(ANIMATION_FILE: str):
    f = "".join(open(ANIMATION_FILE).readlines()).replace("\\next\n", "")
    result: list = []
    for i in f.split('\n'):
        result.append(i.strip())
    return result

#resutn list[processed list, tokens with border str]
def processString(line: str)->list[list, str]:
    processed = []
    toBorder = ""
    # splited = line.split()
    splited = splitByText(line)
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