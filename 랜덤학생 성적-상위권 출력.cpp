#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <cmath>
using namespace std;
string name[100];
int score[100];
int i = 0;

string surname[14] = { "김","이","박","최","조","정","강","신","민","백","양","육","한","황" };
string famname[19] = { "예","송","연","도","사","혜","진","유","연","윤","채","현","주","준","영","이","채","서","소" };
string a, b, c;

void nameList() {
	srand(time(0));
	
	for (int i = 0; i < 100; i++) { //100명의 이름 생성하도록 한다.
		int Random = rand() % 14;
		a = surname[Random]; //성을 하나 임으로 생성한다.

		int Random2 = rand() % 19; // 이름의 첫번째 글자를 임의로 생성한다.
		b = famname[Random2];

		int Random3 = rand() % 19; // 이름의 두번째 글자를 임의로 생성한다.
		c = famname[Random3];

		string d = a + b + c; //스트링을 합쳐서 이름 전체를 만들어준다.
		name[i] = d;
	}
}

void scoreList() {
	for (int k = 0; k < 100; k++) {
		int randomNumber = rand() % 100;
		score[k] = randomNumber;
	}
}

void write() {            //전체 학생의 이름과 성적을 출력하는 함수를 정의해준다.
	cout << "[모든 학생 명단]" << endl;
	for (int i = 0; i < 100; i++) {
		cout << "학번: " << i << "학생 이름: " << name[i] << ",성적: " << score[i] << endl;
	}
}

double avgCal() {//평균을 계산해주는 함수를 정의해준다.
	double average, sum = 0;
	for (int i = 0; i < 100; i++)
	{
		sum = sum + score[i];
		average = (double)sum / 100;
	}

	return average;
}

double standard() {
	double sum = 0;
	double V = 0;
	double average = avgCal();
	for (int i = 0; i < 100; i++)
	{
		sum = sum + score[i];

		V = V + ((score[i] - average) * (score[i] - average)); //표준편차 구하기

		if (i == 99) {
			double variance = V / 100;
			double e = sqrt(variance);

			return e;
		}
	}
}

void greatStudent() { // 표준편차 + 평균점수 이상인 학생의 이름과 성적을 출력하는 함수 정의
	cout << "[우수 학생 명단]" << endl;
	cout << "표준편차 + 평균점수 = " << avgCal() + standard() << endl;
	for (int i = 0; i < 100; i++) {
		if (score[i] >= avgCal() + standard()) {
			cout << "학번: " << i << ", " << name[i] << ": " << score[i] << endl;
		}
	}
}

int main() //위에서 정의한 함수를 호출한다.
{
	nameList();
	scoreList();
	write();
	cout << "평균점수 = " << avgCal() << endl;
	cout << "표준편차 = " << standard() << endl;
	greatStudent();
}