#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <iostream>
using namespace std;


pair<int,int> aa[100001];

int cmp(pair<int,int> i, pair<int,int> j)
{
	return i.second < j.second || i.second == j.second && i.first < j.first;
}
int a[100010];
int b[100010];

int main()
{
	int n;
	int sum = 0;
	scanf("%d",&n);
	for(int i = 1; i <= n; i++){
		scanf("%d",&a[i]);
		if(b[i-1]+a[i] >= a[i]){
			b[i] = b[i-1]+a[i];
		}else b[i] = a[i];
	}
	int max = a[1];
	for(int i = 1; i <= n; i++){
		if(max <= b[i]){
			max = b[i];
		}
	
	}
	printf("%d",max);
	
    return 0;
}