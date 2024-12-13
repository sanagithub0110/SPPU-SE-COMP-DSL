#get data from user
def accept_data(inputs):
  n=int(input("Enter the total no. of students:"))
  for i in range(n):
    x=float(input(f"Enter the first year percentage of student {i+1}:"))
    if x<0 or x>100:
       print("Please Enter percentage in 0 to 100")
    else:
       inputs.append(x)   
  print("Percentage accepted successfully")
  print("\n")
  
#bubble sort
def bubble_sort(lists):
  for i in range(len(lists)):
    x=len(lists)-1
    for j in range(x):
      if lists[j]>lists[j+1]:
        lists[j],lists[j+1]=lists[j+1],lists[j]
  return lists
  
#selection sort
def selection_sort(lists):
  n=len(lists)
  for i in range(n):
    for j in range(n):
      if lists[i]<lists[j]:
        lists[i],lists[j]=lists[j],lists[i]
  return lists

#top 5 percentage  
def display_5(list):
  inputs=sorted(list,reverse=True)
  print("Top 5 Percentage:")
  for i in range (min(5,len(inputs))):
    print(f"{i+1}:{inputs[i]}")
  print("\n")
    
#main function 
def main():
  inputs=[]  
  while True:
        print("1:Accept First Year Percentage Marks")
        print("2:Sorting Using Bubble sort")
        print("3:Sorting Using Selection sort")
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
            list1=bubble_sort(inputs)
            print("AFTER SORTING USING BUBBLE SORT:",list1)
            print("\n")
        elif ch==3: 
            list2=selection_sort(inputs)
            print("AFTER SORTING USING SELECTION SORT:",list2)
            print("\n")
        elif ch==4:
            display_5(list2)
            print("\n") 
        else:
            print("Wrong choice entered!!Try again")    
main()
quit()                     
         
                     
       
