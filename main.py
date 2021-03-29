# keyword Argument; 따로 지정하지 않는다면 순서를 지켜 인자에 넣어주어야한다.
def say_hello(name, age):
  return f"Hello {name} you are {age} years old"

hello = say_hello(age="12", name="hoho")
print(hello)