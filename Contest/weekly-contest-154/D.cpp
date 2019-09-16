#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const int MAX = 1e5+100;

int low[MAX],dfn[MAX],step;
vector<int> mp[MAX];
vector<vector<int>> ans;

void tarjan(int u, int pre)
{
    dfn[u] = low[u] = step++;
    for(auto to: mp[u])
    {
        if(!dfn[to])
        {
            tarjan(to,u);
            // tarjan(u,to);
            low[u]=min(low[u], low[to]);
            if(low[to] > dfn[u])
                ans.push_back({to, u});
        }
        else if(to != pre)
            low[u]=min(low[u], dfn[to]);
    }
}

class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        for (int i=0; i<n; i++) mp[i].clear();
        int m=connections.size();
        for (int i=0; i<m; i++){
            mp[connections[i][0]].push_back(connections[i][1]);
            mp[connections[i][1]].push_back(connections[i][0]);
        }
        
        step=0;
        memset(low, 0, sizeof(low));
        memset(dfn, 0, sizeof(dfn));
        
        ans.clear();
        for (int i=0; i<n; i++){
            if (dfn[i]==0) tarjan(i, i);
            
            for (int j =0; j < n; j++){
                cout << dfn[j] << " ";
            }
            cout << endl;
            for (int j =0; j < n; j++){
                cout << low[j] << " ";
            }
            cout << endl << endl;
        }
        return ans;
    }
};

int main(){
    int n = 5;
    vector<vector <int>> connections = {{0,1},{1,2},{2,0},{1,3},{3,4}};
    Solution solution;
    vector <vector <int >> ans = solution.criticalConnections(n, connections);
    
    cout << ans.size() << endl;
    for (auto i : ans){
        cout << "[" << i[0] << "," << i[1]<< "]" << endl;
    }
    return 0;
}
