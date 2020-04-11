def convertAsciiToText(s):
    s1=""
    for i in range(0,len(s),2):
        s1=s1+chr(int(s[i:i+2]))
    return s1
def main():
    s=input()
    print(convertAsciiToText(s))
main()
