#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>

using namespace std;

template <class T>
inline void hash_combine(std::size_t& seed, const T& v) {
  std::hash<T> hasher;
  seed ^= hasher(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

size_t hash_pair(const int x, const int y) {
  //size_t seed = 0;
  size_t seed = std::hash<int>{}(x);
  //hash_combine(seed, x);
  hash_combine(seed, y);
  return seed;
}

void part1() {
  static constexpr int size = 1000;
  ifstream ifs("input.txt");

  unordered_map<int, int> grid;
  string line;

  int max_x = 0, max_y = 0;
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

    if (max(x1, x2) > max_x) max_x = max(x1, x2);
    if (max(y1, y2) > max_y) max_y = max(y1, y2);

    if (x1 == x2) {
      if (y1 > y2) {
        swap(y1, y2);
      }

      for (int j = y1; j <= y2; j++) {
        grid[x1 * size + j]++;
      }
    } else if (y1 == y2) {
      if (x1 > x2) {
        swap(x1, x2);
      }

      for (int i = x1; i <= x2; i++) {
        grid[i * size + y1]++;
      }
    }
  }

  int ret =
      count_if(grid.begin(), grid.end(), [](auto p) { return p.second > 1; });

  cout << ret << endl;
  cout << "max_x : " << max_x << " max_y: " << max_y << endl;
}

void part2() {
  ifstream ifs("input.txt");

  unordered_map<size_t, int> grid;
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

      for (int j = y1; j <= y2; j++) {
        grid[hash_pair(x1, j)]++;
      }
    } else if (y1 == y2) {
      if (x1 > x2) {
        swap(x1, x2);
      }

      for (int i = x1; i <= x2; i++) {
        grid[hash_pair(i, y1)]++;
      }
    } else {
      if (x1 > x2) {
        swap(x1, x2);
        swap(y1, y2);
      }

      for (int i = 0; i <= (x2 - x1); i++) {
        int x = x1 + i;
        int y = (y1 < y2) ? y1 + i : y1 - i;
        grid[hash_pair(x, y)]++;
      }
    }
  }

  // for ( auto p : grid) {
  //   cout << p.first << ": " << p.second << endl;
  // }

  int ret =
      count_if(grid.begin(), grid.end(), [](auto p) { return p.second > 1; });

  cout << ret << endl;
}

int main() {
  part1();
  part2();

  return 0;
}
