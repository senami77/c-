#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()

{
	srand((unsigned int)time(NULL));
	printf("�� �ָӴϿ� �ִ� ����");
	int myMoney = (rand() % 10 + 1) * 1000;
	printf("%d���̴�.\n", myMoney);
	int coin500 = rand() % 4 * 500;
	int coin100 = rand() % 5000;
	coin100 = coin100 / 100 * 100;
	printf("�׸��� ������ ������");
	printf("%d���̴�.", coin500 + coin100);
	printf("\n���� ���ڸ� �� �� ������?");

	return 0;
}