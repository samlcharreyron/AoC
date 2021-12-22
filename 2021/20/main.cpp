#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <numeric>

using namespace std;

using Image = vector<string>;

static constexpr int pad = 52;

void enhance(const string& code, Image& img, const int num=2) {
  for (int k=0; k < num; k++) {
    Image img_new(img);

    for (int i=1; i < img.size()-1; i++) {
      for (int j=1; j < img[0].size()-1; j++) {
        string s_idx;
        s_idx += img[i-1][j-1];
        s_idx += img[i-1][j];
        s_idx += img[i-1][j+1];
        s_idx += img[i][j-1];
        s_idx += img[i][j];
        s_idx += img[i][j+1];
        s_idx += img[i+1][j-1];
        s_idx += img[i+1][j];
        s_idx += img[i+1][j+1];
        bitset<9> bs(s_idx, 0, 9, '.', '#');
        size_t idx = bs.to_ulong();
        //cout << "i: " << i << " j: " << j << " idx: " << idx << endl;
        img_new[i][j] = code[idx];
      }
    }

    swap(img, img_new);
  }
}

void part1() {
  ifstream ifs("input.txt");

  string code;
  getline(ifs, code);

  string line;
  // empty line
  getline(ifs, line);

  Image img;
  while(getline(ifs, line)) {
    img.push_back(line);
  }


  // pad image by 2
  for (auto& line : img) {
    line.insert(line.begin(), pad, '.');
    line.insert(line.end(), pad, '.');
  }

  string new_line(img[0].size(), '.');
  img.insert(img.begin(), pad, new_line);
  img.insert(img.end(), pad, new_line);

  enhance(code, img, 2);

  //for (auto line : img) {
  //  cout << line << endl;
  //}

  constexpr int skip = 2;
  size_t ret = accumulate(img.begin()+skip, img.end()-skip, 0, [](size_t lhs, auto& line) {
    return lhs + count(line.begin()+skip, line.end()-skip, '#');});

  cout << ret << endl;

}

void part2() {
  ifstream ifs("input.txt");

  string code;
  getline(ifs, code);

  string line;
  // empty line
  getline(ifs, line);

  Image img;
  while(getline(ifs, line)) {
    img.push_back(line);
  }

  for (auto& line : img) {
    line.insert(line.begin(), pad, '.');
    line.insert(line.end(), pad, '.');
  }

  string new_line(img[0].size(), '.');
  img.insert(img.begin(), pad, new_line);
  img.insert(img.end(), pad, new_line);

  enhance(code, img, 50);
  // for (auto line : img) {
  //   cout << line << endl;
  // }

  static constexpr int skip = 0;
  size_t ret = accumulate(img.begin()+skip, img.end()-skip, 0, [](size_t lhs, auto& line) {
    return lhs + count(line.begin()+skip, line.end()-skip, '#');});

  cout << ret << endl;

}


int main() {
  part1();
  part2();
  return 0;
}
