"""Introduction to sets in Python (HackerRank)"""
'''method 1'''

# def average(array):
#     # your code goes here
#      return sum(set(array))/len(set(array))
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)


'''method 2'''

# def average(array):    
#     distinct = set(arr)    
#     return round(sum(distinct)/len(distinct),3)
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)


'''method 3'''

# def average(array):
#     l=set(arr)
#     return '{0:.3f}'.format(sum(array)/len(array))

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)