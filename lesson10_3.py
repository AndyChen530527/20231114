import random
import pyinputplus as pyip

def getStudents(student_nums:int=1, scores_nums:int=2) -> list[list]:



if __name__ == '__main__':
    s_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
    o_nums:int = pyip.inputInt("請輸入科目數(1~7):",min=1,max=7)
    students:list[list] = getStudents(student_nums=s_nums,scores_nums=o_nums)
    print(students)