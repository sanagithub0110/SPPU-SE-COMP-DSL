#include<iostream>
using namespace std;
#define SIZE 10

class dequeue
{
  private: int arr[SIZE];
           int front, rear;
  public:  dequeue()
           {
               front=-1;
               rear=-1;
           }
           void insert_front(int );
           void insert_rear(int );
           void delete_front();
           void delete_rear();
           bool isEmpty();
           bool isFull();
           int get_rear();
           int get_front();

};
int dequeue::get_rear()
{
    if(isEmpty())
    {
        cout<<"\n Underflow !!";
        return -1;
    }
    else
        return arr[rear];
}


int dequeue::get_front()
{
    if(isEmpty())
    {
        cout<<"\n Underflow !!";
        return -1;
    }
    else
        return arr[front];
}

bool dequeue::isFull()
{
    if( (front==0 && rear==SIZE-1) || (front == rear+1))
        return true;
    else
        return false;
}

bool dequeue::isEmpty()
{
    if(front == -1)
        return true;
    else
        return false;
}

void dequeue::insert_front(int x)
{
    if(isFull())
    {
        cout<<"\n OVERFLOW!!! Queue is Full!!";
    }
    else{

        if(front==-1)
            front=rear=0;
        else if(front==0)
            front=SIZE-1;
        else
            --front;

        arr[front]=x;
    }
}


void dequeue::insert_rear(int x)
{
    if(isFull())
        cout<<"\n OVERFLOW!!! Queue is Full!!";
    else
    {
        if(front== -1)
            front=rear=0;
        else if(rear==SIZE-1)
            rear=0;
        else
            ++rear;
        arr[rear]=x;
    }
}

void dequeue::delete_front()
{
    if(isEmpty() )
        cout<<"\n UNDERFLOW !! Queue is Empty !!";
    else
    {
        int x=arr[front];

        if( front == rear)
            front = rear =-1;
            
        else if (front == SIZE-1)
            front = 0;
        else
            ++front;
        cout<<"\n Element deleted from front : "<<x;
    }
}


void dequeue::delete_rear()
{
   if(isEmpty() )
        cout<<"\n UNDERFLOW !! Queue is Empty !!";
   else
   {
       int x=arr[rear];
 
       if( front == rear )
            front = rear =-1;
   
       else if( rear==0)
           rear= SIZE-1;
       else
           --rear;
       cout<<"\n Element deleted from rear : "<<x;
   }
}

int main()
{
    int ch;
	int n;
	dequeue dq;

	do
	{
		cout<<"\n\t\t\t1 : Insert to Front";
		cout<<"\n\t\t\t2 : Insert to Rear";
		cout<<"\n\t\t\t3 : Delete from front";
		cout<<"\n\t\t\t4 : Delete from rear";
		cout<<"\n\t\t\t5 : Display element at front";
		cout<<"\n\t\t\t6 : Display element at rear";
		cout<<"\n\t\t\t7 : Exit";
		cout<<"\n\nEnter your choice : ";
		cin>>ch;
		switch(ch)
		{
			case 1 : cout<<"\nEnter the element to insert in dequeue from front: ";
					 cin>>n;
					 dq.insert_front(n);
					 break;
			case 2 : cout<<"\nEnter the element to insert in dequeue from rear: ";
					 cin>>n;
					 dq.insert_rear(n);
					 break;
            case 3:  dq.delete_front();
                     break;

            case 4:  dq.delete_rear();
                     break;
            case 5:  cout<<"\n Element at front : "<<dq.get_front();
                     break;
            case 6:  cout<<"\n Element at rear : "<<dq.get_rear();
                     break;
			case 7 : cout<<"\nEnd of Program\n";
					 break;
			default: cout<<"\nInvalid choice !! Try again\n\n";
		}
	}while(ch != 7);
	return 0;
}







