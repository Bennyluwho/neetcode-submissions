/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> ret;

    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> temp;
        if (root) {
            q.push(root);
        }
        while(q.size() > 0) {
            int length = q.size();
            for(int i = 0; i < length; ++i) {
                TreeNode* curr = q.front();
                q.pop();
                cout << curr->val << endl;
                temp.push_back(curr->val);
                if (curr->left) {
                    q.push(curr->left);
                }
                if(curr->right) {
                    q.push(curr->right);
                }
            }
            ret.push_back(temp);
            temp.clear();
        }
        return ret;
    }
};
