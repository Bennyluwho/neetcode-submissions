class Solution {
public:
         bool isValid(string s) {
        stack<char> x;
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                x.push(c);
            } else {
                if (x.empty()) return false; // stack must have something to match

                if ((c == ')' && x.top() != '(') ||
                    (c == ']' && x.top() != '[') ||
                    (c == '}' && x.top() != '{')) {
                    return false;
                }
                x.pop();
            }
        }
        return x.empty(); // valid if no unmatched open brackets remain
    }
};
