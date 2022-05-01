import itertools

"""
Given an array of positive numbers and a positive number k 
find the maximum sum of any contiguous subarray of size k
"""
# import math

# def max_contig_k_subarray_sum(l: list, k: int):
#     if not (k and l):
#         return "None"

#     left = 0
#     right = k

#     initial = l[left:right]
#     max_sum = sum(initial)

#     while right < len(l) - 1:
#         left += 1
#         right += 1
#         sum_subarray = sum(initial) - l[left] + l[right]  # travel each element once
#         # keep middle of list throw first out insert new
#         max_sum = max(max_sum, sum_subarray)

#     return max_sum


# max_contig_k_subarray_sum(l=[7, 8, 9, 15, 56, 2], k=3)

"""
Given an array of positive numbers and a positive number S 
find the length of the smallest contiguous subarray 
whose sum is greater
than or equal to S. 
Return 0 if no such subarray exists.
"""

# TIP:
# Sliding Window is a tool
# Real problem in q will have a unique algo to be discovered

# sliding window could be of dynamic lenght... but concept is same.
# build it..piece by piece to right... then take out left.. then again..right

# def subarray_sum_greater_than_S(l: list,s: int):

#     if not (l):
#         return 'invalid request'

#     left=0
#     right=0
#     sub_array=[]
#     min_len=math.inf

#     while right <= len(l) -1:

#         sub_array=l[left:right]

#         if sum(sub_array) >= s:
#             if len(sub_array) < min_len:
#                 min_len= len(sub_array)
#                 min_subarray=sub_array
#             left+=1
#         else:
#             right+=1

#     if min_len!=math.inf:
#         return min_subarray
#     else:
#         return 0

# subarray_sum_greater_than_S(l=[2, 1, 5, 2, 3, 2],s=7)


"""
Write a function to return the maximum number of 
fruits in both baskets.
"""

# def max_fruits_subset(l: list):

#     max_len=0
#     left=0
#     d={}
#     for idx,val in enumerate(l):

#         try:
#             d[val]+=1
#         except:
#             d[val]=1

#         print('idx val is ',idx,val)
#         print('d before while',d)
#         while len(d.keys())>2:              # similar algo to last...
#                                             #incrementally break start
#                                             # of sliding window
#             print(d)
#             d[l[left]]-=1
#             left+=1
#             d = {k: v for k,v in d.items() if v > 0}

#             print("now")
#             print(left)
#             print(d)

#         if len(l[left:idx+1])>max_len:
#             max_sub=l[left:idx+1]
#             max_len=len(max_sub)

#     return max_sub

# max_fruits_subset(['A', 'B', 'C', 'A', 'A'])


"""
Write a function to return the longest 
substring 
in a string
with no repeating characters
"""

# def longest_substring_norepeat(s: str):

#     lst = list(s)
#     left=0
#     d={}
#     MAX_LEN=0

#     for idx,el in enumerate(lst):

#         if el in d.keys():
#             left=idx
#             continue

#         d[el]=idx

#         curr=lst[left:idx+1]

#         if len(curr)>MAX_LEN:
#             MAX_LEN=len(curr)
#             max_subarray=curr

#     return max_subarray


# longest_substring_norepeat(['s','t','u','b','w','t','z','p','v','w','x'])


### ALT
# window_start = max(window_start, char_index_map[right_char] + 1)
# insert the 'right_char' into the map
# char_index_map[right_char] = window_end


# '''
# Longest Subarray with Ones after Replacement (hard)
# '''


# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous
# subarray of 1s having length 6.


# def longest_subarray_with_ones(nums: list,k: int):
#     left=0
#     max_sub=[]

#     for right,el in enumerate(nums):
#         if (right-left-k)>0:
#             while len(l[right-left]-k]) -

# Given a string and a pattern,
# find out if the string contains
# any permutation of the pattern.


def check_if_in_string(String: str, Pattern: str):

    pattern_dict = {}

    for i in Pattern:
        try:
            pattern_dict[i] += 1
        except:
            pattern_dict[i] = 1

    for idx, el in enumerate(String):
        if el not in pattern_dict:
            continue
        else:
            if pattern_dict[el] > 0:
                pattern_dict[el] -= 1

    # print()

    if sum(pattern_dict.values()) == 0:
        return "contains"
    else:
        return "doesnt"


# check_if_in_string(String="oidbaf", Pattern="abc")


