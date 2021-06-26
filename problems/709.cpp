/*
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"

Example 2:

Input: "here"
Output: "here"

Example 3:

Input: "LOVELY"
Output: "lovely"


*/
class Solution {
public:
    string toLowerCase(string str) {
         stringbuf buffer;
        
        for (auto c : str) {
            
            char lowerC = (c >= 'A' && c <= 'Z') ? (c + 32) : c;
            buffer.sputc(lowerC);
        }
        
        return buffer.str();
    }
};