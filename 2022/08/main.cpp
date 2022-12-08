#include <algorithm>
#include <array>
#include <deque>
#include <fstream>
#include <iostream>
#include <numeric>
#include <optional>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

using Grid = vector<vector<int> >;

vector<vector<int> > parse(const vector<string>& lines) {
  vector<vector<int> > grid;

  for (auto line : lines) {
    vector<int> row;
    for (auto c : line) {
      row.push_back(c - '0');
    }
    grid.push_back(row);
  }
  return grid;
}

vector<vector<bool> >  make_visible(int sx, int sy) {
  vector<vector<bool> > visible(sx, vector<bool>(sy, false));
  for (int i=0; i < sx; i++) {
    for (int j=0; j < sy; j++) {
      if (i == 0 || j == 0 || i == sx-1 || j == sy-1) {
        visible[i][j] = true;
      }
    }
  }
  return visible;
}

void print(vector<vector<int> > grid) {
  for (auto row : grid) {
    for (auto c : row) {
      cout << c << " ";
    }
    cout << endl;
  }
  cout << endl;
}

void part1(const Grid& grid, int sx, int sy) {
  auto visible = make_visible(sx, sy);

  auto max_l = vector<vector<int> > (sx, vector<int>(sy, 0));
  for (int i=0; i < sx; i++) {
    max_l[i][0] = grid[i][0];
  }

  auto max_r = vector<vector<int> > (sx, vector<int>(sy, 0));
  for (int i=0; i < sx; i++) {
    max_r[i][sy-1] = grid[i][sy-1];
  }

  auto max_u = vector<vector<int> > (sx, vector<int>(sy, 0));
  for (int j=0; j < sy; j++) {
    max_u[0][j] = grid[0][j];
  }

  auto max_d = vector<vector<int> > (sx, vector<int>(sy, 0));
  for (int j=0; j < sy; j++) {
    max_d[sx-1][j] = grid[sx-1][j];
  }

  for (int i=1; i < (sx -1) ; i++) {
    for (int j=1; j < (sy - 1); j++) {
      if (grid[i][j] > max_l[i][j-1]) {
        max_l[i][j] = grid[i][j];
        visible[i][j] = true;
      } else {
        max_l[i][j] = max_l[i][j-1];
      }
    }
  }

  for (int i=1; i < (sx -1) ; i++) {
    for (int j=(sy - 2); j > 0; j--) {
      if (grid[i][j] > max_r[i][j+1]) {
        max_r[i][j] = grid[i][j];
        visible[i][j] = true;
      } else {
        max_r[i][j] = max_r[i][j+1];
      }
    }
  }

  for (int j=1; j < (sy - 1); j++) {
    for (int i=1; i < (sx -1) ; i++) {
      if (grid[i][j] > max_u[i-1][j]) {
        max_u[i][j] = grid[i][j];
        visible[i][j] = true;
      } else {
        max_u[i][j] = max_u[i-1][j];
      }
    }
  }

  for (int j=1; j < (sy-1); j++) {
    for (int i=(sx-2); i > 0 ; i--) {
      if (grid[i][j] > max_d[i+1][j]) {
        max_d[i][j] = grid[i][j];
        visible[i][j] = true;
      } else {
        max_d[i][j] = max_d[i+1][j];
      }
    }
  }

  // print(max_d);

  size_t sum = accumulate(visible.begin(), visible.end(), 0, [](int acc, const auto& row) {
      return acc + accumulate(row.begin(), row.end(), 0);
    });
  cout << sum << endl;
}

int main(int argc, char** argv) {
  ifstream ifs("input", ios::in);
  string line;
  vector<string> lines;

  while (getline(ifs, line)) {
    lines.push_back(line);
  }

  const auto grid = parse(lines);
  const int sx = grid.size();
  const int sy = grid[0].size();

  part1(grid, sx, sy);

  return 0;
}
