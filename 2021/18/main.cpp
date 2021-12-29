#include <iostream>
#include <memory>

using namespace std;

struct Node {
  unique_ptr<Node> left = nullptr;
  unique_ptr<Node> right = nullptr;
  int val;

  //Node operator +(const Node& other) const {
  //  Node add;
  //  add.left = this;
  //  add.right = &other;
  //  return add;
  //}
};

int find_close(const string& s, int i) {
  int n = 1;
  i++;
  while (n > 0) {
    if (s[i] == '[') {
      n++;
    } else if (s[i] == ']') {
      n--;
    }
    i++;
  }
  return i-1;
}

int find_open(const string& s, int i) {
  int n = 1;
  i--;
  while (n > 0) {
    if (s[i] == ']') {
      n++;
    } else if (s[i] == '[') {
      n--;
    }
    i--;
  }
  return i+1;
}

unique_ptr<Node> parse(const string& s, int il, int ir) {
  cout << "parsing " << s.substr(il, ir - il + 1) << endl;

  if  (il >= ir) {
    return nullptr;
  }

  auto n = make_unique<Node>();

  il++;
  ir--;
  if (s[il] != '[') {
    string s_val = s.substr(il, s.find(",", il)-il);
    n->left = make_unique<Node>();
    n->left->val = stoi(s_val);
  } else {
    int ill = il;
    int ilr = find_close(s, ill);
    n->left = parse(s, ill, ilr);
  }

  if (s[ir] != ']') {
    n->right = make_unique<Node>();
    int i = s.rfind(",", ir);
    string s_val = s.substr(i+1, ir-i);
    n->right->val = stoi(s_val);
  } else {
    int irr = ir;
    int irl = find_open(s, irr);
    n->right = parse(s, irl, irr);
  }

  return n;

}

void part1() {

  //ifstream ifs("test.txt");
  //string line {"[[[[[9,8],1],2],3],4]"};
  string line {"[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"};
  //string line {"[9,8]"};

  auto root = parse(line, 0, line.size() - 1);
  cout << root->left->val <<  " ";
  cout << root->right->val << endl;
}

int main() {
  part1();
  return 0;
}
