def binaryConverter(number):
    binary = bin(number)[2:] 
    binaryNumberList = [int(digit) for digit in binary]  
    return binaryNumberList

def twosComplement(number):
    newNumber = [0] * len(number)
    i = len(number) - 1
    flag = 0 
    while i >= 0:
        if number[i] == 0 and flag == 0:
            newNumber[i] = 0
        elif number[i] == 1 and flag == 0:
            newNumber[i] = 1
            flag = 1
        elif flag == 1:
            newNumber[i] = 0 if number[i] == 1 else 1
        i -= 1
    return newNumber

def recoder(number, required):
    number.append(0)
    while len(number) <= required:
        number.insert(0, 0)
    recodedValue = []
    i = len(number) - 1
    while i > 0:
        if number[i] == 0 and number[i-1] == 0:
            recodedValue.insert(0, 0)
        elif number[i] == 0 and number[i-1] == 1:
            recodedValue.insert(0, -1)
        elif number[i] == 1 and number[i-1] == 0:
            recodedValue.insert(0, 1)
        elif number[i] == 1 and number[i-1] == 1:
            recodedValue.insert(0, 0)
        i -= 1
    return recodedValue

def partialProductGenerator(multiplicand, multiplier, index):
    productLength = 2 * len(multiplicand)
    if multiplier[index] == 1:
        partialProduct = multiplicand
        for i in range(index):
            partialProduct.append(0)
        while len(partialProduct) < productLength:
            partialProduct.insert(0, 0)
    elif multiplier[index] == -1:
        partialProduct = twosComplement(multiplicand)
        for i in range(index):
            partialProduct.append(0)
        while len(partialProduct) < productLength:
            partialProduct.insert(0, 1)
    return partialProduct

def binaryAdder(number1, number2, length):
    carry = 0
    result = []
    for i in range(length - 1, -1, -1):
        digit_sum = int(number1[i]) + int(number2[i]) + carry
        result.insert(0, str(digit_sum % 2))  
        carry = digit_sum // 2 
    return ''.join(result)

def multiply(number1, number2):
    multiplicand = binaryConverter(max(number1, number2))
    multiplicand.insert(0, 0)
    multiplier = recoder(binaryConverter(min(number1, number2)), len(multiplicand))
    print(f"\nMultiplicand: {max(number1, number2)}, binary: {bin(max(number1, number2))[2:]}")
    print(f"Multiplier: {min(number1, number2)}, binary: {bin(min(number1, number2))[2:]}")
    print(f"Recoded multiplier: {multiplier}\n")
    multiplier.reverse()
    final = []
    for i in range(len(multiplier)):
        if multiplier[i] == 0:
            print(f"Step {i+1}: Recoded value is 0, Shift 1 bit.")
            continue
        partial = partialProductGenerator(multiplicand, multiplier, i)
        print(f"Step {i+1}: Recoded value is {multiplier[i]}, Computed partial product: {partial}")
        final.append(partial)

    print("\nPartial products to add:")
    for line in final:
        print(line)

    finalResult = final[0]
    for partial in final[1:]:
        finalResult = binaryAdder(finalResult, partial, len(multiplicand))
    return finalResult

x, y = map(int, input("Enter two numbers to be multiplied: ").split())
answer = multiply(x, y)
print(f"\nAnswer in Binary: {answer}")
print(f"Answer in decimal: {int(answer, 2)}")

