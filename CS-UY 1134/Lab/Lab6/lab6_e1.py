def decimal_to_binary(input_int):
    binary_output=""
    n=0
    while(2**n<=input_int):
        n+=1
    
    input_int-=(2**n)
    for i in range(n-1,-1,-1):
        if(input_int<(2**n)):
            binary_output=binary_output+"0"
        else:
            binary_output=binary_output+decimal_to_binary(input_int)
            break
    return "1"+binary_output