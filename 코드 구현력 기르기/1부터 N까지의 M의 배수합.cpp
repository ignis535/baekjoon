#include <iostream>
using namespace std;

int main(void){
	int n, m;
	
	cin >> n >> m;
	int sum = 0;
	for(int i = 1; i <= n; i++){
		if(i % m == 0) sum += i;
	}
	
	cout << sum;
	return 0;	
}
