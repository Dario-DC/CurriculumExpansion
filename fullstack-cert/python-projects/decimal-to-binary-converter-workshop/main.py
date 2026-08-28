def decimal_to_binary(input):
    print(f"Calling decimal_to_binary({input})")

    if input == 0 or input == 1:
        print("Returning result for base case with input:", input)
        return str(input)
    result = decimal_to_binary(input // 2) + str(input % 2)
    print(f"Returning result for input {input}: {result}")
    return result

decimal_to_binary(10)