#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

using Grid = vector<vector<int>>;
using Position = pair<int, int>;

int a_star(const Grid& grid) {
  const int N = grid.size();
  const int M = grid[0].size();
  const Position start{0, 0};

  Grid g_score(N, vector<int>(M, numeric_limits<int>::max()));
  g_score[start.first][start.second] = 0;

  Grid f_score(N, vector<int>(M, numeric_limits<int>::max()));
  f_score[start.first][start.second] = N-1 + M-1;

  auto comp = [&f_score] (Position p1, Position p2) { 
    return f_score[p1.first][p1.second] > f_score[p2.first][p2.second];
  };

  unordered_set<int> open_s;
  priority_queue<Position, vector<Position>, decltype(comp)> open(comp);
  open.push(start);
  open_s.insert(start.first*M + start.second);

  while (!open.empty()) {
    Position current = open.top();
    if (current == Position{N-1, M-1}) {
      return g_score[N-1][M-1];
    }

    open.pop();
    vector<Position> neighbors;
    if (current.first > 0) {
      neighbors.push_back({current.first - 1, current.second});
    }
    if (current.first < (N-1)) {
      neighbors.push_back({current.first + 1, current.second});
    }
    if (current.second > 0) {
      neighbors.push_back({current.first, current.second - 1});
    }
    if (current.second < (M-1)) {
      neighbors.push_back({current.first, current.second + 1});
    }

    for (auto n: neighbors) {
      size_t tent = g_score[current.first][current.second] + grid[n.first][n.second];
      if (tent < g_score[n.first][n.second]) {
        g_score[n.first][n.second] = tent;
        f_score[n.first][n.second] = tent + (N-1 - n.first) + (M-1 - n.second);

        if (open_s.find(n.first * M + n.second) == open_s.end()) {
          open.push(n);
          open_s.insert(n.first * M + n.second);
        }
      }

    }
  }

  return - 1;
}

void part1() {
  ifstream ifs("input.txt");

  Grid grid;
  string line;
  while (getline(ifs, line)) {
    vector<int> v;
    transform(line.begin(), line.end(), back_inserter(v), [](auto c) { return c - '0'; });
    grid.push_back(v);
  }

  cout << a_star(grid) << endl;

}

void part2() {
  ifstream ifs("input.txt");

  Grid tile;
  string line;
  while (getline(ifs, line)) {
    vector<int> v;
    transform(line.begin(), line.end(), back_inserter(v), [](auto c) { return c - '0'; });
    tile.push_back(v);
  }

  const int N = tile.size();
  const int M = tile[0].size();
  const int NN = 5 * N;
  const int MM = 5 * M;

  Grid grid(N*5,  vector<int>(M*5, 0));

  for (int i=0; i < NN; i++) {
    for (int j=0; j < MM; j++) {
      int ii = i / N;
      int jj = j / M;
      grid[i][j] = (tile[i % N][j % M] + (ii + jj));
      if (grid[i][j] > 9) {
        grid[i][j] = grid[i][j] % 10 + 1;
      }
      // cout << grid[i][j];
    }
    //cout << endl;
  }

  cout << a_star(grid) << endl;

}

int main() {
  part1();
  part2();
  return 0;
}
