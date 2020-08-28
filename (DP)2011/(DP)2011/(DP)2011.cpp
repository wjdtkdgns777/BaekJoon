#include <stdio.h>
#include <string.h>
int main()
{
	int d[5001] = { 1, };
	char a[5002];
	scanf("%s", a + 1);
	int n = strlen(a + 1);
	for (int i = 1; i <= n; i++)
	{
		int x = a[i] - '0', y = a[i - 1] - '0';
		if (1 <= x && x <= 9) d[i] =  d[i - 1] % 1000000;
		if (10 <= 10 * y + x && 10 * y + x <= 26) d[i] = (d[i] + d[i - 2]) % 1000000;
	}
	printf("%d", d[n]);
}