#include <iostream>
using namespace std;

int n, m;

class node {
public:
	int index;
	node* pre;
	node* next;
};

node* cur_node;

void delete_n(node* a) {
	n--;
	if (n == 1) {
		cur_node = a->next;
		a->pre->next = NULL;
		a->next->pre = NULL;
	}
	else {
		a->pre->next = a->next;
		a->next->pre = a->pre;
		cur_node = a->next;
	}
}

node* next_node() {
	for (int i = 0; i < m-1; i++) {
		cur_node = cur_node->next;
	}
	return cur_node;
}

void pop_b() {
	cout << "<";
	while (n!=1) {
		cout << cur_node->index << ", ";
		delete_n(cur_node);
		if(n!=1)
			next_node();
	}
	cout << cur_node->index << ">";
}

int main() {
	cin >> n >> m;
	node* num = new node[n];
	for (int i = 0; i < n; i++) {
		num[i].index = i + 1;
		if (i == n - 1)
			num[i].next = &num[0];
		else
			num[i].next = &num[i + 1];

		if (i == 0)
			num[i].pre = &num[n - 1];
		else
			num[i].pre = &num[i - 1];
	}

	cur_node = &num[m-1];
	pop_b();

	return 0;
}