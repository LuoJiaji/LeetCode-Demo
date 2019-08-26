#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int calculateTime(string keyboard, string word) {
        int m[26] = {0};
        int res = 0;
        int pos = 0;

        for(int i = 0; i < 26; i++){
            m[(keyboard[i]-'a')] = i;
        }

        for (int i = 0; i < word.size(); i++){
            res += abs(m[(word[i]-'a')] - pos);
            pos = m[(word[i]-'a')];
        }

        cout << res << endl;
        return res;
    }
};

int main(){
    Solution solution;
    
    string keyboard1 = "abcdefghijklmnopqrstuvwxyz";
    string word1 = "cba";
    solution.calculateTime(keyboard1, word1);
    
    string keyboard2 = "pqrstuvwxyzabcdefghijklmno";
    string word2 = "leetcode";
    solution.calculateTime(keyboard2, word2);
    return 0;
}

