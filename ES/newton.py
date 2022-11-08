from Interpolation import *


if __name__ == '__main__':

    x = [0.710821, 7.352, 0.7799, 0.82123, 1, 3.142, 1000/7]
    y = [135, 0.121, -58, 103, -77.7717, -50.65765766, 78.345]
    x = [get_input(i) for i in x]
    y = [get_input(i) for i in y]
    print(x)
    print(y)

    interpolation = Interpolation(x, y)
    interpolation.fraction_newton_polynomial()
    loc = float(input("Location : "))

    print(
        f'Answer for x : {interpolation.get_x(loc)} at location {loc} : {interpolation.evaluate(loc)[0]}/{interpolation.evaluate(loc)[1]} or {(interpolation.evaluate(loc)[0] / interpolation.evaluate(loc)[1])}\n')

    for i, val in enumerate(x):
        res = interpolation.evaluate(i)
        print("Loc", i, ": x = ", val, "\t, y = ", res,
              " | ", res[0] / res[1], " (", y[i], ")")
