В Python доступны 1 и 4 варианты сокрытия метода при наследовании

1. public -> public
```python
class A:

    def do(self):
        print("do something")


class B(A):
    pass


a = A()
b = B()
a.do() # do something
b.do() # do something

```

4.  private -> private
```python
class C:

    def __dont_do(self):
        print("this is private")


class D(C):
    pass


c = C()
d = D()
c.__dont_do() # raises an AttributeError
d.__dont_do() # raises an AttributeError
```

Вместо двойного подчеркивания можно использовать декоратор @private. Двойной подчекривание можно обойти при помощи обращения _ClassName__dont_do.