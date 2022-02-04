def arithmetic_arranger(problems,showAnswer = False):
    firstLine = []
    secondLine = []
    bottomDash = []
    ansrLine = []
    firstLineFinal = ""
    secondLineFinal = ""
    bottomLineFinal = ""
    ansrFinal = ""
    if len(problems) > 5:
        print(len(problems))
        return "Error: Too many problems."
    else:
        for splitUpProblem in problems:
            splitUpNums = splitUpProblem.split()[0::2]
            arithmaticOp = splitUpProblem.split()[1]
            print(arithmaticOp)
        if arithmaticOp[0] == "+" or arithmaticOp == "-":
            biggestNumLen = max(len(splitUpNums[0]),len(splitUpNums[1]))
            if biggestNumLen > 4:
                return "Error: Numbers cannot be more than four digits."
            if splitUpNums[0].isdigit() == False or splitUpNums[1].isdigit() == False:
                return "Error: Numbers must only contain digits."
            if showAnswer:
                ans = 0
                if arithmaticOp == "+":
                    ans = str(int(splitUpNums[0])+int(splitUpNums[1]))
                if arithmaticOp == "-":
                    ans = str(int(splitUpNums[0])-int(splitUpNums[1]))
                ansrLine.append(ans.rjust(biggestNumLen+2))
            firstLine.append(splitUpNums[0].rjust(biggestNumLen+2))
            secondLine.append(arithmaticOp[0]+splitUpNums[1].rjust(biggestNumLen+1))
            bottomDash.append(((biggestNumLen+2)*"-").rjust(biggestNumLen+2))
            print(firstLine)
        else:
            return "Error: Operator must be '+' or '-'."
    for indx in range(0,len(problems)):
        if indx == len(problems)-1:
            firstLineFinal += firstLine[indx]
            secondLineFinal += secondLine[indx]
            bottomLineFinal += bottomDash[indx]
        if showAnswer == True:
            ansrFinal += ansrLine[indx]
        else:
            firstLineFinal += firstLine[indx]+"    "
            secondLineFinal += secondLine[indx]+"    "
            bottomLineFinal += bottomDash[indx]+"    "
        if showAnswer == True:
            ansrFinal += ansrLine[indx]+"    "
    if showAnswer:
        arranged_problems = firstLineFinal+"\n"+secondLineFinal+"\n"+bottomLineFinal+"\n"+ansrFinal
    else:
        arranged_problems = firstLineFinal+"\n"+secondLineFinal+"\n"+bottomLineFinal


    return arranged_problems