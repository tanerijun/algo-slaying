#include <cmath>
#include <iostream>

int n[5] = {1}, found = false;

void sqrt4(int i, int k) {
  if (i < 4) {
    int kk = (int)sqrt(k / (5 - i));
    for (n[i] = n[i - 1]; n[i] <= kk; n[i]++) {
      sqrt4(i + 1, k - n[i] * n[i]);
    }
    return;
  }

  n[4] = (int)sqrt(k);
  if (n[4] * n[4] == k) {
    std::cout << n[1] << ' ' << n[2] << ' ' << n[3] << ' ' << n[4] << ' '
              << std::endl;
    found = true;
  }
}

int main() {
  int k;
  std::cin >> k;
  sqrt4(1, 1 << k);
  if (!found) {
    std::cout << "0\n";
  }
}
