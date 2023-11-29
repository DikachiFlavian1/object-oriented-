"""
def main():
    student = get_student()
    if student["name"] == "zucci":
        student["house"] = "green_house"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("house: ")
    return {"name": name, "house": house}
if __name__ == "__main":
    main()"""

"""
class Students:
  ...

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  student = Students()
  student.name = input("name: ")
  student.house = input("house: ")

if __name__ == "__main":
  main()


class Students:
     def __init__(self,name,house) :
        self.name = name
        self.house = house
def main()        :
   student = get_student()
   print(f"{student.name} from {student.house}")
def get_student():
   name = input("name: ")
   house = input("house: ")
   student = Students(name,house)

if __name__ == "__main__":
  main()"""
"""
import random
class Hat:
  def __init__(self) :
        self.houses = ["bluehouse","greenhouse",
                    "yellowhouse","redhouse"]
  def sort(self,name):
      name = input("Name: ")
      print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("name")"""
"""
n = 5
for i in range(n):
    print("MEow")"""
"""
def meow(number:int) :
    return "meow\n" * number
number = int(input("Number: "))
catsound = meow(number)
print(catsound,end="")"""

"""
import sys
if len(sys.argv) == 1:
    print("meow")
else:
    print("usage:meows.py")    


def main():
    yell("this is cs50")
def yell(phrase):
    print(phrase.upper())
if __name__ == "__main__":
    main()
"""

def main():
    n = int(input("what's n? "))
    for i in range(n):
        print(sheep(i +1))

def sheep(n)  :
    return "ssd" * n
if __name__ == "__main__":
    main()

def main():
    n = int(input("whats n? "))
    for s in sheep (n):
        print (s)
def sheep (n) :
    for i in range(n):
        yield "ssd" * i
if __name__ == "__main__":
      main() 