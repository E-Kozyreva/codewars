// Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

#include <string>
using namespace std;

std::string repeat_str(size_t repeat, const string& str) {
  string new_str;
  for (int i = 0; i < repeat; i++)
    new_str += str;
  return new_str;
}
