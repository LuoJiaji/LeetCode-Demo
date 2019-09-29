const int MAXN=1e2+50;
bool block[MAXN][MAXN];

int dist[MAXN][MAXN][5];
int dx[2]={0, 1};
int dy[2]={1, 0};

class Solution {
public:
    int minimumMoves(vector<vector<int>>& grid) {
        int n=grid.size();
        
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                block[i][j]=false;
                dist[i][j][0]=dist[i][j][1]=-1;
                if (grid[i][j]==1) block[i][j]=true;
            }
        }
        
        dist[0][0][0]=0;
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                // Rotate
                for (int k=0; k<2; k++){
                    if (dist[i][j][k]==-1) continue;
                    if (i+1>=n || j+1>=n) continue;
                    if (k==0){
                        if (block[i+1][j]==false && block[i+1][j+1]==false){
                            if (dist[i][j][1-k]==-1 || dist[i][j][1-k]>dist[i][j][k]+1)
                                dist[i][j][1-k]=dist[i][j][k]+1;
                        }
                    }else{
                         if (block[i][j+1]==false && block[i+1][j+1]==false){
                            if (dist[i][j][1-k]==-1 || dist[i][j][1-k]>dist[i][j][k]+1)
                                dist[i][j][1-k]=dist[i][j][k]+1;
                        }
                    }
                }
                
                // Move
                for (int k=0; k<2; k++){
                    if (dist[i][j][k]==-1) continue;
                    for (int w=0; w<2; w++){
                        int nx[2], ny[2]; bool flag=true;
                        nx[0]=i; nx[1]=i+dx[k];
                        ny[0]=j; ny[1]=j+dy[k];
                        for (int idx=0; idx<2; idx++){
                            nx[idx]+=dx[w]; ny[idx]+=dy[w];
                            if (0<=nx[idx] && nx[idx]<n && 0<=ny[idx] && ny[idx]<n){
                                // Pass
                            }else flag=false;

                            if (block[nx[idx]][ny[idx]]) flag=false;
                        }
                        if (flag==false) continue;
                        if (dist[nx[0]][ny[0]][k]==-1 || dist[nx[0]][ny[0]][k] > dist[i][j][k]+1){
                            dist[nx[0]][ny[0]][k] = dist[i][j][k] + 1;
                        }
                    }
                }
            }
        }
        
        return dist[n-1][n-2][0];
    }
};