#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <bitset>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int parse_packet(const string& s, int& pos) {

  string vs;
  bitset<3> bs(s.substr(pos, 3));
  int version = bs.to_ulong();
  int id = bitset<3>(s.substr(pos + 3, 3)).to_ulong();
  // cout << "version: " << version << " id: " << id << endl;

  pos += 6;

  if (id == 4) {
    int val = 0; 
    while (s[pos] == '1') {
      val = (val << 4) + bitset<4>(s.substr(pos+1, 4)).to_ulong();
      pos += 5;
    }
    val = (val << 4) + bitset<4>(s.substr(pos+1, 4)).to_ulong();
    pos += 5;
    // cout << "val: " << val << endl;
  } else {
    bool l_id = s[pos] == '1';
    // cout << "length id: " << l_id << endl;
    if (l_id) {
      int num_sub = bitset<11>(s.substr(pos+1, 11)).to_ulong();
      // cout << "num_sub: " << num_sub << endl;
      pos += 12;
      for (int i=0; i < num_sub; i++) {
        version += parse_packet(s, pos);
      }
    } else {
      int length = bitset<15>(s.substr(pos+1, 15)).to_ulong();
      pos += 16;
      int end = pos + length;
      // cout << "length: " << length << endl;
      while (pos < end) {
        version += parse_packet(s, pos);
      }
    }
  }

  return version;
}


void part1() {
  unordered_map<char, string> conv = {
  {'0', "0000"},
  {'1', "0001"},
  {'2', "0010"},
  {'3', "0011"},
  {'4', "0100"},
  {'5', "0101"},
  {'6', "0110"},
  {'7', "0111"},
  {'8', "1000"},
  {'9', "1001"},
  {'A', "1010"},
  {'B', "1011"},
  {'C', "1100"},
  {'D', "1101"},
  {'E', "1110"},
  {'F', "1111"},
  };

  //string input{"D2FE28"};
  //string input{"38006F45291200"};
  //string input{"EE00D40C823060"};
  //string input{"8A004A801A8002F478"};
  ifstream ifs("input.txt");
  string input;
  ifs >> input;

  string bits;
  for (auto c : input) {
    bits += conv[c];
  }

  int pos = 0;
  cout << parse_packet(bits, pos) << endl;
}

int main() {
  part1();
}
