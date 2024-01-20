#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <iostream>
using namespace std;
int MAX(int x, int y) {
	if (x > y) return x;
	else return y;
}
char a[101][101];
char st[100];
int dp[101][101][101];
int cmp(pair<int,int> i, pair<int,int> j)
{
	return i.second < j.second || i.second == j.second && i.first < j.first;
}


int main()
{
	int n,m,w;

	scanf("%d%d%d", &n, &m, &w);
	for (int i = 0; i < n; i++) {
		scanf("%s", a[i]);
	}
	scanf("%s", &st);
	for (int j = 0; j < n; j++) {
		for (int k = 0; k < m; k++) {
			if (st[0] == a[j][k]) dp[0][j][k]++;
		}
	}
	for (int i = 1; i < strlen(st); i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				if (dp[i - 1][j][k] > 0) {
					for (int x = 1; x <= w; x++) {
						if (j + x < n && a[j + x][k] == st[i]) {
							dp[i][j + x][k] += dp[i - 1][j][k];
						}
						if (k + x < m && a[j][k + x] == st[i]) {
							dp[i][j][k + x] += dp[i - 1][j][k];
						}
						if (j - x >= 0 && a[j - x][k] == st[i]) {
							dp[i][j - x][k] += dp[i - 1][j][k];
						}
						if (k - x >= 0 && a[j][k - x] == st[i]) {
							dp[i][j][k - x] += dp[i - 1][j][k];
						}
					}
				}
			}
		}
	}
	int sum = 0;
	for (int j = 0; j < n; j++) {
		for (int k = 0; k < m; k++) {
			sum += dp[strlen(st) - 1][j][k];
		}
	}
	printf("%d", sum);
	return 0;
}