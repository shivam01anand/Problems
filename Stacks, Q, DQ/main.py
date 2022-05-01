import typing
from numpy import sign

# from pdb import set_trace

class ArrayQueue:
	"""FIFO queue implementation using a python list (w/ circular array design) as underlying storage"""
	DEFAULT_CAPACITY = 10

	def __init__(self):
		"""Create an empty qqueue"""
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		"""Return but don't remove the element at front of q."""
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		"""Remove and reutrn the first element of the queue
		Raise Empty exception if the q is empty"""
		if self.is_empty():
			raise Empty('Queue is empty')
		element = self.first()
		# set_trace()
		self._data[self._front] = None
		self._front = (self._front+1)%len(self._data)
		self._size -= 1
		return element
		# set_trace()

	def enqueue(self, e):
		"""Add an element to the back of q"""
		if self._size == len(self._data):
			self._resize(2*len(self._data))
		# set_trace()
		back_idx = (self._front+self._size)%len(self._data)
		self._data[back_idx] = e
		self._size += 1
		# set_trace()


	def _resize(self, cap):
		"""Resize to a new list of capacity >= len(self)"""
		old = self._data
		self._data = [None]*cap
		walk = self._front
		# set_trace()
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1+walk)%len(old)
			# set_trace()
		# set_trace()
		self._front = 0

class ArrayStack:

    def __init__(self):
        self._data = [ ]
        
    def len (self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self,e):
        self._data.append(e)

    def top(self):
        
        if self.is_empty():
            raise NameError("Stack is empty")
           
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise NameError("Stack is empty")
        return self._data.pop()
    
############################################################################
# Implement a function with signature transfer(S, T) that transfers all ele-
# ments from stack S onto stack T, so that the element that starts at the top
# of S is the ﬁrst to be inserted onto T, and the element at the bottom of S
# ends up at the top of T
############################################################################

# def signature_transfer(S: typing.List[typing.Any],T: typing.List[typing.Any]):
    
#     S=ArrayStack()
#     S.push(4)
#     S.push(5)
#     S.push(6)
#     print(S._data)
    
#     T = ArrayStack()
    
#     for idx in range(0,len(S._data)):
#         el=S.pop()
#         T.push(el)
        
#     return T._data

# signature_transfer(S=[],T=[]) 

####################################################################
# Give a recursive method for removing all the elements from a stack
####################################################################


# S=ArrayStack()
# S.push(5)
# S.push(6)
# S.push(7)

# def empty_stack(S):
    
#     if S.is_empty():
#         return print(f"Data is -> {S._data}")
#     else:
#         S.pop()
#         return empty_stack(S)
    
# empty_stack(S)

####################################################################
#Show how to use a stack S and a queue Q to generate all possible subsets
#of an n-element set T nonrecursively.
####################################################################


# input:
#     s = {1,2,3}

# variables:
#     Stack S
#     Queue Q

# return {1} {2} {1,2} {3,1,2}

# stack = ArrayStack()
# queue = ArrayQueue()

# queue.enqueue(set())

# T = [1,2,3, 4, 5]

# for i in T:
# 	stack.push(i)
# 	#queue.enqueue(i)

# while stack.is_empty()==False:
# 	cur = stack.pop()
# 	# set_trace()
#     for i in range(len(queue)):
#         a = queue.dequeue()
# 		b = a | cur
# 		queue.enqueue(a)
# 		queue.enqueue(b)
# 		# set_trace()
# print('why')

# while queue.is_empty()==False:
#     x = queue.dequeue()
# 	print(x)


#using deque only...

# from collections import deque

# def power_set(s):
#     q = deque()
#     q.appendleft([])
#     for elem in reversed(s):
#         while True:
#             subset = q.pop()
#             print(f"subset is {subset}")
#             q.appendleft([elem] + subset)
#             q.appendleft(subset)
#             print(q)
#             if not subset:
#                 print(f"done with {elem}")
#                 break
            
            
#     return list(q)

# power_set([1,2,3])

#no idea why this way...why this works..


#####################
#postﬁx version of “ (( 5 + 2 )∗( 8 − 3 ))/ 4” is “5 2 + 8 3 − ∗ 4 / ”. Describe
#a nonrecursive way of evaluating an expression in postﬁx notation.
####################


queue = ArrayQueue()

# expr = "5 2 + 8 3 - * 4 / "
# step = 0
# idx = expr.find(' ', step)
# while idx != -1:
# 	char = expr[:idx]
# 	expr = expr[idx+1:].strip()
# 	queue.enqueue(char)
# 	idx = expr.find(' ',0)
# if len(expr) != 0:
# 	queue.enqueue(expr[0])


# stack = ArrayStack()
# expr = ''
# while queue.is_empty() == False:
# 	elem = queue.dequeue()
# 	if elem not in {'+', '-', '*', '/'}:
# 		expr += elem + ' '
# 	elif len(stack) < 2:
# 		numbers = expr.strip().split(' ')
# 		if len(numbers) < 2:
# 			answer = str(eval(stack.pop() + elem + numbers[0]))
# 			stack.push(answer)
# 		else:
# 			answer = str(eval(numbers[0]+elem+numbers[1]))
# 			stack.push(answer)
# 			expr = ''
# 	else:
# 		numbers = []
# 		for i in range(2):
# 			numbers.append(stack.pop())
# 		answer = str(eval(numbers[0]+elem+numbers[1]))
# 		stack.push(answer)