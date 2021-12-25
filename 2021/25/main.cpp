#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

void part1() {
  ifstream ifs("input.txt");

  vector<string> grid;
  string line;

  while(getline(ifs, line)) {
    grid.push_back(line);
  }

  const int N = grid.size();
  const int M = grid[0].size();

  vector<string> grid_old(N, string(M, '.'));
  vector<string> grid_(grid);

  size_t steps = 0;

  while (!equal(grid.begin(), grid.end(), grid_old.begin())) {
    grid_old = grid;

    for (int i=0; i < N; i++) {
      for (int j=0; j < M; j++) {
        if (grid[i][j] == '>' && grid[i][(j+1)%M] == '.') {
          swap(grid_[i][j], grid_[i][(j+1)%M]);
        }
      }
    }

    swap(grid, grid_);
    grid_=grid;

    for (int i=0; i < N; i++) {
      for (int j=0; j < M; j++) {
        if (grid[i][j] == 'v' && grid[(i+1)%N][j] == '.') {
          swap(grid_[i][j], grid_[(i+1)%N][j]);
        }
      }
    }

    swap(grid, grid_);
    grid_=grid;

    steps++;
  }

  cout << steps << endl;
}

int main() {
  part1();
  return 0;
}
