#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>

using namespace std;

int main(int argc, char** argv) {
  ifstream ifs("input.txt", ios::in);

  size_t sum = 0;
  size_t max_val = 0;
  vector<size_t> v;
  for(string line; getline(ifs, line); ) {
    if (line.empty()) {
      max_val = max(sum, max_val);
      v.push_back(sum);
      sum = 0;
    }  else {
      sum += stoi(line);
    }
  }

  sort(v.begin(), v.end(), greater<size_t>());

  cout << v[0] << endl;
  cout << v[0] + v[1] + v[2] << endl; 
  
  return 0;
}
