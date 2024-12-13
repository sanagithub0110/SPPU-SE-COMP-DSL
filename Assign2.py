def accept_marks(inputs):
    n=int(input("Enter the total no. of students:"))
    print("Enter Marks in range 0 to 30 and enter -1 for absent")
    for i in range(n):
        while True:
         x=int(input(f"Enter FDS Marks of student {i + 1} :"))
         if x>=0 and x<=30:
            inputs.append(x)
            break
         elif x==-1:
            inputs.append(-1)
            break
         else:
            print("Please enter marks in range 1 to 30")       
    print("Marks Accepted successfully")

def display_marks(inputs):
    n=len(inputs)
    if(n==0):
        print("\n no marks entered")
    else:
        print("\nMarks obtained in FDS:",inputs)

def find_average(inputs):
    sum=0
    y=len(inputs)
    for i in range(len(inputs)):
        if inputs[i]!=-1:
            sum=sum+inputs[i]
        else:
            y=y-1
    avg=sum/y        
    display_marks(inputs)
    print("Average score of class is ",avg) 

def highlow(inputs):
    max=-1
    min=31
    for i in range(len(inputs)):
         if(max<inputs[i]):
             max=inputs[i]
             max_ind=i 
         if(min>inputs[i] and inputs[i]!=-1):
             min=inputs[i]
             min_ind=i
    print("Hightest marks score of class is %d scored by student %d"%(max,max_ind+1))
    print("Lowest marks score of class is %d scored by student %d"%(min,min_ind+1))
 
def count_absent(inputs):
    count=0
    for i in range(len(inputs)):
        if(inputs[i]==-1):
            count += 1
    display_marks(inputs)
    print("Absent No of students are",count)  

def high_freq(inputs):
    freq=0
    for i in range(len(inputs)) :
        count=0
        if inputs[i]!=-1:
            for j in range(len(inputs)):
                if inputs[i]==inputs[j]:
                    count += 1
                if freq<count:
                    Marks=inputs[i]
                    freq=count
    display_marks(inputs)
    print("Marks with highest frequency is %d and it occured %d"%(Marks,freq))
                   
def main():
    inputs=[]
    while True:
        print("\n\t 1:Accept FDS Marks")
        print("\t 2:Average score of class")
        print("\t 3:Highest and Lowest score of class")
        print("\t 4:Count of absent students for this test")
        print("\t 5:Display marks with highest frequency")
        print("\t 6:Exit")
        ch=int(input("Enter your choice:"))
        if ch==6:
            print("End of program")
            break
        elif ch==1:
            accept_marks(inputs)
            display_marks(inputs)
        elif ch==2:
            find_average(inputs)
        elif ch==3: 
            highlow(inputs)
        elif ch==4:
            count_absent(inputs)
        elif ch==5: 
            high_freq(inputs)   
        else:
            print("Wrong choice entered!!Try again")
          
main()
quit()
