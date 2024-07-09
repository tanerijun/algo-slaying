#include <iostream>
#include <set>
#include <numeric>

using namespace std;

int main()
{
    int n, m, g[26][26]{}, i, j, k, p, p1 = 0;
    pair<int, char> o[26];
    char a, b;
    cin >> n >> m;
    for (p = 0; p < m; p++)
    {
        cin >> a >> b;
        g[a - 'A'][b - 'A'] = 1;
        for (k = 0; k < n; k++)
        {
            for (i = 0; i < n; i++)
            {
                for (j = 0; j < n; j++)
                {
                    g[i][j] |= g[i][k] && g[k][j];
                }
            }
        }
        for (i = 0; i < n && !g[i][i]; i++)
            ;
        if (i < n)
            break;
        if (!p1)
        {
            set<int> on;
            for (i = 0; i < n; i++)
            {
                o[i].first = accumulate(g[i], g[i] + n, 0);
                on.insert(o[i].first);
                o[i].second = char(i + 'A');
            }
            if (on.size() == n)
            {
                p1 = p + 1;
            }
        }
    }
    if (p < m)
    {
        cout << "Order conflict after getting pair " << p + 1 << endl;
    }
    else if (!p1)
    {
        cout << "No answer\n";
    }
    else
    {
        sort(o, o + n);
        cout << "Determine the testing sequence after getting pair " << p1 << " : ";
        for (i = n - 1; i >= 0; i--)
        {
            cout << o[i].second;
        }
        cout << endl;
    }
}