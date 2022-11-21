def find_cur(x, g):
    exmp = (x**3 * 2 - 1 * x**2) #equation
    return x - g * exmp

def Gradient_descent(x, gamma): #Gradient descent
    eps = 1e-5
    count = 0
    while count <= 10_000:
        tmp_cur = x
        x = find_cur(tmp_cur, gamma)
        if abs(x - tmp_cur) < eps:
            return x
        count += 1
print(Gradient_descent(3, 0.01))

