// #include <iostream>
// using namespace std;

// int main()
// {
//     int n, c, a, b, tc;
//     for (tc = 0; cin >> n; n, tc++)
//     {
//         string s = "0123456789", a1, b1;
//         if (tc)
//             cout << endl;
//         c = 0;
//         do
//         {
//             a1 = s.substr(0, 5);
//             a = stoi(a1);
//             b = a * n;
//             if (b > 98765)
//                 break;
//             b1 = to_string(b);
//             sort(b1.begin(), b1.end());
//             if (b1 == s.substr(5))
//             {
//                 cout << b << " / " << a1 << " = " << n << endl;
//                 c++;
//             }
//             reverse(s.begin() + 5, s.end());
//         } while (next_permutation(s.begin(), s.end()));
//         if (!c)
//             cout << "There are no solutions for " << n << ".\n";
//     }
// }

#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    int N;
    int testCase = 0;

    while (cin >> N && N != 0)
    {
        if (testCase > 0)
        {
            cout << endl; // print a blank line between test cases
        }
        testCase++;

        string digits = "0123456789";
        int solutionCount = 0;

        do
        {
            // Extract the first 5 digits as 'abcde'
            string abcdeStr = digits.substr(0, 5);
            int abcde = stoi(abcdeStr);
            int fghij = abcde * N;
            // Break if fghij is more than 5 digits
            if (fghij > 98765)
                break;
            string fghijStr = to_string(fghij);

            if (fghijStr.length() == 5)
            {
                // Sort fghijStr to compare with the last 5 digits of the permutation
                sort(fghijStr.begin(), fghijStr.end());

                // Check if sorted fghijStr matches the last 5 digits of the permutation
                if (fghijStr == digits.substr(5))
                {
                    cout << setfill('0') << setw(5) << fghij << " / "
                         << abcdeStr << " = " << N << endl;
                    solutionCount++;
                }
            }

            // Reverse the last 5 digits to ensure all combinations are checked
            reverse(digits.begin() + 5, digits.end());

        } while (next_permutation(digits.begin(), digits.end()));

        if (solutionCount == 0)
        {
            cout << "There are no solutions for " << N << "." << endl;
        }
    }

    return 0;
}