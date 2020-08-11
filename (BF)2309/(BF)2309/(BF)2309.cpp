#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

	int arr[10],result=0;

	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
		result += arr[i];
	}
	sort(arr, arr + 9);
	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			if ((result - arr[i] - arr[j]) == 100) {

				for (int k = 0; k < 9; k++) {


					if ((k != i) && (k != j)) {

						printf("%d\n", arr[k]);
					}
					

				}

				return 0;
			}

		}

	}
	return 0;
}