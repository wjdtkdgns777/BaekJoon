

#include <iostream>
using namespace std;

int main()
{
    int n;
    long long ss[101];
    cin >> n;
    ss[1] = 1;
    ss[2] = 1;
    ss[3] = 1;
    ss[4] = 2;
    ss[5] = 2;
    ss[6] = 3;
    ss[7] = 4;
    ss[8] = 5;
    ss[9] = 7;
    ss[10] = 9;
    for (int i = 11; i <= 100; i++) {
        ss[i] = ss[i - 1] + ss[i - 5];


    }

    while (n--) {
        int a;
        cin >> a;
        printf("%lld\n", ss[a]);
    }
}

