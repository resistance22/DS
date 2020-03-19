
###bubble sort###
def bubble_sort(A):
   m = len(A)
   bubble_found = False
   for j in range(m):
      for i in range(j,0,-1):
         if A[i] < A[i-1]:
            bubble_found = True
            A[i],A[i-1] = A[i-1],A[i]
         if not bubble_found:
            break
   return A
###/bubble sort/###

###insertion sort###
def insertion_sort(A):
   lenght = len(A)
   for i in range(1,lenght ):
      item = A[i]
      j = i
      while j > 0 and item < A[j-1]:
         A[j] = A[j - 1]
         j -= 1
      A[j] = item
      print(A) 
###/insertion sort/###



###selection sort###
def selection_sort(A):
   for i in range(len(A)):
      min_index = i
      for j in range(i,len(A)):
         if A[min_index] > A[j]:
            min_index = j
      A[min_index],A[i] = A[i],A[min_index]
   print(A)
###/selection sort/###
