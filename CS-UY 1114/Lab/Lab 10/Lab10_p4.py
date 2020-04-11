def html_table_generator(lst,file_to_write_to):
    f=open(file_to_write_to,"w")
    f.write("<html>\n")
    f.write("\t"+"<table>\n")
    f.write("\t"*2+"<tr>\n")
    r=len(lst)
    c=len(lst[0])
    for i in range (c):
        f.write("\t"*3+"<th>"+lst[0][i]+"</th>\n")
    f.write("\t"*2+"</tr>\n")
    for i in range(1,r):
        f.write("\t"*2+"<tr>\n")
        for j in range(c):
            f.write("\t"*3+"<td>"+lst[i][j]+"</td>\n")
        f.write("\t"*2+"</tr>\n")
    f.write("\t"+"<table>\n")
    f.write("<html>\n")

def main():
    html_table_generator([["Header1","Header2","Header3","Header4"],["R1C1","R1C2","R1C3","R1C4"],["R2C1","R2C2","R2C3","R2C4"],["R3C1","R3C2","R3C3","R3C4"]],"lab10_p4.txt")

main()


