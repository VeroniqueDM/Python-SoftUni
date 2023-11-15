from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        # res = 0
        # for num in args:
        #     res += num
        # return res
        return reduce(lambda x, y: x + y,args)
    @staticmethod
    def multiply(*args):
        res = 1
        for num in args:
            res *= num
        return res

    @staticmethod
    def divide(*args):
        res = args[0]
        for num in range(1,len(args)):
            res /= args[num]
        return res

    @staticmethod
    def subtract(*args):
        res = args[0]
        for num in range(1, len(args)):
            res -= args[num]
        return res
#
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
a=1
