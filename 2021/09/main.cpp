#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

using Cave = vector<vector<int>>;
using Visited = vector<vector<bool>>;

void part1() {
  ifstream ifs("input.txt");

  string line;
  Cave cave;
  while (getline(ifs, line)) {
    vector<int> v(line.size());
    transform(begin(line), end(line), begin(v),
              [](const char c) { return c - '0'; });
    cave.push_back(v);
  }

  const int N = cave.size();
  const int M = cave[0].size();

  int sum = 0;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      vector<int> n;
      if (i == 0) {
        n.push_back(cave[i + 1][j]);
      } else if (i == (N - 1)) {
        n.push_back(cave[i - 1][j]);
      } else {
        n.push_back(cave[i + 1][j]);
        n.push_back(cave[i - 1][j]);
      }

      if (j == 0) {
        n.push_back(cave[i][j + 1]);
      } else if (j == (M - 1)) {
        n.push_back(cave[i][j - 1]);
      } else {
        n.push_back(cave[i][j + 1]);
        n.push_back(cave[i][j - 1]);
      }

      if (cave[i][j] < *min_element(n.begin(), n.end())) {
        sum += cave[i][j] + 1;
      }
    }
  }

  cout << sum << endl;
}

int dfs(int i, int j, const Cave& cave, Visited& visited) {
  const int N = cave.size();
  const int M = cave[0].size();

  visited[i][j] = true;

  vector<pair<int, int>> nbrs;
  if (i == 0) {
    nbrs.push_back({i+1, j});
  } else if (i == (N - 1)) {
    nbrs.push_back({i-1, j});
  } else {
    nbrs.push_back({i + 1, j});
    nbrs.push_back({i - 1, j});
  }

  if (j == 0) {
    nbrs.push_back({i, j+1});
  } else if (j == (M - 1)) {
    nbrs.push_back({i, j-1});
  } else {
    nbrs.push_back({i, j+1});
    nbrs.push_back({i, j-1});
  }

  int size = 1;

  for (auto n : nbrs) {
    if (cave[n.first][n.second] != 9 && !visited[n.first][n.second]) {
      size += dfs(n.first, n.second, cave, visited);
    }
  }

  return size;
}

void part2() {
  ifstream ifs("input.txt");

  string line;
  vector<vector<int>> cave;
  while (getline(ifs, line)) {
    vector<int> v(line.size());
    transform(begin(line), end(line), begin(v),
              [](const char c) { return c - '0'; });
    cave.push_back(v);
  }

  const int N = cave.size();
  const int M = cave[0].size();

  Visited visited(N, vector<bool>(M, false));

  vector<int> island_sizes;
  for (int i=0; i < N; i++) {
    for (int j=0; j < M; j++) {
      if (cave[i][j] != 9 && !visited[i][j]) {
        int size = dfs(i, j, cave, visited);
        island_sizes.push_back(size);
        push_heap(island_sizes.begin(), island_sizes.end());
      }
    }
  }

  pop_heap(island_sizes.begin(), island_sizes.end());
  int x1 = island_sizes.back();
  island_sizes.pop_back();

  pop_heap(island_sizes.begin(), island_sizes.end());
  int x2 = island_sizes.back();
  island_sizes.pop_back();

  pop_heap(island_sizes.begin(), island_sizes.end());
  int x3 = island_sizes.back();
  island_sizes.pop_back();

  cout << x1 * x2 * x3 << endl;

}

int main() {
  part1();
  part2();
  return 0;
}
