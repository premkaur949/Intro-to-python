import random

def main():
    print("Khansole Academy")
    a = random.randint(10,99)
    b = random.randint(10,99)
    sum = a + b
    sum = int(sum)
    print("What is "+ str(a) + " + " + str(b) + " ?")
    user_ans = int(input("Your answer: "))
    if user_ans != sum:
        print("Incorrect.")
        print("The expected answer is " + str(sum))
    else:
        print("Correct!")
    
    
if __name__ == '__main__':
    main()
