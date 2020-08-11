#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int n, hap = 1;

void solve()
{
    int i, j, count = 1;
   
    for (i = 0; i < n; i++) {
        count = 1;
        for (j = 0; j < n - 1; j++) {
         
            
            if (arr[i][j] == arr[i][j + 1]) {
                count++;
                if (count > hap) {
                    hap = count;
                }
            }
            else if (arr[i][j] != arr[i][j + 1]) {
                count = 1;
            }

        }
    }
    count = 1;
    for (j = 0; j < n; j++) {
        count = 1;
        for (i = 0; i < n - 1; i++) {


            if (arr[i][j] == arr[i + 1][j]) {
                count++;
                if (count > hap) {
                    hap = count;
                }
            }
            else if (arr[i][j] != arr[i + 1][j])
                count = 1;

        }
    }

    
}

int main()
{
    int i,j;
    int count = 1;
    
    cin >> n;
    vector<char> a(n);


    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            cin >> arr[i][j];

        }
    }


    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {

            solve();
            

            if (i + 1 < n) {
                swap(arr[i][j], arr[i + 1][j]);
                solve();
                swap(arr[i][j], arr[i + 1][j]);
            }
            
            

            if (j + 1 < n) {
                swap(arr[i][j], arr[i][j+1]);
                solve();
                swap(arr[i][j], arr[i][j + 1]);
            }
            
           

        }
    }
    printf("%d", hap);
}
