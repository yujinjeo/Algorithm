#include <stdlib.h>
#include <stdio.h>
int tri[501][501];

int max(int a, int b){
  return a>b?a:b;
}

int main(){
  int n;
  scanf("%d",&n);

  for(int i=1; i<=n; i++){
    for(int j=1; j<=i; j++){
      scanf("%d",&tri[i][j]);
    }
  }

  int answer=0;
  
  for(int i=1; i<=n; i++){
    for (int j=1; j<=i; j++){
      tri[i][j]+=max(tri[i-1][j-1], tri[i-1][j]);
      answer=max(answer,tri[i][j]);
    }
  }
  printf("%d",answer);
  
  return 0; 
}