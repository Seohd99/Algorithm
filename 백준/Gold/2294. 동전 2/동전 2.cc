#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int n,k,coin;
int cnt = 0;
int dp[10001];
int main()
{
	
	scanf("%d%d",&n,&k);
	for(int i = 1; i <= k; i++){
		dp[i] = -1;
	}
	for(int i = 0; i < n; i++){
		scanf("%d",&coin);
		for(int j = coin; j <= k; j++){
			if(dp[j-coin] != -1){
				if(dp[j] != -1)	dp[j] = min(dp[j-coin] + 1,dp[j]);
				else dp[j] = dp[j-coin]+1;
			}
		}
	}
	printf("%d",dp[k]);
	return 0;
}