class Base:
    # id =0
    # name = "abc"
    def __init__(self, id,name):
        self.id = id
        self.name = name
    def printdata(self):
        print("The id is " + str(self.id) +" and name is " + str(self.name))
        
b1=Base(10,'abc')
b1.printdata()
# print(b1.__getstate__)
locals(b1)

# if __name__ == __main__:
#     app.run()