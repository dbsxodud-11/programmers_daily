#include <string>
#include <vector>
#include <cctype>
#include <regex>
#include <iostream>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    // 1. Lowercase
    for (int i=0; i<new_id.size(); i++) {
        new_id[i] = tolower(new_id[i]);
    }
    
    // 2. 특수문자 제거
    string new_id_;
    for (char ch: new_id) {
        if (islower(ch) || isdigit(ch) || ch == '-' || ch == '_' || ch == '.') {
            new_id_ += ch;
        }
    }
    new_id = new_id_;
    
    // 3. 마침표 중복 제거
    char prev_char = new_id[0];
    for (int i=1; i<new_id.size(); i++) {
        if (prev_char == '.' && prev_char == new_id[i]) {
            new_id[i-1] = '?';
        }
        prev_char = new_id[i];
    }
    
    new_id_ = "";
    for (char ch: new_id) {
        if (ch != '?') {
            new_id_ += ch;
        }
    }
    new_id = new_id_;
    
    // 4. 처음과 끝 마침표 삭제
    // cout<<new_id.size()<<endl;
    
    if (new_id[0] == '.')
        new_id.erase(0, 1);
    if (new_id[new_id.size()-1] == '.')
        new_id.erase(new_id.size()-1, 1);
    
    // 5.
    if (new_id.size() == 0)
        new_id = "a";
    
    // 6.
    if (new_id.size() >= 16) {
        new_id.erase(15);
        if (new_id[new_id.size()-1] == '.')
            new_id.erase(new_id.size()-1, 1);
    }
    
    // 7.
    if (new_id.size() <= 2) {
        while (new_id.size() < 3)
            new_id += new_id[new_id.size()-1];
    }
    
    return new_id;
}