#include<iostream>
using namespace std;
int main() {
	int maxv = 0, minv = 100;
	int n;
	int i;

	for (n = 1; n <= 10; n++) {
		cin >> i;
		if (0 <= i and i <= 100)

			//0�� 100 ���̿��� �ּڰ��� �Է¼��ں��� Ŭ ��, 
			//�ִ밪�� �Է¼��ں��� ���� ���� ���մϴ�.
		{
			if (minv > i) {
				minv = i;
			}

			if (maxv < i) {
				maxv = i;
			}
		}
		while (i < 0 or i>100) {
			cout << "0�̻� 100������ ���ڸ� �Է��Ͻÿ�";
			cin >> i;
			if (0 <= i and i <= 100) {
				if (minv > i) {
					minv = i;
				}
				if (maxv < i) {
					maxv = i;
				}
			}		
		}
	}
	cout << "�ּڰ�" << minv << "�ִ�" << maxv;
}