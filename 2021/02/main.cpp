#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

void part1() {
  ifstream ifs("input.txt");

  string line;
  int x = 0, y = 0;

  while (getline(ifs, line)) {
    istringstream iss(line);
    string command;
    int val;

    iss >> command >> val;

    if (command == "forward") {
      x += val;
    } else if (command == "down") {
      y += val;
    } else if (command == "up") {
      y -= val;
    }
  }

  cout << x * y << endl;
}

void part2() {
  ifstream ifs("input.txt");

  string line;
  int x=0, y=0, aim=0;

  while (getline(ifs, line)) {
    istringstream iss(line);
    string command;
    int val;

    iss >> command >> val;

    if (command == "forward") {
      x += val;
      y += aim * val;
    } else if (command == "down") {
      aim += val;
    } else if (command == "up") {
      aim -= val;
    }
  }

  cout << x * y << endl;
}

int main() {
  part1();
  part2();

  return 0;
}
