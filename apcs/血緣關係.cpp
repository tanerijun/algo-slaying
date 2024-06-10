#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>

using namespace std;

// Create undirected edges
void add_edge(unordered_map<int, unordered_set<int>> &graph, int u, int v)
{
  graph[u].insert(v);
  graph[v].insert(u);
}

// BFS to find the farthest node and its distance
pair<int, int> find_farthest_node(const unordered_map<int, unordered_set<int>> &graph, int start_node)
{
  unordered_set<int> visited;
  queue<pair<int, int>> q; // queue of (current_node, current_distance)
  q.push({start_node, 0});

  int farthest_node = start_node;
  int max_distance = 0;

  while (!q.empty())
  {
    int current_node = q.front().first;
    int current_distance = q.front().second;
    q.pop();

    if (visited.find(current_node) != visited.end())
    {
      continue;
    }
    visited.insert(current_node);

    if (current_distance > max_distance)
    {
      max_distance = current_distance;
      farthest_node = current_node;
    }

    for (int neighbor : graph.at(current_node))
    {
      if (visited.find(neighbor) == visited.end())
      {
        q.push({neighbor, current_distance + 1});
      }
    }
  }

  return {farthest_node, max_distance};
}

int main()
{
  int N;
  cin >> N;

  unordered_map<int, unordered_set<int>> graph;
  for (int i = 0; i < N - 1; ++i)
  {
    int a, b;
    cin >> a >> b;
    add_edge(graph, a, b);
  }

  // Find farthest node from an arbitrary start node (e.g., node 0)
  int start_node = 0; // arbitrary, any node will work
  pair<int, int> farthest_node_info = find_farthest_node(graph, start_node);

  // Find farthest node from the previously found farthest node
  pair<int, int> diameter_info = find_farthest_node(graph, farthest_node_info.first);

  // Output the diameter of the tree
  cout << diameter_info.second << endl;

  return 0;
}
