'''Реалізація однозв'язного списку
Почнемо з реалізації основних структур для однозв'язного списку.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
     
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")

def reverse_linked_list(llist):
    '''Функція реверсування однозв'язного списку
    Тепер напишемо функцію для реверсування однозв'язного списку.'''
    prev = None
    curr = llist.head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    llist.head = prev

def merge_sorted_lists(l1, l2):
    '''Алгоритм сортування для однозв'язного списку
    Напишемо алгоритм сортування злиттям для однозв'язного списку.'''
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next

def merge_sort_linked_list(head):
    '''Алгоритм сортування для однозв'язного списку
    Напишемо алгоритм сортування злиттям для однозв'язного списку.'''
    if not head or not head.next:
        return head

    def split(head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return head, slow

    def merge(l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    left, right = split(head)
    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)
    return merge(left, right)

def merge_two_sorted_lists(l1, l2):
    '''Функція для об'єднання двох відсортованих однозв'язних списків'''
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

#Приклад використання

# Створення першого списку
llist1 = LinkedList()
llist1.append(1)
llist1.append(4)
llist1.append(5)

# Створення другого списку
llist2 = LinkedList()
llist2.append(1)
llist2.append(3)
llist2.append(4)

# Друк початкових списків
print("Список 1:")
llist1.print_list()
print("Список 2:")
llist2.print_list()

# Об'єднання двох відсортованих списків
merged_head = merge_two_sorted_lists(llist1.head, llist2.head)
merged_list = LinkedList()
merged_list.head = merged_head

print("Об'єднаний відсортований список:")
merged_list.print_list()

# Реверсування об'єднаного списку
reverse_linked_list(merged_list)
print("Реверсований об'єднаний список:")
merged_list.print_list()

# Сортування списку злиттям
sorted_head = merge_sort_linked_list(merged_list.head)
sorted_list = LinkedList()
sorted_list.head = sorted_head

print("Відсортований реверсований список:")
sorted_list.print_list()
