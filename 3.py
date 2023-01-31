# Write your solution for algorithm 3 below

# Write an algorithm that takes in an unsorted numerical
#  list as an argument and creates a new sorted list in 
# descending order (use the sorted() function).

myList = [5,1,15,2,12,13]

newList = sorted(myList, reverse=True)

print(newList)