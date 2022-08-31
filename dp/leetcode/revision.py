def rev_arr(arr, n):
    if n == 0:
        return []
    return [arr[n-1]] + rev_arr(arr, n-1)


def rev_arr2(arr):
    if not arr:
        return []
    return [arr.pop()] + rev_arr2(arr)


def rev_str(s, n):
    if n == 0:
        return ""
    return s[n-1] + rev_str(s, n-1)


def ispallindrome(s):
    n = len(s)

    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True


def bsearch(arr, x):
    low = 0
    high = len(arr) - 1

    while(low<=high):
        mid = (low+high)//2
        mid_element = arr[mid]

        if mid_element < x:
            low = mid + 1
        elif mid_element > x:
            high = mid - 1
        else:
            return True
    return False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = node
        else:
            self.head = node

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def print_decorator(fn):
    def wrapper(*args, **kwrags):
        print('start')
        fn(*args, **kwrags)
        print('end')
    return wrapper

@print_decorator
def hello(x, y):
    print('hello world', x+y)
#arr = [1, 2, 3, 4, 5]
#print(rev_arr(arr, 5))
#print(rev_arr2(arr))
#print(rev_str("hello", 5))
#print(ispallindrome("abccb"))
#print(bsearch(arr, 6))

# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.insert(2)
# ll.printLL()
# arr = [2, 7, 1, 5, 3, 4, 6]
# bubblesort(arr)
# print(arr)
hello(2, 3)
