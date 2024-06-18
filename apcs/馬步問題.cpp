#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// See 馬步問題.py for explanation

const int move_x[8] = {2, 1, -1, -2, -2, -1, 1, 2};
const int move_y[8] = {1, 2, 2, 1, -1, -2, -2, -1};

vector<vector<int>> board;
vector<vector<int>> result;

bool is_valid_move(int row, int col, int n)
{
  return row >= 0 && row < 3 && col >= 0 && col < n && board[row][col] == 0;
}

void knight_tour(int row, int col, int move_i, int n)
{
  if (move_i == 3 * n)
  {
    vector<int> board_state;
    for (int i = 0; i < 3; ++i)
    {
      for (int j = 0; j < n; ++j)
      {
        board_state.push_back(board[i][j]);
      }
    }
    result.push_back(board_state);
    return;
  }

  for (int i = 0; i < 8; ++i)
  {
    int next_row = row + move_x[i];
    int next_col = col + move_y[i];
    if (is_valid_move(next_row, next_col, n))
    {
      board[next_row][next_col] = move_i + 1;
      knight_tour(next_row, next_col, move_i + 1, n);
      board[next_row][next_col] = 0; // backtrack
    }
  }
}

int main()
{
  int n;
  cin >> n;

  board = vector<vector<int>>(3, vector<int>(n, 0));
  board[0][0] = 1;

  knight_tour(0, 0, 1, n);

  if (result.empty())
  {
    cout << 0 << endl;
  }
  else
  {
    vector<int> lexicographically_smallest = *min_element(result.begin(), result.end());
    for (size_t i = 0; i < lexicographically_smallest.size(); ++i)
    {
      cout << lexicographically_smallest[i];
      if (i != lexicographically_smallest.size() - 1)
        cout << " ";
    }
    cout << endl;
  }

  return 0;
}
