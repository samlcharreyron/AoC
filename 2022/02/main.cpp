#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <sstream>

using namespace std;

int play(int x, int y) {
  // 0 rock
  // 1 paper
  // 2 scissors
 
  if (x == y) {
    return -1;
  }

  if (x == 0 && y == 2) {
    // x wins
    return 0;
  }

  if (x == 0 && y == 1) {
    // y wins
    return 1;
  }

  if (x == 1 && y == 0) {
    // x wins
    return 0;
  }

  if (x == 1 && y == 2) {
    // y wins
    return 1;
  }

  if (x == 2 && y == 0) {
    // y wins
    return 1;
  }

  if (x == 2 && y == 1) {
    // x wins
    return 0;
  }

  return -1;

}

int play2(int x, int y) {
  // 0 x wins
  // 1 draw
  // 2 y wins
  if (y == 1) {
    return x;
  }

  if (x == 0 && y == 0) {
    // scissors
    return 2;
  }

  if (x == 0 && y == 2) {
    // paper
    return 1;
  }

  if (x == 1 && y == 0) {
    // rock
    return 0;
  }

  if (x == 1 && y == 2) {
    // scissors
    return 2;
  }

  if (x == 2 && y == 0) {
    // paper
    return 1;
  }

  if (x == 2 && y == 2) {
    // rock
    return 0;
  }

  return -1;
}

void part1(const vector<string>& v) {
  size_t score_x = 0;
  size_t score_y = 0;

  for (const string& s : v) {
    istringstream ss(s);
    char xs, ys;
    ss >> xs;
    ss >> ys;

    int x = xs - 'A';
    int y = ys - 'X';

    int r = play(x, y);
    if (r == 0) {
      score_x += 6 + x + 1;
      score_y += y + 1;
    } else if (r == 1) {
      score_x += x + 1;
      score_y += 6 + y + 1;
    } else {
      score_x += 3 + x + 1;
      score_y += 3 + y + 1;
    }
  }

  cout << score_x << " " << score_y << endl;
}

void part2(const vector<string>& v) {
  size_t score_x = 0;
  size_t score_y = 0;

  for (const string& s : v) {
    istringstream ss(s);
    char xs, ys;
    ss >> xs;
    ss >> ys;

    int x = xs - 'A';
    int r = ys - 'X';

    int y = play2(x, r);
    if (r == 0) {
      score_x += 6 + x + 1;
      score_y += y + 1;
      // cout << "x win" << y + 1 << endl;
    } else if (r == 2) {
      score_x += x + 1;
      score_y += 6 + y + 1;
      // cout << "y win" << 6 + y + 1 << endl;
    } else {
      score_x += 3 + x + 1;
      score_y += 3 + y + 1;
      // cout << "draw" << 3 + y + 1 << endl;
    }
  }

  cout << score_x << " " << score_y << endl;
}

int main(int argc, char** argv) {
  ifstream ifs("input.txt", ios::in);
  vector<string> v;
  // copy(istream_iterator<string>(ifs), istream_iterator<string>(), back_inserter(v));
  string line;
  while (getline(ifs, line)) {
    v.push_back(line);
  }

  part1(v);
  part2(v);

  return 0;
}
