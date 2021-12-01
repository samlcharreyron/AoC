#include <fstream>
#include <iostream>
#include <unordered_map>
#include <regex>
#include <sstream>
#include <string>
#include <unordered_set>

using namespace std;

const unordered_set<string> required_fields = {"byr", "iyr", "eyr", "hgt",
                                        "hcl", "ecl", "pid"};

bool hasRequiredFields(const unordered_map<string, string>& fields) {
    for (const auto r : required_fields) {
        if (fields.count(r) == 0) {
            return false;
        }
    }

    return true;
}

bool validateFields(const unordered_map<string, string>& fields) {
    for (const auto f : fields) {
        if (f.first == "byr") {
            if (f.second.size() != 4 || stoi(f.second) < 1920 ||
                stoi(f.second) > 2002)
                return false;
        } else if (f.first == "iyr") {
            if (f.second.size() != 4 || stoi(f.second) < 2010 ||
                stoi(f.second) > 2020)
                return false;
        } else if (f.first == "eyr") {
            if (f.second.size() != 4 || stoi(f.second) < 2020 ||
                stoi(f.second) > 2030)
                return false;
        } else if (f.first == "hgt") {
            smatch m;
            if (!regex_match(f.second, m, regex("^((\\d)+)(in|cm)$"))) {
                return false;
            }

            int h = stoi(m[1].str());
            string t = m[3].str();
            if (t == "in" && (h < 59 || h > 76)) {
                return false;
            }

            if (t == "cm" && (h < 150 || h > 193)) {
                return false;
            }
        }

        else if (f.first == "hcl") {
            if (!regex_match(f.second, regex("^#[a-z0-9]{6}$"))) {
                return false;
            }
        }

        else if (f.first == "ecl") {
            const unordered_set<string> available = {"amb", "blu", "brn", "gry",
                                              "grn", "hzl", "oth"};
            if (count(available.cbegin(), available.cend(), f.second) == 0) {
                return false;
            }

        } else if (f.first == "pid") {
            if (!regex_match(f.second, regex("^[\\d]{9}$"))) {
                return false;
            }
        }
    }

    return true;
}

int main(int argc, char** argv) {
    ifstream ifs("input.txt", ios::in);

    int num_valid_1 = 0;
    int num_valid_2 = 0;
    while (ifs.good()) {
        unordered_map<string, string> fields;
        string str;
        while (getline(ifs, str)) {
            if (str.empty()) break;

            istringstream iss(str);
            string w;
            while (iss >> w) {
                istringstream wss(w);
                string f, v;
                getline(wss, f, ':');
                wss >> v;
                fields[f] = v;
            }
        }

        if (hasRequiredFields(fields)) {
            num_valid_1++;
            if (validateFields(fields)) {
                num_valid_2++;
            }
        }
    }

    cout << num_valid_1 << endl;
    cout << num_valid_2 << endl;
}
