#Accept data from user
def accept_array(A):
  print()
  print("----ENTER THE DATA IN THE SORTED ORDER----")
  print()
  n=int(input("Enter the total no. of students:="))
  for i in range(n):
    print()
    print("Enter the data of student %d:"%(i+1))
    name=input("Enter the name:=")
    mobile=input("Enter the mobile no:=")
    print()
    x=[name,mobile]
    A.append(x)
  print("Data accepted successfully")
  return n

#display data  
def display(A,n):
  print()
  print("----DATABASE IS-----")
  print()
  if(n==0):
    print("\n NO DATA FOUND")
  else:
    for i in range(n):
      print("STUDENT %d:=%10s %s"%((i+1),A[i][0],A[i][1])) 
    print("\n")  
  
#recursive binary Search function     
def recursive_binary_Search(A,s,l,X):
  if(s<=l):
    mid=int((s+l)/2)
    if(A[mid][0]==X):
      return mid
    elif(A[mid][0]>X):
      return  recursive_binary_Search(A,s,mid-1,X)   #recursive calling
    else:    
      return recursive_binary_Search(A,mid+1,l,X)
  return -1      
 
#iterative binary Search function
def iterative_binary_Search(A,n,X):
   s=0; 
   l=n-1
   while(s<=l):     
     mid=int((s+l)/2)
     if(A[mid][0]==X):
        return mid          
     else:
       if(X<A[mid][0]):
           l=mid-1
       else:
           s=mid+1
   return -1  
                  
#Fibonacci Search function
def Fibonacci_Search(A,n,X) :
   f1 = 0
   f2 = 1
   f3 = f1 + f2
   offset = -1
   while (f3 < n) :
      f1 = f2
      f2 = f3
      f3  = f1 + f2
   while (f3 > 1) :
      i = min(offset+f1, n-1)
      if(A[i][0] == X) :
         return i        
      else :
         if (X < A[i][0] ) :  
            f3  = f1
            f2 = f2 - f1
            f1 = f3 - f2
         else :     
            f3  = f2
            f2 = f1
            f1 = f3 - f2
            offset = i
   if(f2 == 1 and (offset+1) < n and A[offset + 1][0] == X) :      
      return offset+1    
   return -1 

#inserting new element in data if not found  
def insert_friend(A,n,X):
   Mob=input("enter the mobile number of the friend:")
   Y=[X,Mob]
   A.append(Y)
   j=n-1
   while(j>=0):
     if(A[j][0]<=X):
       break
     else:
       A[j+1][0]=A[j][0]
     j=j-1
   A[j+1][0]=X
   print("\nfriend  added in the database")
   display(A,n+1)
   
      
         
#main function
def main():
   while True:
    print("1.Accept Students Info")
    print("2.Display Students Info")
    print("3.Itreative Binary search")
    print("4.Recursive Binary Search")
    print("5.Fibonacci Search")
    print("6.Exit")
    ch=int(input("Enter your Choice:"))
    if(ch==1):
      A=[]
      n=accept_array(A)
    elif(ch==2):  
      display(A,n)
    elif(ch==3):
      X=input("Enter the name of the student that need to be search:=")
      flag=iterative_binary_Search(A,n,X)                                      #calling a function
      if(flag==-1):
         print("\n DATA NOT FOUND")
         insert_friend(A,n,X)
         n=n+1  #increment by one
      else:
         print("\n LOCATION IS FOUND AT:= %d"%(flag+1))  
    elif (ch==4):
      X=input("Enter the name of the student that need to be search:=")
      flag=recursive_binary_Search(A,0,n-1,X)                                   #calling a function
      if(flag==-1):
         print("\n DATA NOT FOUND")
         insert_friend(A,n,X)
         n=n+1
      else:
         print("\n LOCATION IS FOUND AT:= %d"%(flag+1))       
    elif(ch==5):
      X=input("Enter the name of the student that need to be search:=")
      flag  = Fibonacci_Search(A,n,X)                                             #calling a function
      if(flag == -1) :
         print("\n DATA NOT FOUND")
         insert_friend(A,n,X)                                                       #calling a function
         n=n+1
      else :
         print("\n LOCATION IS FOUND AT:= %d"%(flag+1))  
    else:
      print("End of the program")
      quit()
      
main()       #caliing main function
