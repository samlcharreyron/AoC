#include <deque>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

using Grid = vector<vector<int>>;
static constexpr int N = 10;

vector<pair<int, int>> getNeighbors(int i, int j) {
  vector<pair<int, int>> n;
  if (i > 0) {
    n.push_back({i - 1, j});
    if (j > 0) {
      n.push_back({i - 1, j - 1});
    }
    if (j < (N - 1)) {
      n.push_back({i - 1, j + 1});
    }
  }
  if (i < (N - 1)) {
    n.push_back({i + 1, j});
    if (j > 0) {
      n.push_back({i + 1, j - 1});
    }
    if (j < (N - 1)) {
      n.push_back({i + 1, j + 1});
    }
  }
  if (j > 0) {
    n.push_back({i, j - 1});
  }
  if (j < (N - 1)) {
    n.push_back({i, j + 1});
  }
  return n;
}

void part1() {
  const int STEPS = 100;
  ifstream ifs("input.txt");

  string line;
  Grid grid;
  while (getline(ifs, line)) {
    vector<int> v;
    transform(line.begin(), line.end(), back_inserter(v),
              [](char c) { return c - '0'; });
    grid.push_back(v);
  }

  int ret = 0;
  for (int k = 0; k < STEPS; k++) {
    vector<pair<int, int>> set_z;
    deque<pair<int, int>> to_flash;
    unordered_set<int> flashed;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        grid[i][j]++;
        if (grid[i][j] > 9) {
          to_flash.push_back({i, j});
        }
      }
    }

    while (!to_flash.empty()) {
      auto [i, j] = to_flash.front();
      to_flash.pop_front();
      flashed.insert(i * N + j);

      auto n = getNeighbors(i, j);

      for (auto p : n) {
        if (count(to_flash.begin(), to_flash.end(), p) == 0 &&
            flashed.find(p.first * N + p.second) == flashed.end() &&
            ++grid[p.first][p.second] > 9) {
          to_flash.push_back({p.first, p.second});
        }
      }
    }

    for (auto x : flashed) {
      int i = x / N;
      int j = x - i*N;
      grid[i][j] = 0;
    }

    ret += flashed.size();
  }

  cout << ret << endl;
}

void part2() {
  const int STEPS = 300;
  ifstream ifs("input.txt");

  string line;
  Grid grid;
  while (getline(ifs, line)) {
    vector<int> v;
    transform(line.begin(), line.end(), back_inserter(v),
              [](char c) { return c - '0'; });
    grid.push_back(v);
  }

  int ret = 0;
  for (int k = 0; k < STEPS; k++) {
    vector<pair<int, int>> set_z;
    deque<pair<int, int>> to_flash;
    unordered_set<int> flashed;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        grid[i][j]++;
        if (grid[i][j] > 9) {
          to_flash.push_back({i, j});
        }
      }
    }

    while (!to_flash.empty()) {
      auto [i, j] = to_flash.front();
      to_flash.pop_front();
      flashed.insert(i * N + j);

      auto n = getNeighbors(i, j);

      for (auto p : n) {
        if (count(to_flash.begin(), to_flash.end(), p) == 0 &&
            flashed.find(p.first * N + p.second) == flashed.end() &&
            ++grid[p.first][p.second] > 9) {
          to_flash.push_back({p.first, p.second});
        }
      }
    }

    for (auto x : flashed) {
      int i = x / N;
      int j = x - i*N;
      grid[i][j] = 0;
    }

    if (flashed.size() == (N*N)) {
      cout << k+1 << endl;
      return;
    }


    ret += flashed.size();
  }

  // cout << ret << endl;
}

int main() {
  part1();
  part2();
  return 0;
}
