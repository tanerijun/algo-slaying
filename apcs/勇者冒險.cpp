#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <algorithm>

using namespace std;

const int INF = numeric_limits<int>::max();
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

struct Node
{
    int x, y, level;
    Node(int x, int y, int level) : x(x), y(y), level(level) {}
    // Custom comparator for priority queue (min-heap based on level)
    bool operator>(const Node &other) const
    {
        return level > other.level;
    }
};

int find_minimum_level(int R, int C, pair<int, int> start, pair<int, int> end, vector<vector<int>> &map_grid)
{
    vector<vector<int>> dist(R, vector<int>(C, INF));
    priority_queue<Node, vector<Node>, greater<Node>> pq; // min-heap

    dist[start.first][start.second] = 0;
    pq.push(Node(start.first, start.second, 0));

    while (!pq.empty())
    {
        Node current = pq.top();
        pq.pop();

        int x = current.x, y = current.y, level = current.level;

        if (x == end.first && y == end.second)
        {
            return level;
        }

        // Skip if we've found a better path to this node
        if (level > dist[x][y])
            continue;

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx >= 0 && nx < R && ny >= 0 && ny < C && map_grid[nx][ny] != -1)
            {
                int new_level = max(level, map_grid[nx][ny]);
                if (new_level < dist[nx][ny])
                {
                    dist[nx][ny] = new_level;
                    pq.push(Node(nx, ny, new_level));
                }
            }
        }
    }

    return -1; // No path found (shouldn't happen)
}

int main()
{
    // Disables the synchronization between C and C++ standard streams
    // which can greatly improve the performance of cin/cout operations
    ios_base::sync_with_stdio(false);

    // Unties cin from cout. By default, cin is tied to cout, which means that cout
    // is flushed automatically before cin does an input operation. Untying them can improve performance.
    cin.tie(NULL);

    int R, C, Rs, Cs, Rd, Cd, N;
    cin >> R >> C >> Rs >> Cs >> Rd >> Cd >> N;

    vector<vector<int>> map_grid(R, vector<int>(C, -1));

    // Set start and end points to 0 (no monsters)
    map_grid[Rs][Cs] = 0;
    map_grid[Rd][Cd] = 0;

    // Fill in passable areas with monster levels
    for (int i = 0; i < N; i++)
    {
        int Ri, Ci, Li;
        cin >> Ri >> Ci >> Li;
        map_grid[Ri][Ci] = Li;
    }

    int result = find_minimum_level(R, C, {Rs, Cs}, {Rd, Cd}, map_grid);
    cout << result << endl;

    return 0;
}