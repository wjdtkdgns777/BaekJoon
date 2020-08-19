

#include <iostream>
using namespace std;

int main()
{   
    int a,count=0;
    cin >> a;
    for (int i = 1; i <= a; i++) {
        int k;
        k = i;
        while (k > 0) {
            count++;
            k = k / 10;
        }


    }
    printf("%d", count);
}

