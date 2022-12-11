#include <algorithm>
#include <array>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <optional>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
#include <functional>

using namespace std;

// A class that stores big integers
// Allows you to add, and multiply two big integers
class BigInt {
public:
    BigInt() = default;
    explicit BigInt(const string& s) {
        for (auto it = s.rbegin(); it != s.rend(); ++it) {
            digits.push_back(*it - '0');
        }
    }

    explicit BigInt(const int i) {
        string s = to_string(i);
        for (auto it = s.rbegin(); it != s.rend(); ++it) {
            digits.push_back(*it - '0');
        }
    }

    BigInt& operator+=(const BigInt& other) {
        int carry = 0;
        for (size_t i = 0; i < max(digits.size(), other.digits.size()) || carry; ++i) {
            if (i == digits.size()) {
                digits.push_back(0);
            }
            digits[i] += carry + (i < other.digits.size() ? other.digits[i] : 0);
            carry = digits[i] >= 10;
            if (carry) {
                digits[i] -= 10;
            }
        }
        return *this;
    }

    BigInt& operator*=(int x) {
        int carry = 0;
        for (size_t i = 0; i < digits.size() || carry; ++i) {
            if (i == digits.size()) {
                digits.push_back(0);
            }
            long long cur = carry + digits[i] * 1ll * x;
            digits[i] = int(cur % 10);
            carry = int(cur / 10);
        }
        return *this;
    }

    friend ostream& operator<<(ostream& out, const BigInt& x) {
        for (int i = int(x.digits.size()) - 1; i >= 0; --i) {
            out << x.digits[i];
        }
        return out;
    }

private:
  vector<int> digits;
};


struct Monkey {
  int num;
  char op_c;
  string operand;
  size_t divisor;
  int true_monkey;
  int false_monkey;
  deque<long long> starting_items;
  size_t inspections;

  Monkey(int num, char op_c, string operand, int divisor, int true_monkey,
         int false_monkey, const vector<int>& starting_items)
      : num(num), op_c(op_c), operand(operand), divisor(divisor),
        true_monkey(true_monkey), false_monkey(false_monkey),
        starting_items(starting_items.begin(), starting_items.end()), inspections(0) {}
};

vector<Monkey> parse_monkeys(const vector<string>& lines) {
  vector<Monkey> monkeys;
  regex monkey_re("^Monkey (\\d+):$");

  for(int i=0; i < lines.size(); i+=7) {
    smatch match;
    regex_search(lines[i], match, monkey_re);
    int monkey = stoi(match[1].str());

    stringstream ss(lines[i+1].substr(18));
    vector<int> starting_items;
    string item;
    while(getline(ss, item, ',')) {
      starting_items.push_back(stoi(item));
    }

    char op_c = lines[i+2][23];
    string operand = lines[i+2].substr(25);

    int divisor = stoi(lines[i+3].substr(21));
    int true_monkey = stoi(lines[i+4].substr(29));
    int false_monkey = stoi(lines[i+5].substr(30));

    monkeys.push_back(Monkey(monkey, op_c, operand, divisor, true_monkey, false_monkey, starting_items));
  }
  return monkeys;
}

binary_function<int, int, int> get_operation(char op_c) {
  binary_function<int, int, int> operation;
  if (op_c == '+') {
    operation = plus<int>();
  } else if (op_c == '*') {
    operation = multiplies<int>();
  }
  return operation;
}

int get_operand(const string& operand, int old) {
  if (operand == "old") {
    return old;
  } else {
    return stoi(operand);
  }
}

void print_monkeys(const vector<Monkey>& monkeys) {
  for (const auto& monkey: monkeys) {
    cout << monkey.num << ": ";
    for (int item : monkey.starting_items) {
      cout << item << ", ";
    }
    cout << " inspections: " << monkey.inspections << endl;
  }
  cout << endl;
}

void part1(vector<Monkey> monkeys) {
  for (int r=0; r < 20; r++) {
    for (auto& monkey: monkeys) {
      for (auto item : monkey.starting_items) {
        size_t worry_level = 0;
        if (monkey.op_c == '+') {
          worry_level = item + get_operand(monkey.operand, item);
        } else {
          worry_level = item * get_operand(monkey.operand, item);
        }
        worry_level /= 3;

        bool is_divisible = worry_level % monkey.divisor == 0;
        if (is_divisible) {
          // cout << "throw: " << worry_level << " to monkey " << monkey.true_monkey << endl;
          monkeys[monkey.true_monkey].starting_items.push_back(worry_level);
        } else {
          //cout << "throw: " << worry_level << " to monkey " << monkey.false_monkey << endl;
          monkeys[monkey.false_monkey].starting_items.push_back(worry_level);
        }
        monkey.starting_items.pop_front();
        monkey.inspections++;
      }
    }

    // cout << "Round " << r << endl;
    // print_monkeys(monkeys);
    // cout << endl;
  }

  vector<size_t> inspections;
  transform(monkeys.begin(), monkeys.end(), back_inserter(inspections), [](const Monkey& monkey) { return monkey.inspections; });
  sort(inspections.begin(), inspections.end());
  reverse(inspections.begin(), inspections.end());
  cout << inspections[0] * inspections[1] << endl;
}

void part2(vector<Monkey> monkeys) {
  for (int r=0; r < 20; r++) {
    for (auto& monkey: monkeys) {
      for (auto item : monkey.starting_items) {
        long long worry_level = 0;
        if (monkey.op_c == '+') {
          worry_level = item + get_operand(monkey.operand, item);
        } else {
          worry_level = item * get_operand(monkey.operand, item);
        }
        //worry_level /= 3;

        bool is_divisible = worry_level % monkey.divisor == 0;
        if (is_divisible) {
          // cout << "throw: " << worry_level << " to monkey " << monkey.true_monkey << endl;
          monkeys[monkey.true_monkey].starting_items.push_back(worry_level);
        } else {
          //cout << "throw: " << worry_level << " to monkey " << monkey.false_monkey << endl;
          monkeys[monkey.false_monkey].starting_items.push_back(worry_level);
        }
        monkey.starting_items.pop_front();
        monkey.inspections++;
      }
    }

    // cout << "Round " << r << endl;
    // print_monkeys(monkeys);
    // cout << endl;
  }

  print_monkeys(monkeys);

  vector<size_t> inspections;
  transform(monkeys.begin(), monkeys.end(), back_inserter(inspections), [](const Monkey& monkey) { return monkey.inspections; });
  sort(inspections.begin(), inspections.end());
  reverse(inspections.begin(), inspections.end());
  cout << inspections[0] * inspections[1] << endl;
}

int main(int argc, char** argv) {
  ifstream ifs("test", ios::in);
  string line;
  vector<string> lines;

  while (getline(ifs, line)) {
    lines.push_back(line);
  }

  vector<Monkey> monkeys = parse_monkeys(lines);

  part1(monkeys);
  part2(monkeys);

  return 0;
}
