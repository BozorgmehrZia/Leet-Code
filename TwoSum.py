def two_sum(nums, s):
    dic = {}
    for i in range(len(nums)):
        if s - nums[i] in dic.keys():
            return i, dic[s - nums[i]]
        dic[nums[i]] = i
    return -1

class Employee:
    def __init__(self, name, baseSalary, Employees = None):
        self.name = name
        self.baseSalary = baseSalary
        self.Employees = Employees

    def get_salary_sum(self):
        if self.Employees is None:
            return self.baseSalary
        return sum(i.get_salary_sum() for i in self.Employees) + self.baseSalary


e = Employee("John", 5000, [Employee("Alice", 3000, [Employee("Bob", 2000), Employee("Eve", 2500)])])
if __name__ == '__main__':
    print(e.get_salary_sum())