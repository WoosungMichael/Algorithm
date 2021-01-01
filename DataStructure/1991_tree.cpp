#include <iostream>
#include <vector>
using namespace std;

vector<vector<char>> v;

void preorder(char a) {
	if (a == '.')
		return;
	cout << v[a-'A'][0];
	preorder(v[a - 'A'][1]);
	preorder(v[a - 'A'][2]);
}

void inorder(char a) {
	if (a == '.')
		return;
	inorder(v[a - 'A'][1]);
	cout << v[a - 'A'][0];
	inorder(v[a - 'A'][2]);
}

void postorder(char a) {
	if (a == '.')
		return;
	postorder(v[a - 'A'][1]);
	postorder(v[a - 'A'][2]);
	cout << v[a - 'A'][0];
}

int main() {
	int n;
	cin >> n;
	v.assign(n, vector<char>(3,'.'));

	for (int i = 0; i < n; i++) {
		char a, b, c;
		cin >> a >> b >> c;

		v[a - 'A'][0] = a;
		v[a - 'A'][1] = b;
		v[a - 'A'][2] = c;
	}

	preorder('A'); 
	cout << endl;
	
	inorder('A');
	cout << endl;
	
	postorder('A');
	cout << endl;
}