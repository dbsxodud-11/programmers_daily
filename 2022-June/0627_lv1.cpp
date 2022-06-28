#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    const int n = id_list.size();
    
    vector<int> answer(n);
    unordered_map<string, int> id2index;
    for (int i=0; i<n; i++) {
        id2index[id_list[i]] = i;
    }
    
    sort(report.begin(), report.end());
    report.erase(unique(report.begin(), report.end()), report.end());
    
    vector<pair<int, int>> v;
    for (const auto& r: report) {
        stringstream ss(r);
        string source, target;
        ss >> source >> target;
        v.push_back(pair(id2index[source], id2index[target]));
    }
    
    vector<int> count(n);
    for (const auto& [src, tar]: v) {
        count[tar] += 1;
    }
    
    for(const auto& [src, tar]: v) {
        if (count[tar] >= k) {
            answer[src] += 1;
        }
    }
    
    return answer;
}