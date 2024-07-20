#include <iostream>
#include <vector>
#include <algorithm>

bool can_cover(const std::vector<int> &P, int K, int diameter)
{
    int count = 1;
    int curr_end = P[0] + diameter; // position where coverage ends
    for (size_t i = 1; i < P.size(); ++i)
    {
        if (P[i] > curr_end)
        { // every pos before curr_end are covered
            count++;
            curr_end = P[i] + diameter;
        }
        if (count > K)
        {
            return false;
        }
    }
    return true;
}

int find_min_diameter(const std::vector<int> &P, int K)
{
    // Set the lower bound to 1 (minimum possible diameter)
    // Set the upper bound to the maximum distance between any two points
    int left = 1, right = P.back() - P.front();
    while (left < right)
    {
        int mid = left + (right - left) / 2;
        if (can_cover(P, K, mid))
        {
            right = mid; // try lowering the diameter even more
        }
        else
        {
            left = mid + 1;
        }
    }
    return left;
}

int main()
{
    int N, K;
    std::cin >> N >> K;

    std::vector<int> P(N);
    for (int i = 0; i < N; ++i)
    {
        std::cin >> P[i];
    }

    std::sort(P.begin(), P.end());

    int res = find_min_diameter(P, K);
    std::cout << res << std::endl;

    return 0;
}