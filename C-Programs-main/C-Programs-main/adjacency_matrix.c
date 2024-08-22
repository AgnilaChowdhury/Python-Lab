#include <stdio.h>

int main() {
   
   int i,j,v,w;
    printf("Enter the no. of vertexes\n");
    scanf("%d",&v);

    int graph[v][v];
    char vertex[v];
    
     for (i = 0; i < v; i++) {
        for (j = 0; j < v; j++) {
            graph[i][j] = 0;
        }
    }
    
    
    printf("Enter the vertexes\n");
    for(i=0;i<v;i++)
        scanf(" %c", &vertex[i]);
    
    enum enum_vertex{P,Q,R,S,T,U};

    
    printf("Enter the adjacent vertexes and weights(give negative weight for a dummy vertex to exit)\n");
  
    for(i=0;i<v;i++)
    {
         char adj_vertex;
    do{
        printf("Enter the adjacent vertexes of %c and its corresponding weights \n",vertex[i]);
        char v;
        scanf(" %c",&adj_vertex);
       
        scanf("%d",&w);
        if (w < 0) 
                break;

        enum enum_vertex c=adj_vertex - 'P' + 1;;
        graph[i][c-1]=w;
    }while(w>0);
    }
  
   printf("Adjacency Matrix:\n");
    printf("   ");
    for (int i = 0; i < v; i++) {
        printf("%c ", vertex[i]);
    }
    printf("\n");
    for (int i = 0; i < v; i++) {
        printf("%c ", vertex[i]);
        for (int j = 0; j < v; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
    return 0;
}