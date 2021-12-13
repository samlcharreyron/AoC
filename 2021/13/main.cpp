#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

template <class T>
inline void hash_combine(std::size_t& seed, const T& v) {
  std::hash<T> hasher;
  seed ^= hasher(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

struct hash_pair {
  size_t operator()(const pair<int, int>& p) const {
    size_t seed = std::hash<int>{}(p.first);
    hash_combine(seed, p.second);
    return seed;
  }
};

void part1() {
  ifstream ifs("input.txt");

  string line;
  int x_max = 0, y_max = 0;
  vector<pair<int, int>> points;
  vector<pair<bool, int>> folds;
  while (getline(ifs, line)) {
    if (line[0] == 'f') {
      vector<string> words;
      istringstream iss(line);
      copy(istream_iterator<string>(iss), istream_iterator<string>(),
           back_inserter(words));
      bool is_x = (words[2][0] == 'x');
      auto it = words[2].find('=');
      int val = stoi(words[2].substr(it + 1, words[2].size()));
      folds.push_back({is_x, val});
    } else if (all_of(line.begin(), line.end(),
                      [](auto c) { return isspace(c); })) {
    } else {
      string xs, ys;
      istringstream iss(line);
      getline(iss, xs, ',');
      getline(iss, ys, ',');
      int x = stoi(xs), y = stoi(ys);
      if (x > x_max) {
        x_max = x;
      }
      if (y > y_max) {
        y_max = y;
      }
      points.push_back({stoi(xs), stoi(ys)});
    }
  }

  const int N = y_max + 1;
  const int M = x_max + 1;
  vector<vector<int>> grid(N, vector<int>(M, 0));
  for (auto p : points) {
    grid[p.second][p.first]++;
  }

  size_t ret = 0;
  if (folds[0].first) {
    // fold along x
    int start =  2 * folds[0].second - x_max;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < (x_max - folds[0].second); j++) {
        if (grid[i][x_max - j] > 0) {
          grid[i][j+start]++;
        }
      }
    }
    for (int i=0; i < N; i++) {
      for (int j=0; j < folds[0].second; j++) {
        if (grid[i][j] > 0) {
          ret++;
        }
      }
    }
  } else {
    int start = 2 * folds[0].second - y_max;
    for (int i = 0; i < (y_max - folds[0].second); i++) {
      for (int j = 0; j < M; j++) {
        if (grid[y_max - i][j] > 0) {
          grid[i+start][j]++;
        }
      }
    }

    for (int i=0; i < folds[0].second; i++) {
      for (int j=0; j < M; j++) {
        if (grid[i][j] > 0) {
          ret++;
        }
      }
    }
  }

  cout << ret << endl;
}

void part2() {
  ifstream ifs("input.txt");

  string line;
  int x_max = 0, y_max = 0;
  vector<pair<int, int>> points;
  vector<pair<bool, int>> folds;
  while (getline(ifs, line)) {
    if (line[0] == 'f') {
      vector<string> words;
      istringstream iss(line);
      copy(istream_iterator<string>(iss), istream_iterator<string>(),
           back_inserter(words));
      bool is_x = (words[2][0] == 'x');
      auto it = words[2].find('=');
      int val = stoi(words[2].substr(it + 1, words[2].size()));
      folds.push_back({is_x, val});
    } else if (all_of(line.begin(), line.end(),
                      [](auto c) { return isspace(c); })) {
    } else {
      string xs, ys;
      istringstream iss(line);
      getline(iss, xs, ',');
      getline(iss, ys, ',');
      int x = stoi(xs), y = stoi(ys);
      if (x > x_max) {
        x_max = x;
      }
      if (y > y_max) {
        y_max = y;
      }
      points.push_back({stoi(xs), stoi(ys)});
    }
  }
  
  vector<vector<int>> grid(y_max + 1, vector<int>(x_max + 1, 0));
  for (auto p : points) {
    grid[p.second][p.first]++;
  }
  
  for (auto fold : folds) {
    if (fold.first) {
      // fold along x
      int start =  2 * fold.second - x_max;
      for (int i = 0; i < (y_max + 1); i++) {
        for (int j = 0; j < (x_max - fold.second); j++) {
          if (grid[i][x_max - j] > 0) {
            grid[i][j+start] = 1;
          }
        }
      }
      x_max = fold.second;
    } else {
      int start = 2 * fold.second - y_max;
      for (int i=0; i < (y_max - fold.second); i++) {
        for (int j = 0; j < (x_max+1); j++) {
          if (grid[y_max - i][j] > 0) {
            grid[i+start][j] = 1;
          }
        }
      }
      y_max = fold.second;
    }
  }

  for (int i=0; i < y_max; i++) {
    for (int j=0; j < x_max; j++) {
      cout << grid[i][j] << " ";
    }
    cout << endl;
  }
}

int main() {
  part1();
  part2();
  return 0;
}
