#include <stdio.h>
#include <stdlib.h>


typedef unsigned long long int li;

int init(li ***T, int N){

  *T=(li**)malloc((N+1)*sizeof(li*));
  if(*T==NULL){
    printf("Error occured!\n");
    return -1 ;
  }
  for(int i = 0; i <= N; i++){
    (*T)[i]=(li*)malloc(sizeof(li)*(N+1));
    if((*T)[i]==NULL){
      printf("Error occured!\n");
      return -1 ;
    }
  }
  return 1;
}

li count (li **T, int N){

  T[0][0] = 1;

  T[1][1] = 1;

  for(int n=0 ; n<=N ; n++){
    for(int h=0; h<=N ; h++){
     
      if( (h>n) || (h==0 && h!=n) || (h==1 && h!=n) ){
        T[n][h] = 0;
      }

     
      if(n>=h && h>1){
        li sum=0;
        for(int l=1; l<=n; l++){
        
          sum += T[l-1][h-1] * T[n-l][h-1] +    
          T[l-1][h-1]* T[n-l][h-2] +            
          T[l-1][h-2]* T[n-l][h-1];             

        }
        T[n][h] = sum;

      }
    }
  }

  li retval=0;
  for(int i=0; i<=N; i++){
    retval+=T[N][i];
  }

  return retval;
}

int main(){
  int N;
  printf("Give the number of keys: ");
  scanf("%d", &N);
  putchar('\n');
  if( N < 0) return 1;
  li **T;
  int success=init(&T, N);

  if(success==-1){
    printf("A exiting!\n");
    return -1;
  }


  printf("from %d keys there are %d different AVL trees\n",N,count(T,N));


  //#define MATRIXOSAN
  //for smaller Ns, we can print out to result to console by removing the comment from the previous line
 
  #ifdef MATRIXOSAN
  printf("Do you want to see the result as matrix? (y/n)\n");
  char choice;
  int valid=0;
  while(!valid){
    scanf("%c", &choice);
    if(choice=='y'){

      
      for(int i=0; i<=N; i++){
        for(int j=0; j<=N; j++){
          printf("%li\t", T[i][j]);
        }
        putchar('\n');
      }
        valid=1;
      }else if(choice =='n'){
          break;
      }
    }
    #endif

    //free the allocated memory
    for(int i = 0; i < N; i++)
        free(T[i]);
    free(T);

  return 0;
}
