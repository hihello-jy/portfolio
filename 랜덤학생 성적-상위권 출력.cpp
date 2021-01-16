#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <cmath>
using namespace std;
string name[100];
int score[100];
int i = 0;

string surname[14] = { "��","��","��","��","��","��","��","��","��","��","��","��","��","Ȳ" };
string famname[19] = { "��","��","��","��","��","��","��","��","��","��","ä","��","��","��","��","��","ä","��","��" };
string a, b, c;

void nameList() {
	srand(time(0));
	
	for (int i = 0; i < 100; i++) { //100���� �̸� �����ϵ��� �Ѵ�.
		int Random = rand() % 14;
		a = surname[Random]; //���� �ϳ� ������ �����Ѵ�.

		int Random2 = rand() % 19; // �̸��� ù��° ���ڸ� ���Ƿ� �����Ѵ�.
		b = famname[Random2];

		int Random3 = rand() % 19; // �̸��� �ι�° ���ڸ� ���Ƿ� �����Ѵ�.
		c = famname[Random3];

		string d = a + b + c; //��Ʈ���� ���ļ� �̸� ��ü�� ������ش�.
		name[i] = d;
	}
}

void scoreList() {
	for (int k = 0; k < 100; k++) {
		int randomNumber = rand() % 100;
		score[k] = randomNumber;
	}
}

void write() {            //��ü �л��� �̸��� ������ ����ϴ� �Լ��� �������ش�.
	cout << "[��� �л� ���]" << endl;
	for (int i = 0; i < 100; i++) {
		cout << "�й�: " << i << "�л� �̸�: " << name[i] << ",����: " << score[i] << endl;
	}
}

double avgCal() {//����� ������ִ� �Լ��� �������ش�.
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

		V = V + ((score[i] - average) * (score[i] - average)); //ǥ������ ���ϱ�

		if (i == 99) {
			double variance = V / 100;
			double e = sqrt(variance);

			return e;
		}
	}
}

void greatStudent() { // ǥ������ + ������� �̻��� �л��� �̸��� ������ ����ϴ� �Լ� ����
	cout << "[��� �л� ���]" << endl;
	cout << "ǥ������ + ������� = " << avgCal() + standard() << endl;
	for (int i = 0; i < 100; i++) {
		if (score[i] >= avgCal() + standard()) {
			cout << "�й�: " << i << ", " << name[i] << ": " << score[i] << endl;
		}
	}
}

int main() //������ ������ �Լ��� ȣ���Ѵ�.
{
	nameList();
	scoreList();
	write();
	cout << "������� = " << avgCal() << endl;
	cout << "ǥ������ = " << standard() << endl;
	greatStudent();
}