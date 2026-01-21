//Write a function that reverses a string. The input string is given as an array of characters s

class Solution {
public:
    void reverseString(vector<char>& s) {
        int l=0;                  // l=left
        int r=s.size()-1;         // r=right

        while(l<r){               // Keep swapping characters until the left pointer crosses the right pointer
            swap(s[l],s[r]);
            l++;
            r--;
        }                         // Time: O(n) 
    }                             // Space: O(1)
};
