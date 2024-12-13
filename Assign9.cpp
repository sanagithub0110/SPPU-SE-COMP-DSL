#include <iostream>
#include <string.h>
#define max 50
using namespace std;

class STACK
{
  private:
    char a[max];
    int top;
  
  public:
    STACK()
    {
      top=-1;
      }
      
     
      void palindrome();
};

void STACK::palindrome()
{
  char str[max];
  int i,j;
  
  for(i=top,j=0;i>=0;i--,j++)
  {
    str[j]=a[i];
  }
  str[j]='\0';
  
  if(strcmp(str,a)==0)
    cout<<"\n\n String is a palindrome...";
  else
    cout<<"\n\n String is not a palindrome...";
}

int main()
{
  STACK stack;
  
  char str[max];
  int i=0;
  
  cout<<"\n Enter string to be checked whether its a palindrome: \n\n";
    cin.getline(str,50);
    
    stack.palindrome();
  
}    
    
