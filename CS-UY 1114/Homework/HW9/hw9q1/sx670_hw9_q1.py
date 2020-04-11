class Student:
    def __init__(self,name,NYU_id,net_id):
        self.name=name
        self.NYU_id=NYU_id
        self.net_id=net_id
        self.grades_list=[]

    def add_grade(self,catalog_name,grade):
        self.grades_list.append((catalog_name,grade))
        
    def average(self):
        s=0
        for i in self.grades_list:
            if(i[1]!='\n'):
                s=s+int(i[1])
        ave=round(s/len(self.grades_list))
        return ave
    
    def get_email(self):
        return self.net_id+"@nyu.edu"

def load_students(students_data_filename):
    f=open(students_data_filename,"r")
    student=[]
    Info=(f.readline()).split(",")
    for line in f:
        lst=line.split(",")
        if(lst[0]!='NYU ID'):
            s=Student(lst[1],lst[0],lst[2])
            for i in range(3,len(lst)):
                if(lst[i]!=""):
                    s.add_grade(Info[i],lst[i])
            student.append(s)
    f.close()
    return student

def generate_performance_report(student_lst,out_filename):
    f=open(out_filename,"w+")
    f.write("NYU ID,Average\n")
    for i in student_lst:
        s=""
        s=s+i.NYU_id+","+str(i.average())+"\n"
        f.write(s)
    f.close()

def generate_course_mailing_list(student_lst,catalog_name,out_filename):
    f=open(out_filename,"w+")
    for i in student_lst:
        for j in i.grades_list:
            if(catalog_name==j[0]):
                f.write(i.get_email())
                f.write("\n")
    f.close()

def main():
    f=open('hw9 - students grades.csv','r')
    generate_performance_report(load_students('hw9 - students grades.csv'),'Performance Report.csv')
    Info=(f.readline()).split(",")
    for i in range(3,len(Info)):
        generate_course_mailing_list(load_students('hw9 - students grades.csv'),Info[i],Info[i]+".txt")
    
main()
