

#include <iostream>
#include <algorithm>
using namespace std;


int gcd(int a, int b)

{

    if (a % b == 0)

        return b;



    return gcd(b, a % b);

}

int lcm(int a, int b)

{

    return (a * b) / gcd(a, b);

}


int main()
{      

    int n;
    cin >> n;
    while (n--) {
        int c, m, n, x, y;
        cin >> m >> n>>x>>y;
        c = lcm(m, n);

        while (1) {
            if (x == y) {

                printf("%d\n", x);
                break;

            }

            else if (x > y) {
                y = y + n;
            }
            else if (y > x) {
                x = x + m;
            }

            if ((x > c) || (y > c)) {
                printf("-1");
                break;
            }
        }

       
    }
}
