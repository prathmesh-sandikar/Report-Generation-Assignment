def CheckPrimeOrNot(a):
    if a>1:
        for j in range(2, int(a / 2)+1):
            if (a%j)==0:
                return "Not Prime"
        else:
            return "Prime"
    else:
        return False


def CheckPalindromeOrNot(a):
    temp = a
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if a == reverse:
        return True
    else:
        return False


if __name__=="__main__":
    num1=float(input("Enter first number:"))
    print(CheckPrimeOrNot(num1))
    print(CheckPalindromeOrNot(num1))
