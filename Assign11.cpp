#include<iostream>
using namespace std;
const int MAX = 5;   // Maximum number of jobs in the queue
class Job
{
    int id;       
    int priority;   
    friend class Queue; // Granting access to Queue class to Job's private members

public:
    void getdata()
    {
        cout << "\nEnter Job Id:- ";
        cin >> id;
        cout << "\nEnter Job Priority:- ";
        cin >> priority;
    }
    void putdata()
    {
        cout << "\n\t" << id;
        cout << "\t\t" << priority;
    }
};

class Queue
{
    int front, rear;   
    Job queue[MAX];     // Array to store the jobs

public:
    Queue()
    {
        front = rear = -1; // Initialize the queue as empty
    }

    bool isEmpty();    // Check if the queue is empty
    bool isFull();     // Check if the queue is full
    void insert();     // Insert a job into the queue
    void remove();     // Remove a job from the queue
    void display();    // Display all jobs in the queue
};

// Method to check if the queue is empty
bool Queue::isEmpty()
{
    if (front == (rear + 1) || rear == -1)
        return true;
    else
        return false;
}

// Method to check if the queue is full
bool Queue::isFull()
{
    if (rear == MAX - 1)
    {
        return true;
    }
    else
        return false;
}

// Method to insert a job into the queue
void Queue::insert()
{
    Job j;

    if (isFull())
    {
        cout << "\n Queue is Full.";
    }
    else
    {
        j.getdata(); 
        if (rear == -1)
        {
            front++;
            rear++;
            queue[rear] = j;
        }
        else
        {
            int i = rear;
            while (i >= front && queue[i].priority > j.priority)
            {
                queue[i + 1] = queue[i]; 
                i--;
            }
            queue[i + 1] = j;
            rear++;
        }
        cout << "\n Job Added To Queue.";
    }
}

// Method to remove a job from the queue
void Queue::remove()
{
    if (rear == -1 || front == (rear + 1))
    {
        cout << "\n Queue is Empty.";
    }
    else
    {
        front++; // Move front pointer to remove the job
        cout << "\n Job Processed From Queue.";
    }
}

// Method to display all jobs in the queue
void Queue::display()
{
    if (isEmpty())
    {
        cout << "\n Queue is Empty.";
    }
    else
    {
        for (int i = front; i <= rear; i++)
        {
            queue[i].putdata(); // Display each job
        }
    }
}

// Main function to drive the program
int main()
{
    int ch; 
    Queue q; // Create a Queue object

    do
    {
        // Menu for user interaction
        cout << "\n****MENU****\n";
        cout << "1. Insert Job\n";
        cout << "2. Display Jobs\n";
        cout << "3. Remove Job\n";
        cout << "4. Exit\n";

        cout << "Enter the Choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            q.insert(); // Insert a new job
            break;

        case 2:
            cout << "\n Job Id ";
            cout << "\t  Job Priority ";
            q.display(); // Display all jobs
            break;

        case 3:
            q.remove(); // Remove a job
            cout << "\n Remaining Jobs are :- ";
            q.display(); // Display remaining jobs
            break;

        case 4:
            cout<<"End of the Program";
            break; // Exit the loop and end the program
        }
    } while (ch != 4);
    return 0;
}
