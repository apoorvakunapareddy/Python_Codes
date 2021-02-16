class StringCovert():
    def getString(self):
        self.String1 = input("Please enter the string: ")
    
    def print_String(self):
        print(self.String1.upper())

x=StringCovert()
x.getString()
x.print_String()