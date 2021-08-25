startNumber, endNumber = input("Nhập vào 2 số: ").split()
startNumber = int(startNumber)
endNumber = int(endNumber)

if endNumber < startNumber:
    print("Số kết thúc phải lớn hơn số bắt đầu")
else:
    for number in range(startNumber, endNumber + 1):
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)