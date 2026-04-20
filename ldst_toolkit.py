#Assignment 2
#LDST Toolkit


'''Name of the School: School of Engineering & Technology
Program (Class / Semester / Batch): B.Tech CSE (AI & ML) , 2nd semester, 2025-29
Course Title: Data Structures
Course Code: ETCCDS202
Unit Number: 2
Unit Title: Linear Data Structures
Student Name: SWATI SINGH
Roll No: 2501730269
Section: A'''




# Task 1: Dynamic Array
class DynamicArray:
    def __init__(self, capacity=2):
        self.size, self.capacity = 0, capacity
        self.array = [None] * capacity

    def append(self, x):
        if self.size == self.capacity:
            print(f"[Resize]: {self.capacity} -> {self.capacity * 2}")
            new_arr = [None] * (self.capacity * 2)
            new_arr[:self.size] = self.array
            self.array, self.capacity = new_arr, self.capacity * 2
        self.array[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0: return None
        self.size -= 1
        return self.array[self.size]

    def __str__(self):
        return f"Array: {self.array[:self.size]} (Size: {self.size}, Cap: {self.capacity})"



# Task 2: Linked Lists
class Node:
    def __init__(self, data, next_node=None):
        self.data, self.next = data, next_node

class DNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data, self.next, self.prev = data, next_node, prev_node

class SinglyLinkedList:
    def __init__(self): self.head = None
    
    def insert_at_beginning(self, x): self.head = Node(x, self.head)
    
    def insert_at_end(self, x):
        if not self.head: 
            self.head = Node(x)
            return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = Node(x)

    def delete_by_value(self, x):
        curr, prev = self.head, None
        while curr and curr.data != x:
            prev, curr = curr, curr.next
        if curr:
            if prev: prev.next = curr.next
            else: self.head = curr.next

    def traverse(self):
        res, curr = [], self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(res) if res else "Empty List")

class DoublyLinkedList:
    def __init__(self): self.head = None

    def insert_at_end(self, x):
        if not self.head:
            self.head = DNode(x)
            return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = DNode(x, None, curr)

    def insert_after_node(self, target, x):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if curr:
            new_node = DNode(x, curr.next, curr)
            if curr.next: curr.next.prev = new_node
            curr.next = new_node

    def delete_at_position(self, pos):
        if not self.head: return
        curr = self.head

        if pos == 0:
            self.head = curr.next
            if self.head: self.head.prev = None
            return

        for _ in range(pos):
            if not curr: return
            curr = curr.next

        if curr:
            if curr.next: curr.next.prev = curr.prev
            if curr.prev: curr.prev.next = curr.next

    def traverse(self):
        res, curr = [], self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        print(" <-> ".join(res) if res else "Empty List")



# Task 3: Stack & Queue
class Stack:
    def __init__(self): self.storage = SinglyLinkedList()

    def push(self, x): self.storage.insert_at_beginning(x)

    def pop(self):
        if not self.storage.head: return None
        val = self.storage.head.data
        self.storage.head = self.storage.head.next   # O(1) optimized
        return val

    def peek(self):
        return self.storage.head.data if self.storage.head else None

class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def dequeue(self):
        if not self.head: return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):   
        return self.head.data if self.head else None




# Task 4: Application
def is_balanced(expr):
    s = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in pairs.values():
            s.push(char)
        elif char in pairs:
            if s.pop() != pairs[char]:
                return False
    return s.peek() is None




# --- Main Test Runner ---
if __name__ == "__main__":
    print("--- TASK 1: DYNAMIC ARRAY ---")
    da = DynamicArray(2)
    for i in range(1, 11): da.append(i)
    print(da)
    print("Popped:", [da.pop() for _ in range(3)])

    print("\n--- TASK 2A: SINGLY LINKED LIST ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_end(3)
    print("After inserts:")
    sll.traverse()
    sll.delete_by_value(3)
    print("After deleting 3:")
    sll.traverse()

    print("\n--- TASK 2B: DOUBLY LINKED LIST ---")
    dll = DoublyLinkedList()
    for x in [10, 20, 30]:
        dll.insert_at_end(x)
    dll.insert_after_node(20, 25)
    print("After insert 25 after 20:")
    dll.traverse()
    dll.delete_at_position(1)
    print("After deleting position 1 (20):")
    dll.traverse()
    dll.delete_at_position(2)  
    print("After deleting last position:")
    dll.traverse()

    print("\n--- TASK 3: STACK & QUEUE ---")
    stk, que = Stack(), Queue()
    stk.push("A")
    stk.push("B")
    print(f"Stack Pop: {stk.pop()} | Peek: {stk.peek()}")

    que.enqueue("X")
    que.enqueue("Y")
    print(f"Queue Dequeue: {que.dequeue()} | Next: {que.dequeue()}")

    que.enqueue("Z")
    print(f"Queue Front: {que.front()}")  

    print("\n--- TASK 4: BALANCED PARENTHESES ---")
    for t in ["([])", "([)]", "(((", ""]:   
        print(f"'{t}' -> {is_balanced(t)}")
