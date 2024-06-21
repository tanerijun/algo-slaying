#include <set>
#include <iostream>
using namespace std;

int main()
{
  int n, m, a, b, i, mxa = 1;
  set<int> s[10001];
  cin >> n >> m;
  for (i = 1; i <= n; i++)
  {
    s[i].insert(i);
  }
  while (m--)
  {
    cin >> a >> b;
    if (s[a].size() < s[b].size())
    {
      swap(a, b);
    }
    s[a].insert(s[b].begin(), s[b].end());
    if (s[a].size() > s[mxa].size())
    {
      mxa = a;
    }
  }
  cout << mxa << endl;
  for (int i : s[mxa])
    cout << i << ' ';
  cout << endl;
}