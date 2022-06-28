#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int zero_count = count(lottos.begin(), lottos.end(), 0);
    // cout<<zero_count<<endl;
    set<int> lottos_set, win_nums_set;
    for (int i=0; i<lottos.size(); i++) {
        lottos_set.insert(lottos[i]);
        win_nums_set.insert(win_nums[i]);
    }
    
    set<int> intersection;
    auto iter = set_intersection(lottos_set.begin(), lottos_set.end(),
                                 win_nums_set.begin(), win_nums_set.end(),
                                 inserter(intersection, intersection.begin()));
    
    int worst = intersection.size();
    int best = intersection.size() + zero_count;
    
    answer.push_back((best >= 2) ? 7 - best: 6);
    answer.push_back((worst >= 2) ? 7 - worst: 6);
    
    return answer;
}