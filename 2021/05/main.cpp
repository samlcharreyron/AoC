#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

void part1() {
  static constexpr int size = 1000;
  ifstream ifs("input.txt");

  unordered_map<int, int> grid;
  string line;

  while (getline(ifs, line)) {
    stringstream ss(line);
    int x1, y1, x2, y2;
    ss >> x1;
    ss.ignore(1);
    ss >> y1;
    ss.ignore(4);
    ss >> x2;
    ss.ignore(1);
    ss >> y2;

    if (x1 == x2) {
      if (y1 > y2) {
        swap(y1, y2);
      }

      for (int j=y1; j <= y2; j++) {
        grid[x1 * size + j]++;
      }
    }
    else if (y1 == y2) {
      if (x1 > x2) {
        swap(x1, x2);
      }

      for (int i=x1; i <= x2; i++) {
        grid[i * size + y1]++;
      }
    } 
  }

  int ret = count_if(grid.begin(), grid.end(), [](auto p) {
      return p.second > 1;
      });

  cout << ret << endl;

}

int main() {
  part1();

  return 0;
}
