
# In[4]:


#Delete the elements in an linked list whose sum is equal to zero
def delete_zero_sum(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    sum_map = {}
    curr = dummy

    while curr:
        prefix_sum += curr.val

        if prefix_sum in sum_map:
            prev = sum_map[prefix_sum]
            prev.next = curr.next

            # Remove nodes with zero sum in between
            while prev != curr:
                prev = prev.next
                del sum_map[prefix_sum]

            curr = prev
        else:
            sum_map[prefix_sum] = curr

        curr = curr.next

    return dummy.next

#Reverse a linked list in groups of a given size:
def reverse_linked_list_groups(head, k):
    curr = head
    prev = None
    next_node = None
    count = 0

    # Reverse the current group
    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1

    # Recursive call for the remaining list
    if next_node:
        head.next = reverse_linked_list_groups(next_node, k)

    return prev

#Merge a linked list into another linked list at alternate positions:

def merge_alternate_positions(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        next1 = curr1.next
        next2 = curr2.next

        curr1.next = curr2
        curr2.next = next1

        curr1 = next1
        curr2 = next2

    if curr2:
        curr1.next = curr2

    return head1

#Count pairs with a given sum in an array:

def count_pairs_with_sum(arr, target):
    count = 0
    num_map = {}

    for num in arr:
        complement = target - num
        count += num_map.get(complement, 0)
        num_map[num] = num_map.get(num, 0) + 1

    return count

#Find duplicates in an array:
def find_duplicates(arr):
    duplicates = []
    num_map = {}

    for num in arr:
        if num in num_map:
            duplicates.append(num)
        else:
            num_map[num] = 1

    return duplicates

#Find the Kth largest and Kth smallest number in an array:

import heapq

def find_kth_largest_smallest(arr, k):
    min_heap = []
    max_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return heapq.heappop(max_heap), heapq.heappop(min_heap)

#Move all negative elements to one side of the array:

def move_negative_elements(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1

    return arr

#Reverse a string using a stack data structure:

def reverse_string(string):
    stack = []
    reversed_string = ""

    for char in string:
        stack.append(char)

    while stack:
        reversed_string += stack.pop()

    return reversed_string

#Evaluate a postfix expression using a stack:
def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()


#Implement a queue using the stack data structure:

class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)



# In[2]:





# In[3]:





# In[ ]:




