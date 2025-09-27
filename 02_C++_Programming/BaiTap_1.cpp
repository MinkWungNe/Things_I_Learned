// Write a C++ program to represent a graph using adjacency matrix and adjacency list.
// The program should allow adding edges and display the graph in both representations.

#include <iostream>
#include <vector>
using namespace std;

void addEdge(vector<vector<int>> &mat, vector<vector<int>> &list, int i, int j)
{
    mat[i][j] = 1;  // Đồ thị vô hướng nên cả 2 đều = 1
    mat[j][i] = 1;  // Đây là hướng của cạnh
    list[i].push_back(j);  // Lưu dữ liệu của đỉnh kề vào đỉnh
    list[j].push_back(i);  
}

// Hiển trị danh sách liền kề
void printList(const vector<vector<int>> &mat) {
    int V = mat.size();
    for (int i = 0; i < V; i++) 
    {
        cout << i << ": "; // Print the vertex
        for (int j = 0; j < mat[i].size(); j++) 
        {
            cout << mat[i][j] << " "; // Print its adjacent
        }
        cout << endl; 
    }
}

// Hiển thị ma trận liền kề
void printMatrix(vector<vector<int>> &mat)
{
    int V = mat.size();
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{

    // Tạo đồ thị 4 đỉnh
    int V = 4;
    vector<vector<int>> mat(V, vector<int>(V, 0));  // để in ma trận
    vector<vector<int>> list(V);    // để in danh sách

    // Them canh
    addEdge(mat, list, 0, 1);
    addEdge(mat,list , 0, 2);
    addEdge(mat,list , 1, 2);
    addEdge(mat,list , 2, 3);

    /* Alternatively we can also create using below
       code if we know all edges in advacem

     vector<vector<int>> mat = {
        { 0, 1, 0, 0 },
        { 1, 0, 1, 0 },
        { 0, 1, 0, 1 },
        { 0, 0, 1, 0 } }; 
    */

    cout << "Danh sach ke: " << endl;
    printList(list);

    cout << "Ma tran ke: " << endl;
    printMatrix(mat);

    return 0;
}