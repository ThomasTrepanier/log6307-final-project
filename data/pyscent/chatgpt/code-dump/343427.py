class Example:
    def method1(self):
        print("method1 called")
        self.method2()  # Call another method from the same class

    def method2(self):
        print("method2 called")

obj = Example()
obj.method1()
# Output:
# method1 called
# method2 called
