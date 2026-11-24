#create a list of 10 numbers and print the first,last,and middle elements

numbers=[10,20,30,40,50,60,70,80,90,100]
print("first element:",numbers[0])
print("last element:",numbers[-1])
print("middle elements:",numbers[4],numbers[5])

#add an element at the end,at the begining,and at index 3.

numbers=[10,20,30,40,50]
numbers.append(60)
print("after adding at end:",numbers)
numbers.insert(0,5)
print("after adding at beginning:",numbers)
numbers.insert(3,25)
print("after adding at index 3:",numbers)

#remove an element by value, by index,and remove the last item

numbers=[10,20,30,40,50,60]
numbers.remove(30)
print("after removing by value:",numbers)
numbers.pop(2)
print("after removing by index:",numbers)
numbers.pop()
print("after removing last item:",numbers)

#find the sum,minimum,maximum,and average of a list of numbers

numbers=[10,20,30,40,50]
total=sum(numbers)
print("sum:",total)
minimum=min(numbers)
print("minimum:",minimum)
maximum=max(numbers)
print("maximum:",maximum)
average=total/len(numbers)
print("average:",average)

#reverse a list in three ways(reverse(),slicing,reversed()

num=[10,20,30,40,50]
list1=numbers.copy()
list1.reverse()
print("using reverse():",list1)
list2=numbers[::-1]
print("using slicing:",list2)
list3=list(reversed(numbers))
print("using reversed():",list3)
#6

numbers = [5, 2, 8, 1, 9, 3]

# Ascending order
ascending = sorted(numbers)

# Descending order
descending = sorted(numbers, reverse=True)

print("Original List:", numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)

#7
numbers = [1, 2, 3, 2, 4, 2, 5]

count = numbers.count(2)

print(count)

#8

numbers = [1, 2, 3, 2, 4, 1, 5]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)

#9

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)

#10

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = list(set(list1) ^ set(list2))

print(result)

#11

numbers = [10, 20, 5, 40, 30]

largest = max(numbers)
numbers.remove(largest)

second_largest = max(numbers)

print("Second largest:", second_largest)

#12

numbers = [1, 2, 3, 4, 5]

k = 2

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print(rotated)

#13

nested_list = [[1, 2], [3, 4], [5]]

flat_list = [num for sublist in nested_list for num in sublist]

print(flat_list)

#14

squares = [num**2 for num in range(1, 21)]

print(squares)

#15

numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])





