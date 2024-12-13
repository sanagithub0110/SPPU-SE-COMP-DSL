def accept_matrix():
  M=[]
  r=int(input("Enter The No. of Rows in Matrix:"))  
  c=int(input("Enter the No. of Coloums in Matrix:"))
  print("Enter Elements Row-Wise:-")
  for i in range(r):
    row=[]
    for j in range (c):
      element=int(input(f"Element [{i+1},{j+1}]:"))
      row.append(element)
    M.append(row)
  return M,r,c

def display_matrix(M,y):
  print("Matrics %s:" %y)
  for row in M:
    print("[",end="")
    for element in row:
      print(element,"",end="")
    print("]")
  
def addition_matrix(M1,M2,r,c):
  M3=[]
  for i in range (r):
    A=[]
    for j in range (c): 
       A.append(M1[i][j]+M2[i][j])
    M3.append(A)
  display_matrix(M3,"Addition")
  
def subtraction_matrix(M1,M2,r,c):
  M3=[]
  for i in range (r):
    A=[]
    for j in range (c): 
       A.append(M1[i][j]-M2[i][j])
    M3.append(A)
  display_matrix(M3,"Subtraction") 
  
def  multiplication_matrix(M1,M2,r1,c1,c2):
   M3=[]
   for i in range (r1):
     A=[]
     for j in range (c2):
       sum=0
       for k in range(c1):
         sum=sum+(M1[i][k]*M2[k][j])
       A.append(sum)
     M3.append(A)
   display_matrix(M3,"Multiplication")
   
def find_transpose_matrix(M,r,c):
  T=[]
  for i in range (c):
    A=[]
    for j in range (r):
      A.append(M[j][i])
    T.append(A)
  display_matrix(T,"Transpose")
    
def main():
 M1=[]
 M2=[]
 while True:
        print("\t1:Accept The Matrix")
        print("\t2:Addition of Matrix")
        print("\t3:Subtraction of matrix")
        print("\t4:Multiplication of matrix")
        print("\t5:Transpose of Matrix")
        print("\t6:Exit")
        ch=int(input("Enter your choice:"))
        if ch==6:
            print("End of program")
            break
        elif ch==1:
            print("Enter The Details Of Matrix 1:")
            M1,r1,c1=accept_matrix()
            print("Enter The Details Of Matrix 2:")
            M2,r2,c2=accept_matrix()
            display_matrix(M1,1)
            display_matrix(M2,2)
        elif ch==2:
            if r1!=r2 or c1!=c2:
              print("Matrix Addition cannot be done")
            else:
              addition_matrix(M1,M2,r1,c1)
        elif ch==3: 
            if r1!=r2 or c1!=c2:
              print("Matrix subtraction cannot be done")
            else:
              subtraction_matrix(M1,M2,r1,r2)
        elif ch==4:
            if c1!=r2:
               print("Matrix Multiplication cannot be done")
            else:
               multiplication_matrix(M1,M2,r1,c1,c2)
        elif ch==5: 
            print("\t 1:Transpose of 1st Matrix")
            print("\t 2:Transpose of 2nd Matrix")
            y=int(input("Enter your choice:"))
            if y==1:
              find_transpose_matrix(M1,r1,c1)
            elif y==2:
              find_transpose_matrix(M2,r2,c2)
            else:
              print("Wrong choice entered!!Try again")
                                          
        else:
            print("Wrong choice entered!!Try again")

main()
quit()
