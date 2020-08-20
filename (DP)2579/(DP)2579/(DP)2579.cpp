
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n,i;
    int ss[301];
    int score[301];
    cin >> n;
    for (i = 1; i <= n; i++) {
        cin >> ss[i];
    }
    score[0] = 0;
    score[1] = ss[1];
    score[2] = ss[1] + ss[2];

    for (i = 3; i <= n; i++) {
        score[i] = max(ss[i - 1] + score[i - 3] + ss[i], score[i - 2] + ss[i]);
    }

    printf("%d", score[n]);
}
