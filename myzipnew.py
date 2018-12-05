def myzipnew(arg1,arg2):
 if len(arg1)<len(arg2):
  length=len(arg1)
 else:
  length=len(arg2)

 list1=[None]*length
 list2=[None]*length

 for i in range(0,length):
  list1[i]=arg1[i]
  list2[i]=arg2[i]

 #print(list1)
 #print(list2)

 result=[None]*(len(list1)+len(list2))
 result[::2]=list1
 result[1::2]=list2
 #print(result)

 list3=[None]*(len(result))
 list3=[result[i:i+2] for i in range(0,len(result),2)]
 #print(list3)

 list4=[None]*(len(result))
 list4=[tuple(list3[i]) for i in range(0,len(list3))]

 print(list4)

myzipnew([1,2,3],[4,5,6])
myzipnew([1,2],[4,5,6])
myzipnew([1,2,3],[4,5])