def write_name(filename,first_name,last_name):
    f=open(filename,"w")
    f.write(first_name+" "+last_name)
    f.close()


def main():
    write_name("lab10_1.txt","Kevin","Xu")

main()
