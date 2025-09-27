// We can use adjacency matrix to find the degree of each vertex in an undirected graph.
// The degree of a vertex is the number of edges connected to it.

#include <iostream>
#include <vector>
using namespace std;

void addEdge(vector<vector<int>> &mat, int i, int j)
{
    mat[i][j] = 1;  // Đồ thị có hướng nên vào = -1 | ra = 1
    mat[j][i] = -1;
}

// Hiển thị số Bậc In/Out của các đỉnh
void printMatrix(vector<vector<int>> &mat)
{
    int V = mat.size();
    int In = 0;
    int Out = 0;
    for (int i = 0; i < V; i++)
    {
        cout << i << "'s Deg: ";
        for (int j = 0; j < V; j++)
        {
            if(mat[i][j] == 1)
            {
                Out++;
            }
            else if (mat[i][j] == -1)
            {
                In++;
            }
        }
        cout << "In = " << In << "| Out = " << Out << endl;
        In = 0; 
        Out = 0;
    }
}

int main()
{

    // Tạo đồ thị 4 đỉnh
    int V = 4;
    vector<vector<int>> mat(V, vector<int>(V, 0));  // để in ma trận

    // Them canh
    addEdge(mat, 0, 1);
    addEdge(mat, 0, 2);
    addEdge(mat, 1, 2);
    addEdge(mat, 2, 3);

    cout << "Danh sach bac cua dinh: " << endl;
    printMatrix(mat);

    return 0;
}