def find_permutation(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from
    # the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def main():
    print("Permutation exist: " + str(find_permutation("oicdbaf", "abc")))
    print("Permutation exist: " + str(find_permutation("odicf", "dc")))
    print("Permutation exist: " + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print("Permutation exist: " + str(find_permutation("aaacb", "abc")))


"""
Write a function to return a list of 
starting indices of the anagrams of the 
pattern in the given string.
"""

# string_anagram(s="abbcabc", p="abc")
# "bca", "cab", and "abc".

################## TRY ONE ########################


def string_anagram(s: str, p: str):

    left = 0
    p_freq = {}
    window_freq = {}
    anagrams = []

    for el in p:
        try:
            p_freq[el] += 1
        except:
            p_freq[el] = 1
    print(p_freq)

    for right, x in enumerate(s):

        print(x, right)
        if x not in p_freq.keys():
            print(right)
            left += 1
            window_freq = {}
            continue
        else:  # wrong abb chars in S but shouldnt have gone here..
            # need sliding window for lenght management..
            try:
                window_freq[x] += 1
            except:
                window_freq[x] = 1

            if window_freq == p_freq:
                anagrams.append(window_freq)

    return anagrams


# string_anagram(s="abbcabc", p="abc")

################## TRY TWO ########################


def string_anagram_taketwo(s: str, p: str):

    left = 0
    p_freq = {}
    window_freq = {}
    anagrams = []

    for el in p:
        try:
            p_freq[el] += 1
        except:
            p_freq[el] = 1

    print(p_freq)

    for right, x in enumerate(s):

        if x not in p_freq.keys():
            print(right, "out")
            left = right
            print(left)
            window_freq = {}
            continue

        window = s[left : right + 1]

        print(window, "window")

        try:
            window_freq[x] += 1
        except:
            window_freq[x] = 1

        print(window_freq, "window")

        if len(window) == len(p):
            if window_freq == p_freq:
                anagrams.append(window)

        if len(window) >= len(p):
            left += 1
            window_freq[s[left]] -= 1

            if window_freq[s[left]] == 0:
                del window_freq[s[left]]

    return anagrams


# string_anagram_taketwo(s="adbcabc", p="abc")


def find_string_anagrams(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    result_indices = []
    # Our goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]
    for window_end, right_char in enumerate(str1):
        if right_char in char_frequency:
            # Decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):  # Have we found an anagram?
            result_indices.append(window_start)

        print(window_end)
        # Shrink the sliding window
        if window_end >= len(pattern) - 1:

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1  # Before putting the character back, decrement the matched count
                print(char_frequency[left_char], "freq of left")
                char_frequency[left_char] += 1  # Put the character back

    return result_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


# main()


"""
Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
"""


def remove_key_from_string(str1, key):
    left = 0
    non_key_idxs = 0

    while left <= len(str1) - 1:
        if str1[left] != key:
            str1[non_key_idxs] = str1[left]
            non_key_idxs += 1
        left += 1
    return str1[:non_key_idxs]


# remove_key_from_string([3, 2, 3, 6, 3, 10, 9, 3], key=3)
"""
Given a sorted array, create a new array containing squares 
of all the numbers of the input array in the sorted order.
"""


def make_squares(arr):
    squares = []
    arr = [x * x for x in arr]
    right = len(arr) - 1
    left = 0
    while left <= right:

        if arr[left] >= arr[right]:
            squares.append(arr[left])
            left += 1

        if arr[left] < arr[right]:
            squares.append(arr[right])
            right -= 1

    return squares[::-1]


make_squares([-2, -1, 0, 2, 3])

# 3N
# instead of appending...
# just make random list then change value from back to


def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return squares


def main():

    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


# main()

"""
Given an array of unsorted numbers
find all unique triplets in it that
add up to zero.
"""


def triplets_sum_zero(lst):
    triplets = []
    for idx, el in enumerate(lst):
        inner_freq = {}

        for j in lst[:idx] + lst[idx + 1 :]:

            if -(el + j) in inner_freq:
                triplets.append([el, j, -(el + j)])
                continue
            if j not in inner_freq:
                inner_freq[j] = 1

    return triplets


# x = triplets_sum_zero([-3, 0, 1, 2, -1, 1, -2])
# x = [sorted(y) for y in x]

# x.sort()
# x = list(x for x, _ in itertools.groupby(x))
# x


"""
Given an array with positive numbers and a positive target number, 
find all of its contiguous subarrays whose product is less than 
the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
"""

# sort it, then pair start and when condition meets
# - all remaining will also satisfy condition

# def prod_less_than_target(lst: List,target: int):

#     left=0,right=left+1

#     results=[]

#     list.sort()

#     while left < len(lst):

#         if lst[left]<target:
#             results.append([x])

#         if lst[right]*lst[left]<target:
#             results.append([lst[right],lst[left]])

#         left+=1


# for i in range(right, left-1, -1):


def countSubArrayProductLessThanK(a, k):
    n = len(a)
    p = 1
    res = 0
    start = 0
    end = 0
    while end < n:

        # Move right bound by 1
        # step. Update the product.
        p *= a[end]

        # Move left bound so guarantee
        # that p is again less than k.
        while start < end and p >= k:
            p = int(p // a[start])
            start += 1

        # If p is less than k, update
        # the counter. Note that this
        # is working even for (start == end):
        # it means that the previous
        # window cannot grow anymore
        # and a single array element
        # is the only addendum.
        if p < k:
            l = end - start + 1  # 1 already there?
            # suppose 2 added then
            # l = 1, right = 2
            # [1] arleady there
            # [1], [1,2] AND [2] so that's why 1

            res += l

        end += 1

    return res


# Driver Code
# if __name__ == "__main__":
#     print(countSubArrayProductLessThanK([1, 2, 3, 4], 10))
#     print(countSubArrayProductLessThanK([1, 9, 2, 8, 6, 4, 3], 100))
#     print(countSubArrayProductLessThanK([5, 3, 2], 16))
#     print(countSubArrayProductLessThanK([100, 200], 100))
#     print(countSubArrayProductLessThanK([100, 200], 101))

# counting number of ... is O(n)

# counting all instances...is o(n^3) :o
# temp_list = deque()
#     for i in range(right, left-1, -1):
#       temp_list.appendleft(arr[i])
#       result.append(list(temp_list))
#   return result

'''
Given two strings containing backspaces 
(identified by the character ‘#’), 
check if the two strings are equal.
'''

# def strs_w_backspace_equal_or_not(str1,str2):
    
#     str1=list(str1)
#     str2=list(str2)
    
#     #one i for traversal - but another set of two pointers slowly moving through iterable,
#     # checking equality only at corrected strings lenght counter (hypo)
#     # as soon as equality breaks for pair's correct length counter (hypo)
    
#     x1=0
#     x2=0
    
#     for i in range(-min(len(str1),len(str2))+1,1):
#         print(i)
        
#         if str1[-x1] != '#' and str2[-x2] != '#':
#             if str1[-x1] != str2[-x2]:
#                 return 'not equal'
#             x1+=1
#             x2+=1
            
#         if str1[-x1] == '#' and str2[-x2] == '#':
#             x1+=2
#             x2+=2
            
#         if str1[-x1] == '#':
#             x1+=2
#         elif str2[-x2] == '#':
#             x2+=2
    
#     if 
            
             
        


# str1=['a','b']
# str2=['c','d','e']

# for i in range(-max(len(str1),len(str2))+1,1):
#     print(str2[-i])


def group_movies_within_k_distance(movies,dist=5):
    
    movies_to_group=len(movies.keys())
    
    groups = {}
    
    left=0
    right=left+dist
    
    while movies_to_group > 0:
        
    return groups



def binary_search(l,el):
    
    right = len(l)-1
    
    left = 0 
    
    while left < right:
        
        mid = (right + left)%2

        if el == l[mid]:
            return mid
        elif el > l[mid]:
            left = mid+1
        elif el < l[mid]:
            left = mid -1
            
    return -1 
            
            
# binary_search([1,2,3,4],3)
# print("5")
    
    
# print("4")


# s1='asd'
# s2='ab'

# [[0]*(len(s2)+1) for i in range(len(s1)+1)]


def longest_common_subsequence(s1,s2):
    
    matrix=[[None]*(len(s2)+1) for i in range(len(s1)+1)]
    
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            
            if i==0 or j==0:
                matrix[i][j]=0
                
            elif s1[i-1] == s2[j-1]:
                matrix[i][j]=1+matrix[i-1][j-1]
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
                
    return matrix[len(s1)][len(s2)]

X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", longest_common_subsequence("AGGTAB", "GXTXAYB") )






