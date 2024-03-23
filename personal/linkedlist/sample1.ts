class node<T> {
	public data: T;
	public next: node<T>; //think of this as the next node

	constructor(givenData: T) {
		this.data = givenData; //convection says you name givenData just as data
	}
}

class linkedList<T> {
	head: node<T> | null;
	size: number;

	constructor() {
		this.head = null;
		this.size = 0;
	}

	add(data: T) {
		const newNode = new node(data);

		if (!this.head) {
			this.head = newNode;
		} else {
			let current: node<T> = this.head;
			while (current.next) {
				current = current.next;
			}
			current.next = newNode;
		}
		this.countNodes(this.head);
	}

	countNodes(head: node<T>) {
		if (head) {
			let count: number = 0;
			let current: node<T> = head;
			while (current.next) {
				console.log(current.data);
				current = current.next;
				count++;
			}
		} else {
			return 0;
		}
	}
}

let linkedlist = new linkedList();
linkedlist.add(2);
console.log("read");
