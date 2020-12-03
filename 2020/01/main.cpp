#include <chrono>
#include <deque>
#include <fstream>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

int part1(deque<int> v) {
    while (!v.empty()) {
        int e1 = v.back();
        v.pop_back();
        int e2 = 1;
        for (int e2 : v) {
            if (e1 + e2 == 2020) {
                return e1 * e2;
            }
        }
    }

    return 0;
}

int part2(deque<int> v) {

    while (!v.empty()) {
        int e1 = v.back();
        v.pop_back();
        deque<int> v2 = v;
        while (!v2.empty()) {
            int e2 = v2.back();
            v2.pop_back();
            int e3 = 1;
            for (int e3 : v2) {
                if (e1 + e2 + e3 == 2020) {
                    return e1 * e2 * e3;
                }
            }
        }
    }

    return 0;
}

int main(int argc, char** argv) {
    ifstream f("input.txt", ios::in);

    if (!f.is_open()) return -1;

    deque<int> v;
    string line;
    while (getline(f, line)) {
        v.push_back(stoi(line));
    }

    auto start = chrono::high_resolution_clock::now();
    sort(v.begin(), v.end());
    int result1 = part1(v);
    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = end - start;
    cout << result1 << " elapsed " << 1e6 * elapsed.count() << " us" << endl;

    start = chrono::high_resolution_clock::now();
    int result2 = part2(v);
    end = chrono::high_resolution_clock::now();
    elapsed = end - start;
    cout << result2 << " elapsed " << 1e6 * elapsed.count() << " us" << endl;

    return 0;
}
