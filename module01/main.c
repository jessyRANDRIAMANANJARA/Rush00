#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int N;
    int i = 0;
    scanf("%d", &N);
    while (i++ < N)
    {
        if(i % 5 == 0)
        {
            if (i % 7 == 0)
                printf("FooBar\n");
            else
                printf ("Foo\n");
        }
        else if (i % 7 == 0)
            printf("Bar\n");
        
        else
            printf("%d\n", i);
        // i++;
    }
    return 0;
}