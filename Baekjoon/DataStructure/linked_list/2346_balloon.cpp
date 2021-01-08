#include <iostream>
using namespace std;

int n;

class node {
public:
	int index;
	int data;
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
	}
}

node* next_node(int a) {
	if (a > 0) {
		for (int i = 0; i < a; i++) {
			cur_node = cur_node->next;
		}
	}
	else if (a < 0) {
		for (int i = 0; i < -a; i++) {
			cur_node = cur_node->pre;
		}
	}
	return cur_node;
}

void pop_b() {
	while (n!=1) {
		cout << cur_node->index << " ";
		delete_n(cur_node);
		if(n!=1)
			next_node(cur_node->data);
	}
	cout << cur_node->index;
}

int main() {
	cin >> n;
	node* balloon = new node[n];

	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		balloon[i].index = i + 1;
		balloon[i].data = num;
		if (i == n - 1)
			balloon[i].next = &balloon[0];
		else
			balloon[i].next = &balloon[i + 1];

		if (i == 0)
			balloon[i].pre = &balloon[n - 1];
		else
			balloon[i].pre = &balloon[i-1];
	}

	cur_node = &balloon[0];
	pop_b();

	return 0;
}