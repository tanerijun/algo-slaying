// https://www.youtube.com/watch?v=6_gnFOeg1ZE

#include <iostream>

int main() {
  int n, i, j, c, mxc = -1, mxn, pr[26], pc[26], cr[5] = {}, cc[5] = {}, c1 = 0,
                  c2 = 0;
  for (i = 0; i < 5; i++) {
    for (j = 0; j < 5; j++) {
      std::cin >> n, pr[n] = i, pc[n] = j;
    }
  }
  while (std::cin >> n, n != -1) {
    cr[pr[n]]++, cc[pc[n]]++;
    c1 += pr[n] == pc[n];
    c2 += pr[n] + pc[n] == 4;
    pr[n] = pc[n] = -1;
  }
  for (n = 1; n <= 25; n++) {
    if (pr[n] == -1) {
      continue;
    }
    c = (cr[pr[n]] == 4) + (cc[pc[n]] == 4) + (pr[n] == pc[n] && c1 == 4) +
        (pr[n] + pc[n] == 4 && c2 == 4);
    if (c > mxc) {
      mxc = c, mxn = n;
    }
  }
  std::cout << mxn << std::endl;
}
