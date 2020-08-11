#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int a, b, c,date=1;
    cin >> a>>b>>c;
    
    while (1) {

        if (((date - a) % 15 == 0) && ((date - b) % 28 == 0) && ((date - c) % 19 == 0))
            break;

        else
            date++;
    }
    

    printf("%d", date);
}

