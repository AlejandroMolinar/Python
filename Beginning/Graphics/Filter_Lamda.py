class Employees():
    def __init__(self, name, position, salary):
        self.name=name;
        self.position=position;
        self.salary=salary;
        
        
    def __str__(self):
        
        return "Hello {}, your position in de company is {} and your salary is {}.\n".format(self.name, self.position, self.salary);


listEmployeer=[
    
        Employees("Alejandro", "Director", 8000),
        Employees("Maria", "Sub Director", 7500),
        Employees("Peter", "Security Chief", 5000),
        Employees("Susan", "Secretary", 4000),
        Employees("Marcus", "Security", 4000)
        
    ]
        
        
def comisionEmp(employeer): 
    
    if (employeer.salary<=4000):
        employeer.salary= employeer.salary*1.03;
    
    return employeer;



#maxSalary= filter(lambda employee: employee.salary>=5000, listEmployeer);

listComision= map(comisionEmp, listEmployeer);

for employ in listComision:
    
    print(employ);