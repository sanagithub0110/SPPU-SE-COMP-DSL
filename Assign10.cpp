#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool isMatchingPair(char char1, char char2) {	
    if (char1 == '(' && char2 == ')') {
        return true; 
    } else if (char1 == '{' && char2 == '}') {
        return true;
    } else if (char1 == '[' && char2 == ']') {
        return true;
    }
    return false;
}

bool isWellParentrized(const string& exp) {
    stack<char> s;
    for (int i = 0; i < exp.length(); i++) {
        if (exp[i] == '(' || exp[i] == '{' || exp[i] == '[') {
            s.push(exp[i]);
        } else if (exp[i] == ')' || exp[i] == '}' || exp[i] == ']') {
            if (s.empty() || !isMatchingPair(s.top(), exp[i])) {
                return false;
            } else {
                s.pop();
            }  
        }
    }
    return s.empty();
}

int main() {
    string exp;
    cout << "Enter an Expression: " << endl;
    cin >> exp;
    if (isWellParentrized(exp)) {
        cout << "The string you have entered is well-parenthesized." << endl;
    } else {
        cout << "The string you have entered is not well-parenthesized." << endl;
    }
    return 0;
}

