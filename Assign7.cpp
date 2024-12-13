#include<iostream>
using namespace std;

struct NODE 
{
	int prn;
	string name;
	struct NODE *next;
};
typedef NODE node;

class pinnacle_club
{
	private:
	node *president;
	node *secretary;
	
	public:
	pinnacle_club();
	~pinnacle_club();
	void add_member();
	void delete_member();
	void display_members();
	void display_total_members();
	void concatenation(pinnacle_club &);
	
};

pinnacle_club :: pinnacle_club()

{
	president=NULL;
	secretary=NULL;
}

pinnacle_club :: ~pinnacle_club()
{
	node *temp, *n;
	temp=president;
	while(temp!=NULL)
	{
		n=temp;
		temp=temp->next;
		delete n;
	}
	cout<<"Destructor called!"<<endl;
}

void pinnacle_club :: add_member()
{
	node *temp;
	node *member=new node;
	cout<<"Enter the PRN Number : ";
	cin>>member->prn;
	cout<<"	Enter name of member : ";
	cin>>member->name;
	member->next=NULL;
	
	if (president==NULL)
	{
		president=member;
		cout<<"President added!!"<<endl;
	}
	else
	{
		if (secretary==NULL || president->next==NULL)
		{
			secretary=member;
			president->next=secretary;
			cout<<"Secretary added !!"<<endl;
		}
		else
		{
			temp=president;
			while(temp->next!=secretary)
			{
			temp=temp->next;
			temp->next=member;
			member->next=secretary;
			cout<<"Member added!!"<<endl;
			}
		}
	}
}
	
void pinnacle_club :: display_members()
{
	if(president==NULL)
	{
		cout<<"No members added to the pinnacle club!"<<endl;
	}
	else
	{
		node *temp;
		temp=president;
		cout<<"Pinnacle club members :"<<endl;
		cout<<"PRN"<<" "<<"Member name"<<endl;
		while (temp!=NULL)
		{
			cout<<temp->prn<<" "<<temp->name;
			if(temp==president)
			cout<<"- President";
			if(temp==secretary)
			cout<<"- Secretary";
			temp=temp->next;
		}
	}
}

int main()
{
	pinnacle_club A1, A2;
	int ch;
	do
	{
		cout<<"\t1.Add member"<<endl;
		cout<<"\t2.Delete member"<<endl;
		cout<<"\t3.Display total member"<<endl;
		cout<<"\t4.Display list in reverse order using recursion"<<endl;
		cout<<"\t5.Concanate two lists"<<endl;
		cout<<"\t6.Exit"<<endl;
		cout<<"Enter your choice : ";
		cin>>ch;
		
		switch(ch)
		{
			case 1: A1.add_member();
				break;
			case 3: A1.display_members();
				break;
			case 6: cout<<"End of program";
				break;
				
			default: cout<<"Invalid choice !!";
		}
	}
	while(ch!=6);
}

