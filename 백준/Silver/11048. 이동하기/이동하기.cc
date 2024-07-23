#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int map[1001][1001];
int dp[1001][1001];

int n, x, y;
int mm(int i, int j, int k) {
    if (i < j) i = j;
    if (i < k) i = k;
    return i;
}

int main()
{
    scanf("%d%d", &x, &y);
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++) {
            scanf("%d", &map[i][j]);
        }
    }
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++) {
            dp[i][j] = mm(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + map[i][j];
        }
    }
    printf("%d", dp[x][y]);

    return 0;
}