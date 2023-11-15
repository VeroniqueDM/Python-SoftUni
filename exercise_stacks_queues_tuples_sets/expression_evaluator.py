from collections import deque
expression = input().split()
numbers = deque()
for elements in expression:

        if elements in "+-*/":
            while len(numbers) > 1:
                first = numbers.popleft()
                second = numbers.popleft()
                result = 0
                if elements == "+":
                    result = first + second
                elif elements == "-":
                    result = first - second
                elif elements == "*":
                    result = first * second
                else:
                    result = first // second
                numbers.appendleft(result)
        else:
            numbers.append(int(elements))

print(numbers.popleft())
