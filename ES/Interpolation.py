class Interpolation:

    def __init__(self, x, y):
        assert len(x) == len(y)
        self.x = x
        self.y = y

    # + - * / operations for integer_as_ratio
    def summation(self, num1, num2):
        return float(((num1[0] * num2[1]) + (num2[0] * num1[1])) / (num1[1] * num2[1])).as_integer_ratio()

    def sub(self, num1, num2):
        if not isinstance(num1, tuple):
            num1, num2 = float(num1).as_integer_ratio(), float(
                num2).as_integer_ratio()

        if num1[1] == num2[1]:
            return float((num1[0] - num2[0]) / num1[1]).as_integer_ratio()
        else:
            return float(((num1[0] * num2[1]) - (num2[0] * num1[1])) / (num1[1] * num2[1])).as_integer_ratio()

    def multiply(self, num1, num2):  # num1 - numerator, num2 - denominator
        if num2[0] == 0:
            return float(0).as_integer_ratio()
        return float((num1[0] * num2[0]) / (num1[1] * num2[1])).as_integer_ratio()

    def division(self, num1, num2):  # num1 - numerator, num2 - denominator
        if not isinstance(num1, tuple):
            num1, num2 = float(num1).as_integer_ratio(), float(
                num2).as_integer_ratio()
        #         if (num2[0]*num1[1]) == 0:
        #             return float(0).as_integer_ratio()
        #         print(num1[0], ", ", num1[1], ", ", num2[0], ", ", num2[1])
        return float((num1[0] * num2[1]) / (num2[0] * num1[1])).as_integer_ratio()

    def get_d(self):
        x = self.x
        y = self.y
        y_len = len(y)

        pyramid = [[y] + [0] * (y_len - 1) for y in y]
        numerator, denominator = [
            [y] + [0] * (y_len - 1) for y in y], [[y] + [0] * (y_len - 1) for y in y]

        for j in range(1, y_len):
            for i in range(y_len - j):
                numerator[i][j] = self.sub(
                    pyramid[i + 1][j - 1], pyramid[i][j - 1])
                denominator[i][j] = self.sub(x[i + j], x[i])
                pyramid[i][j] = self.division(
                    numerator[i][j], denominator[i][j])

        return pyramid[0], numerator[0], denominator[0]

    def fraction_newton_polynomial(self):
        y = self.y
        x = self.x
        coeff, numerator, denominator = self.get_d()
        eq = []
        temp = ' '
        p0 = float(coeff[0]).as_integer_ratio()
        print(f'P0(x) = {p0}')

        for idx in range(1, len(y)):
            if x[idx - 1] >= 0:
                temp += f'(x-{x[idx - 1]})'
            else:
                temp += f'(x+ {-x[idx - 1]})'
            eq.append(
                f'({numerator[idx][0]}/{numerator[idx][1]})/({denominator[idx][0]}/{denominator[idx][1]}) *{temp}')  # fraction
            #             eq.append(f'{self.division((numerator[idx][0] / numerator[idx][1]), (denominator[idx][0] / denominator[idx][1]))} *{temp}')  ### fraction
            print(f'P{idx}(x) = {coeff[0]} + ', '+ '.join(eq))

        return [p0] + [self.division(numerator[i], denominator[i]) for i in range(1, len(numerator))]

    def get_x(self, idx):
        index = idx
        x = self.x
        if index != int(index):
            return x[int(index)] + ((x[int(index) + 1] - x[int(index)]) * (index - int(index)))
        else:
            return x[int(index)]

    def evaluate(self, index):
        pyramid, numerator, denominator = self.get_d()
        C = pyramid
        x = self.get_x(index)
        y = float(self.y[0]).as_integer_ratio()
        for i in range(1, len(self.x)):
            v = float(1).as_integer_ratio()
            for j in range(0, i):
                v = self.multiply(v, self.sub(x, self.x[j]))
            v = self.multiply(v, C[i])
            y = self.summation(y, v)
        return y

def get_input(n):
    if isinstance(n, str) and '/' in n:
        nums = n.split('/')
        return int(nums[0]) / int(nums[1])
    else:
        return float(n)