#include <stdio.h>

int main() {

	int coin;
	printf("돈을 입력해주세요.(원)");
	scanf("%d", &coin);

	/*int coin1000 = coin / 1000;*/
	int coin500 = coin / 500;
	coin = coin % 500;
	int coin100 = coin / 100;
	coin = coin % 100;
	int coin50 = coin / 50;
	coin = coin % 50;
	int coin10 = coin / 10;
	coin = coin % 10;
	printf("오백원권 %d개, ", coin500);
	printf("백원권 %d개, ", coin100);
	printf("오십원권 %d개, ", coin50);
	printf("십원권 %d개, ", coin10);

	return 0;
}