names = ['gongjun', 'mrgong', 'misslee', 'abc']
'''测试'''
relsult = [name for name in names if len(name) >= 3]

print(relsult)



class student:

    def __init__(self, name, age, sex, className):
        self.name = name
        self.age = age
        self.sex = sex
        self.className = className

    def getName(self):
        return self.name


if __name__ == "__main__":
    s = student("austin",18,'男','电子商务')
    print(s.getName())
