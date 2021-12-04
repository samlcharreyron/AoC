#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

static constexpr int board_size = 5;
static constexpr int num_boards = 100;

struct Position {
  int board;
  int row;
  int col;
};

struct Board {
  int unmarked;
  vector<int> b_rows;
  vector<int> b_cols;
  bool done;

  Board()
      : unmarked(0),
        b_rows(board_size, board_size),
        b_cols(board_size, board_size),
        done(false) {}
};

void part1() {
  ifstream ifs("input.txt");

  string line;
  getline(ifs, line);

  istringstream iss(line);

  vector<string> nums_as_strs;
  string num_as_str;
  while (getline(iss, num_as_str, ',')) {
    nums_as_strs.push_back(num_as_str);
  }

  vector<int> nums;
  transform(nums_as_strs.begin(), nums_as_strs.end(), back_inserter(nums),
            [](const auto s) { return stoi(s); });

  unordered_map<int, vector<Position>> val_2_positions;

  vector<Board> boards(num_boards);
  for (int b = 0; b < num_boards; b++) {
    getline(ifs, line);
    int unmarked = 0;
    for (int i = 0; i < board_size; i++) {
      getline(ifs, line);
      istringstream iss(line);
      for (int j = 0; j < board_size; j++) {
        Position p;
        p.board = b;
        p.row = i;
        p.col = j;
        int val;
        iss >> val;
        unmarked += val;
        // cout << "board: " << b << " v: " << val << " r: " << i << " c: " << j
        // << endl;
        val_2_positions[val].push_back(p);
      }
      boards[b].unmarked = unmarked;
    }
  }

  for (auto val : nums) {
    auto it = val_2_positions.find(val);
    if (it != val_2_positions.end()) {
      for (auto p : it->second) {
        boards[p.board].unmarked -= val;
        boards[p.board].b_rows[p.row]--;
        if (boards[p.board].b_rows[p.row] == 0) {
          cout << "board: " << p.board << " done on row " << p.row;
          cout << " with val: " << val;
          cout << " unmarked: " << boards[p.board].unmarked << endl;
          cout << val * boards[p.board].unmarked << endl;
          return;
        }
        boards[p.board].b_cols[p.col]--;
        if (boards[p.board].b_cols[p.col] == 0) {
          cout << "board: " << p.board << " done on col " << p.col;
          cout << " with val: " << val;
          cout << " unmarked: " << boards[p.board].unmarked << endl;
          cout << val * boards[p.board].unmarked << endl;
          return;
        }
      }
    }
  }
}

void part2() {
  ifstream ifs("input.txt");

  string line;
  getline(ifs, line);

  istringstream iss(line);

  vector<string> nums_as_strs;
  string num_as_str;
  while (getline(iss, num_as_str, ',')) {
    nums_as_strs.push_back(num_as_str);
  }

  vector<int> nums;
  transform(nums_as_strs.begin(), nums_as_strs.end(), back_inserter(nums),
            [](const auto s) { return stoi(s); });

  unordered_map<int, vector<Position>> val_2_positions;

  vector<Board> boards(num_boards);
  for (int b = 0; b < num_boards; b++) {
    getline(ifs, line);
    int unmarked = 0;
    for (int i = 0; i < board_size; i++) {
      getline(ifs, line);
      istringstream iss(line);
      for (int j = 0; j < board_size; j++) {
        Position p;
        p.board = b;
        p.row = i;
        p.col = j;
        int val;
        iss >> val;
        unmarked += val;
        // cout << "board: " << b << " v: " << val << " r: " << i << " c: " << j
        // << endl;
        val_2_positions[val].push_back(p);
      }
      boards[b].unmarked = unmarked;
    }
  }

  for (auto val : nums) {
    auto it = val_2_positions.find(val);
    if (it != val_2_positions.end()) {
      for (auto p : it->second) {
        if (!boards[p.board].done) {
          boards[p.board].unmarked -= val;
          boards[p.board].b_rows[p.row]--;
          if (boards[p.board].b_rows[p.row] == 0) {
            cout << "board: " << p.board << " done on row " << p.row;
            cout << " with val: " << val;
            cout << " unmarked: " << boards[p.board].unmarked << endl;
            cout << val * boards[p.board].unmarked << endl;
            boards[p.board].done = true;
          }
        }
        if (!boards[p.board].done) {
          boards[p.board].b_cols[p.col]--;
          if (boards[p.board].b_cols[p.col] == 0) {
            cout << "board: " << p.board << " done on col " << p.col;
            cout << " with val: " << val;
            cout << " unmarked: " << boards[p.board].unmarked << endl;
            cout << val * boards[p.board].unmarked << endl;
            boards[p.board].done = true;
          }
        }
      }
    }
  }
}

int main() {
  cout << "-------" << endl;
  cout << "part 1" << endl;
  part1();
  cout << "-------" << endl;
  cout << "part 2" << endl;
  part2();
  cout << "-------" << endl;
  return 0;
}
