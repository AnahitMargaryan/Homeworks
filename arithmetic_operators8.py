
#Exercise 8. Given the salaries of three employees working at a department, find the
#amount of money by which the salary of the highest-paid employee differs
#from the salary of the lowest-paid employee. The input consists of three
#positive integers - the salaries of the employees. Output a single number,
#the difference between the top and the bottom salaries

a = 2500
b = 3000
c = 1800

if a > b > c:
    print(a - c)
if a < b < c:
    print(c - a)
if a > b < c:
    print(b - a)
if a < b > c:
    print(b -  c)
else:
    print ("All are equal.")




# with max(), min()

salary1 = 2500
salary2 = 3000
salary3 = 1800
 
max_salary = max(salary1, salary2, salary3)
min_salary = min(salary1, salary2, salary3)
salary_difference = max_salary - min_salary
print(salary_difference)


