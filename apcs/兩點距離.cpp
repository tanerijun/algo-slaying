// Content
// 請設計一個函式，輸入兩點(x1,y1)及(x2,y2)的座標，傳回兩點的距離

// Input
// 輸入四個浮點數x1, y1, x2, y2，分別為兩個點的座標

// Output
// 輸出兩點間的距離

// Sample Input #1
// 1.0 2.0 4.0 6.0
// Sample Output #1
// 5

#include <cmath>
#include <iostream>

double calculateDistance(double x1, double y1, double x2, double y2) {
  return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

int main() {
  double x1, y1, x2, y2;

  std::cin >> x1 >> y1 >> x2 >> y2;

  double distance = calculateDistance(x1, y1, x2, y2);

  std::cout << distance << std::endl;

  return 0;
}
