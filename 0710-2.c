#include <stdio.h>

int main()
{
	int radius = 5;

	float Pi = 3.14;

	float area = radius * radius * Pi; 

	float girth = radius * 2* Pi;

	printf("원의 넓이:%.2f", area);
	printf("원의 둘레:%.2f", girth);

	return 0;
}
