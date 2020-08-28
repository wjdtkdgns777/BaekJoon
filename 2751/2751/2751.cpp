#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int num;
    
    cin >> num;
    vector<int> a(num);
    for (int i = 0; i < num; i++)
    {
        cin >> a[i];
       
    }
    sort(a.begin(), a.end());
    for (int i = 0; i < num; i++)
        cout << a[i] << '\n';
}