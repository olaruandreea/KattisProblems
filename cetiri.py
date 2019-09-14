integersInput = raw_input().split()
numberList = [int(v) for v in integersInput]

sortedList = sorted(numberList)


if int(sortedList[2])  - int(sortedList[1]) == int(sortedList[1])  - int(sortedList[0]):
    print int(sortedList[2]) + int(sortedList[2]) - int(sortedList[1])
elif int(sortedList[1])  - int(sortedList[0]) == (int(sortedList[2]) - int(sortedList[1]))/2:
    print int(sortedList[1]) + (int(sortedList[2]) - int(sortedList[1]))/2
elif int(sortedList[2]) - int(sortedList[1]) != int(sortedList[1]) - int(sortedList[0]):
    print  int(sortedList[0]) + int(sortedList[2]) - int(sortedList[1])
