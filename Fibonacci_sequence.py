import numpy as np

def Fibonacci(num,n_0,n_1):
    f_n = np.zeros((num,1))
    f_n[0] = n_0;
    f_n[1] = n_1;
    for i in range(1,num-1):
     f_n[i+1] = f_n[i-1]+f_n[i]
    F_n = f_n[num]
    return F_n

def main():
    n_0 = 0
    n_1 = 1  # initializing the first two terms of the sequence
    num = 100  # a random setup of the nth Fibo term
    F_n = Fibonacci(num,n_0,n_1)
    print("The"+"str(num)"+"th Fibonacci number is: ",F_n)

 if __name__ == "__main__":
     main()