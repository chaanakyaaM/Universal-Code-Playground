# Title: Check palindrome
# Topic: Basics
# Language: cpp

#include <iostream>
using namespace std;
int main(){
    string s; cin >> s;
    string rev = string(s.rbegin(), s.rend());
    cout << (s == rev ? "Palindrome" : "Not palindrome");
}
