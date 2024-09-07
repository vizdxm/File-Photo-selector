#include <bits/stdc++.h>
using namespace std;

string tostring(int x) {
	string r = "0000";
	r[0] = x/1000 + '0';
	x%=1000;
	r[1] = x/100 + '0';
	x%=100;
	r[2] = x/10 + '0';
	x%=10;
	r[3] = x + '0';
	return r;
}

int main () {
	vector <string> v;
	string ori,des,dom;
	cout << "enter domain ";
	cin >> dom;
	cout << "enter destination ";
	cin >> des;
	string a; cin >> a;
	while(a!="0") {
		//cout << tostring(a);
		v.push_back(a);
		cin >> a;
	}
	
	for(int i=0;i<v.size();i++) {
		cout<< "copy " << v[i] << " " << des << "\n";
	}
}
