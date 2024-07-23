#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int honeybox[100001];
int sum[100001];
int n, m = 0;

int main()
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &honeybox[i]);
		sum[i] = sum[i - 1] + honeybox[i];
	}
	for (int i = 2; i < n; i++) {
		// 꿀통을 제일 왼쪽에 뒀을 때
		if (m < sum[n - 1] + sum[i - 1] - honeybox[i]) m = sum[n - 1] + sum[i - 1] - honeybox[i];
		//꿀통을 제일 오른쪽에 뒀을때
		if (m < sum[n] - honeybox[1] + sum[n]  - sum[i] - honeybox[i]) m = sum[n] - honeybox[1] + sum[n] - sum[i] - honeybox[i];
		//꿀통을 중간에 뒀을 때
		if (m < sum[i] - honeybox[1] + sum[n-1] - sum[i-1]) m = sum[i] - honeybox[1] + sum[n - 1] - sum[i - 1];
	}
	printf("%d", m);

	return 0;
}