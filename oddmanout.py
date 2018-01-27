x = int(raw_input())
i = 0 
j = 1
case_no = 1
l = []
alone = ""
found  = []
final_list = []
while i < (x*2):
     number = raw_input()
     if j % 2 == 0:
         tokens = number.split()
         for each in tokens:
             if each not in l:
                 l.append(each)
             else:
                 found.append(each) 
         for number in l:
             if number not in found:
                 alone = str(number)
         final_list.append("Case #" + str(case_no)+": " + str(alone))
         case_no += 1
     alone = ""
     del l[:]
     del found[:]
     j += 1
     i += 1
for each in final_list:
    print each
