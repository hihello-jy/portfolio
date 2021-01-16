#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

#define START_X 10
#define START_Y 500
#define BALL_SIZE 50

//*******************************
//�����쿡�� �ܼ� �׷����� ���� ������ �Լ���
HWND hwnd;
HDC hdc;

// �׷����� �ʱ�ȭ �Ѵ�.
void init_graphics(void)
{
	hwnd = GetForegroundWindow();
	hdc = GetWindowDC(hwnd);
}

// ȭ���� �����.
void clear_screen(void)
{
	Rectangle(hdc, 0, 0, 1000, 1000);
}

//Ŀ���� Ư���� ��ġ�� ������.
void gotoxy(int x, int y)
{
	COORD coord = { 0, 0 };
	coord.X = x; coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

//*************************************************************************

int velocity;                          // ���� �ʱ�ӵ�
double angle;                          // ���� �ʱ� ����
int ballVx;                            // ���� ���� x���� �ӵ�
int ballVy;                            // ���� ���� y���� �ӵ�
int ballX;                             // ���� ���� x��ǥ
int ballY;                             // ���� ���� y��ǥ
int shooterX, shooterY;                // �߻�� ���� ��ǥ             



//���� �׸���.
void draw_ball()
{
	Ellipse(hdc, ballX - BALL_SIZE / 2, ballY - BALL_SIZE / 2, ballX + BALL_SIZE / 2, ballY + BALL_SIZE / 2);
}

//�������� �ʱ�ȭ�Ѵ�.
void init(void)
{
	ballVx = (int)(velocity * cos(angle * 3.141592 / 180));
	ballVy = (int)(-velocity * sin(angle * 3.141592 / 180));
	ballX = START_X + ballVx;
	ballY = START_Y + ballVy;
	shooterX = ballX;
	shooterY = ballY;
}

//������ ����� �׸���.
void draw_background(void)
{
	//ȭ���� �����.
	clear_screen();

	//�߻�븦 �׸���.
	MoveToEx(hdc, START_X, START_Y, 0);
	LineTo(hdc, shooterX, shooterY);

	//�ٴڼ��� �׸���.
	MoveToEx(hdc, 10, 500, 0);
	LineTo(hdc, 500, 500);

	//Ÿ���� �׸���.
	Rectangle(hdc, 400, 400, 450, 500);
}

//�޴��� ȭ�鿡 ����Ѵ�.
void print_menu(void)
{
	gotoxy(1, 1);
	printf("z: �߻� ���� ����");
	gotoxy(1, 2);
	printf("x: �߻� ���� ����");
	gotoxy(1, 3);
	printf("c: �߻� �ӵ� ����");
	gotoxy(1, 4);
	printf("v: �߻� �ӵ� ����");
	gotoxy(1, 5);
	printf("s: ���� ����");
	gotoxy(1, 6);
	printf("q: ���� ����");
}

int main(void)
{
	int counter = 0;        //�ݺ� Ƚ��
	int success = 0;        //���� Ƚ��

	init_graphics();

	velocity = 60;          //���� �ʱ� �ӵ�
	angle = 45.0;           //���� �ʱ� ����

	while (1)
	{
		init();                 //���� �ӵ��� ������ �ٽ� ����Ѵ�.
		draw_background();      //����� �׸���.
		draw_ball();            //���� �׸���.

		print_menu();
		int command = _getch();
		switch (command) {
		case 'z':
			angle += 10;
			break;
		case 'x':
			angle -= 10;
			break;
		case 'c':
			velocity += 10;
			break;
		case 'v':
			velocity -= 10;
			break;
		case 'q':
			return 0;
		case 's':
			goto START;
		}
	}

START:
	while (1)
	{
		system("cls");//ȭ���� �����.
		gotoxy(1, 2);
		printf("�ݺ�Ƚ��: %d", counter);
		gotoxy(1, 3);
		printf("���� ��ġ: (%d, %d)", ballX, ballY);
		if (success == 1) {
			gotoxy(1, 1);
			printf("��ǥ���� ���߾����ϴ�. ");
			printf("������ ����Ǿ����ϴ�. ");
			return 0;
		}
		Sleep(300); //��ǻ�͸� 200ms(�и�������) ���� ���ڰ� �Ѵ�.
		ballVy = ballVy + 10; //�߷� ���ӵ��� 10�̶�� �����Ѵ�.
		ballX = ballX + ballVx; //x�� �������� 1�� ���� ���� ������ ��ǥ�� ����Ѵ�.
		ballY = ballY + ballVy; //y�� �������� 1�� ���� ���� ������ ��ǥ�� ����Ѵ�.

		draw_background();
		draw_ball();

		//���� ��ǥ���� �¾�����
		if ((ballX >= 375) && (ballX <= 525) && (ballY >= 375) && (ballY <= 525)) {
			success = 1;
		}
		//���� ��踦 �������
		if (ballY >= 500 || ballY < 0)
			break;
		counter++;
	}
	gotoxy(1, 1);
	printf("������ ����Ǿ����ϴ�. ");
	return 0;
}