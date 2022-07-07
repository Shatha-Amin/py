A = int(input("Enter an interger1"))
B = int(input("Enter an interger2"))
Op = int(input("1=+ ,2=-,3=*,4=/ 11= breakpoint"))
if( Op==1):
     print(A+B)
elif(Op==2):
     print(A - B)
elif (Op==3):
     print(A * B)
elif (Op==4):
     print(A / B)
elif(Op==11):
   exit()


