from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.cnt = 0

    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.cnt += 1

    def dequeue(self):
        if self.front is None:
            return -1
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        self.cnt -= 1
        return node.data

    def get_front(self):
        return self.front.data if self.front else -1

    def get_rear(self):
        return self.rear.data if self.rear else -1

    def is_empty(self):
        return 1 if self.front is None else 0


if __name__ == "__main__":
    q = Queue()
    for i in range(int(input())):
        command = input().rstrip()
        if command[:4] == "push":
            c, n = command.split()
            q.enqueue(n)
        elif command == "pop":
            print(q.dequeue())
        elif command == "front":
            print(q.get_front())
        elif command == "back":
            print(q.get_rear())
        elif command == "size":
            print(q.cnt)
        elif command == "empty":
            print(q.is_empty())

