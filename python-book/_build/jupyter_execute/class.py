#!/usr/bin/env python
# coding: utf-8

# # Classの使い方

# ### ```class```とは

# In[1]:


# class名は大文字を使用することが多い
class Person:
    name = 'Tom'
    age  = 32


# In[2]:


# <__main__.Person at 0x7fe2e107cfa0>
person = Person()
person


# In[ ]:





# In[3]:


print(person.name)
print(person.age)


# ### ```init```とは

# In[4]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In[5]:


person = Person('John', 29)
print(person.name)
print(person.age)


# ### 3. classの継承について

# In[6]:


# classのプロパティのみ継承する
class Student(Person):
    pass


# In[7]:


student = Student('Mike', 20)
print(student.name)
print(student.age)


# In[8]:


# 継承先のclassでinitすると、継承元のinitプロパティは失われる
class Student(Person):
    def __init__(self, grade):
        self.grade = grade


# In[9]:


# 継承元のinitは呼び出されない
student = Student('Scott', 15)


# In[45]:


# 上記を回避するためには、継承先init()内に継承元init()を呼び出す
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_info(self):
        print('my name is {}, {} years old.'.format(self.name, self.age))

class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade


# In[46]:


student = Student('Julia', 20, 3)
print(student.name)
print(student.age)
print(student.grade)
student.print_info()


# In[ ]:





# ### ```super()```とは？

# In[37]:


# super()を使うと、全てのpropertyとmethodも引き継ぐことができる
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_info(self):
        print('my name is {}, {} years old.'.format(self.name, self.age))
    
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade


# In[38]:


# methodの
student = Student('Julia', 20, 3)
student.print_info()


# ### `__iter__()`とは

# In[87]:


class MyNumbers:
    # __itre__()によって、iterotor（繰り返し処理）を作成する
    def __iter__(self):
        self.number = 1
        return self
    
    def __next__(self):
        current_number = self.number
        self.number += 1
        return current_number


# In[88]:


mynumbers = MyNumbers()
myiter = iter(mynumbers)


# In[89]:


print(next(myiter))
print(next(myiter))
print(next(myiter))


# In[94]:


class MyNumbers:
    # __iter__()によって、iterotor（繰り返し処理）を作成する
    def __iter__(self):
        self.number = 1
        return self
    
    # 繰り返し処理部分を作成する
    def __next__(self):
        if self.number <= 10:
            current_number = self.number
            self.number += 1
            return current_number
        else:
            raise StopIteration

mynumbers = MyNumbers()
myiter = iter(mynumbers)

for number in myiter:
    print(number)


# ### ```__repr__()```とは

# In[64]:


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        pass
    
    
    def __repr__(self):
        return "<__main__.Person: name = " + str(self.name) + "; age = " + str(self.age) + ">"


# In[65]:


person = Person('Kate', 24)
person


# In[ ]:




