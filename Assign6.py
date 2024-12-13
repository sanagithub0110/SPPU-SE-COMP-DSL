def accept_data(inputs):
  n=int(input("Enter the total no. of students:"))
  for i in range(n):
    while True:
      x=float(input(f"Enter the first year percentage of student {i+1}:"))
      if x<0 or x>100:
          print("Please Enter percentage in 0 to 100")
      else:
          inputs.append(x)
          break
  print("Percentage accepted successfully")
  print("\n")
  
def display_data(inputs):
  n=len(inputs)
  for i in range(n):
    print(f"The first-Year percentage of student {i+1}:",inputs[i])
  print("\n") 
  
def quick_sort(inputs,left,right):
  i=left
  j=right
  pivot=inputs[(left+right)//2]
  while i<=j:
    while inputs[i]<pivot:
      i+=1
    while inputs[j]>pivot:
      j-=1
    if i<=j:
      inputs[i],inputs[j]=inputs[j],inputs[i]  
      i+=1
      j-=1
  if left<j:
    quick_sort(inputs,left,j)
  if i<right:
    quick_sort(inputs,i,right)       
        
def display_5(inputs):     
  lists=sorted(inputs,reverse=True)
  print("Top 5 Percentage:")
  for i in range (min(5,len(lists))):
    print(f"{i+1}:{lists[i]}")
  print("\n")
 
def main():
  inputs=[]
  while True:
    print("1:Accept First-Year Percentage Marks")
    print("2:Display First-Year Percentage Marks")
    print("3:Sorting Using Quick sort")
    print("4:Top 5 Students With Highest Percentage")
    print("5:Exit")
    print("\n")
    ch=int(input("Enter your choice:"))
    if ch==5:
      print("End of program")
      break
    elif ch==1:
      accept_data(inputs)
    elif ch==2:
      display_data(inputs)
      print("\n")
    elif ch==3:
      quick_sort(inputs,0,len(inputs)-1)
      print("AFTER SORTING USING QUICK SORT:",inputs)
      print("\n")
    elif ch==4:
      display_5(inputs)
      print("\n")
    else:
      print("Wrong choice entered!!Try again")
main()
quit() 
