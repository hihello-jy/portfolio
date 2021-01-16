#include<iostream>
using namespace std;
int main() {
	int maxv = 0, minv = 100;
	int n;
	int i;

	for (n = 1; n <= 10; n++) {
		cin >> i;
		if (0 <= i and i <= 100)

			//0과 100 사이에서 최솟값이 입력숫자보다 클 때, 
			//최대값이 입력숫자보다 작을 때를 비교합니다.
		{
			if (minv > i) {
				minv = i;
			}

			if (maxv < i) {
				maxv = i;
			}
		}
		while (i < 0 or i>100) {
			cout << "0이상 100이하의 숫자를 입력하시오";
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
	cout << "최솟값" << minv << "최댓값" << maxv;
}