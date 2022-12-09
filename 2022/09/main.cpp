#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>
#include <tuple>
#include <array>
#include <deque>
#include <regex>
#include <optional>

using namespace std;

struct Point {
  int x;
  int y;
  Point(int x, int y) : x(x), y(y) {}

  Point operator + (const Point& other) const {
    return Point(x + other.x, y + other.y);
  }

  Point operator * (int n) const {
    return Point(x * n, y * n);
  }

  Point operator / (int in) const {
    return Point(x / in, y / in);
  }

  Point operator - (const Point& other) const {
    return Point(x - other.x, y - other.y);
  }

  const Point& operator += (const Point& other) {
    x += other.x;
    y += other.y;
    return *this;
  }
};

int dist(const Point& a, const Point& b) {
  return abs(a.x - b.x) + abs(a.y - b.y);
}

const map<char, const Point> directions = {
  {'U', Point(0, 1)},
  {'D', Point(0, -1)},
  {'L', Point(-1, 0)},
  {'R', Point(1, 0)},
};

int main(int argc, char** argv) {
  ifstream ifs("input", ios::in);
  string line;
  vector<string> lines;
  
  while (getline(ifs, line)) {
    lines.push_back(line);
  }

  const size_t width = 1024;

  const Point start(width/2, width/2);
  Point head = start;
  Point tail = start;

  vector<vector<int> > grid(width, vector<int>(width, 0));

  size_t sum = 0;
  for (const auto& line : lines) {
    char dir = line[0];
    int num = stoi(line.substr(2));
    // cout << dir << endl;
    while (num--) {
      head += directions.at(dir);
      bool in_line = head.x == tail.x || head.y == tail.y;
      if (in_line && dist(head, tail) == 2) {
        Point dir = (head - tail) / 2;
        // cout << "dir: " << dir.x << " " << dir.y << endl;
        // int dir_x = (head.x != tail.x) ? 1 : 0;
        // int dir_y = (head.y != tail.y) ? 1 : 0;
        tail += dir;
      } else if(!in_line && dist(head, tail) > 2) {
        // cout << "diag " << dist(head, tail) << endl;
        int dir_x = (head.x > tail.x) ? 1 : -1;
        int dir_y = (head.y > tail.y) ? 1 : -1;
        tail += Point(dir_x, dir_y);
      }
      if (grid[width-tail.y][tail.x] == 0) {
        sum += 1;
        grid[width-tail.y][tail.x] = 1;
      }
        // cout << "head: " << head.x << ", " << head.y << " ";
        // cout << "tail: " << tail.x << ", " << tail.y << endl;
    }
  }

  cout << sum << endl;

  return 0;
}
