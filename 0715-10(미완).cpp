#include <stdio.h>

int main() {

	int coin;
	printf("���� �Է����ּ���.(��)");
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
	printf("������� %d��, ", coin500);
	printf("����� %d��, ", coin100);
	printf("���ʿ��� %d��, ", coin50);
	printf("�ʿ��� %d��, ", coin10);

	return 0;
}