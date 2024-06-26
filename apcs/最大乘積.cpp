#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int n, tc = 1;

  while (cin >> n)
  {
    vector<int> s(n);

    for (int i = 0; i < n; ++i)
    {
      cin >> s[i];
    }

    long long max_product = 0;

    for (int i = 0; i < n; ++i)
    {
      long long current_product = 1;
      for (int j = i; j < n; ++j)
      {
        current_product *= s[j];
        max_product = max(max_product, current_product);
      }
    }

    cout << "Case #" << tc << ": The maximum product is " << max_product << ".\n";
    ++tc;
  }

  return 0;
}
