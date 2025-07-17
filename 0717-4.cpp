#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()

{
	srand((unsigned int)time(NULL));
	printf("내 주머니에 있는 돈은");
	int myMoney = (rand() % 10 + 1) * 1000;
	printf("%d원이다.\n", myMoney);
	int coin500 = rand() % 4 * 500;
	int coin100 = rand() % 5000;
	coin100 = coin100 / 100 * 100;
	printf("그리고 과자의 가격은");
	printf("%d원이다.", coin500 + coin100);
	printf("\n나는 과자를 살 수 있을까?");

	return 0;
}