#include <stdio.h>

int main()
{
	int radius = 5;

	float Pi = 3.14;

	float area = radius * radius * Pi; 

	float girth = radius * 2*Pi;

	printf("���� ����:%.2f", area);
	printf("���� �ѷ�:%.2f", girth);

	return 0;
}