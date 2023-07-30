
# coding: utf-8

# In[1]:


# SCHOOL ADMINISTRATION PROGRAM


# In[2]:


import csv


# In[3]:


def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Place","Likes"])
        
        writer.writerow(info_list)

if __name__=='__main__':        
    condition = True
    student_num=1

    while(condition):
        student_info = input("Enter student information for student#{} in the following format (Name Age Place Likes): ".format(student_num))
        
        
        student_info_list=student_info.split(' ')
        
        print("\nThe entered information is-\nName:{}\nAge:{}\nPlace:{}\nLikes:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("Is the entered information correct? (yes/no): ")
        
        if choice_check=="yes":
            write_into_csv(student_info_list)
            
            condition_check=input("Enter (yes/no) if you want to enter information for another student: ")
            if condition_check=="yes":
                condition=True
                student_num=student_num + 1
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("\nPlease re-enetr the values: ")

