#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

#define START_X 10
#define START_Y 500
#define BALL_SIZE 50

//*******************************
//윈도우에서 콘솔 그래픽을 위한 변수와 함수들
HWND hwnd;
HDC hdc;

// 그래픽을 초기화 한다.
void init_graphics(void)
{
	hwnd = GetForegroundWindow();
	hdc = GetWindowDC(hwnd);
}

// 화면을 지운다.
void clear_screen(void)
{
	Rectangle(hdc, 0, 0, 1000, 1000);
}

//커서를 특정한 위치로 보낸다.
void gotoxy(int x, int y)
{
	COORD coord = { 0, 0 };
	coord.X = x; coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

//*************************************************************************

int velocity;                          // 공의 초기속도
double angle;                          // 공의 초기 각도
int ballVx;                            // 공의 현재 x방향 속도
int ballVy;                            // 공의 현재 y방향 속도
int ballX;                             // 공의 현재 x좌표
int ballY;                             // 공의 현재 y좌표
int shooterX, shooterY;                // 발사대 끝의 좌표             



//볼을 그린다.
void draw_ball()
{
	Ellipse(hdc, ballX - BALL_SIZE / 2, ballY - BALL_SIZE / 2, ballX + BALL_SIZE / 2, ballY + BALL_SIZE / 2);
}

//변수들을 초기화한다.
void init(void)
{
	ballVx = (int)(velocity * cos(angle * 3.141592 / 180));
	ballVy = (int)(-velocity * sin(angle * 3.141592 / 180));
	ballX = START_X + ballVx;
	ballY = START_Y + ballVy;
	shooterX = ballX;
	shooterY = ballY;
}

//게임의 배경을 그린다.
void draw_background(void)
{
	//화면을 지운다.
	clear_screen();

	//발사대를 그린다.
	MoveToEx(hdc, START_X, START_Y, 0);
	LineTo(hdc, shooterX, shooterY);

	//바닥선을 그린다.
	MoveToEx(hdc, 10, 500, 0);
	LineTo(hdc, 500, 500);

	//타깃을 그린다.
	Rectangle(hdc, 400, 400, 450, 500);
}

//메뉴를 화면에 출력한다.
void print_menu(void)
{
	gotoxy(1, 1);
	printf("z: 발사 각도 증가");
	gotoxy(1, 2);
	printf("x: 발사 각도 감소");
	gotoxy(1, 3);
	printf("c: 발사 속도 증가");
	gotoxy(1, 4);
	printf("v: 발사 속도 감소");
	gotoxy(1, 5);
	printf("s: 게임 시작");
	gotoxy(1, 6);
	printf("q: 게임 종료");
}

int main(void)
{
	int counter = 0;        //반복 횟수
	int success = 0;        //성공 횟수

	init_graphics();

	velocity = 60;          //공의 초기 속도
	angle = 45.0;           //공의 초기 각도

	while (1)
	{
		init();                 //현재 속도와 각도로 다시 계산한다.
		draw_background();      //배경을 그린다.
		draw_ball();            //공을 그린다.

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
		system("cls");//화면을 지운다.
		gotoxy(1, 2);
		printf("반복횟수: %d", counter);
		gotoxy(1, 3);
		printf("공의 위치: (%d, %d)", ballX, ballY);
		if (success == 1) {
			gotoxy(1, 1);
			printf("목표물을 맞추었습니다. ");
			printf("게임이 종료되었습니다. ");
			return 0;
		}
		Sleep(300); //컴퓨터를 200ms(밀리세컨드) 동안 잠자게 한다.
		ballVy = ballVy + 10; //중력 가속도를 10이라고 가정한다.
		ballX = ballX + ballVx; //x축 방향으로 1초 동안 공이 움직인 좌표를 계산한다.
		ballY = ballY + ballVy; //y축 방향으로 1초 동안 공이 움직인 좌표를 계산한다.

		draw_background();
		draw_ball();

		//공이 목표물에 맞았으면
		if ((ballX >= 375) && (ballX <= 525) && (ballY >= 375) && (ballY <= 525)) {
			success = 1;
		}
		//공이 경계를 벗어났으면
		if (ballY >= 500 || ballY < 0)
			break;
		counter++;
	}
	gotoxy(1, 1);
	printf("게임이 종료되었습니다. ");
	return 0;
}