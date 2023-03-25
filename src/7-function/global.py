def one():
    print(x)
    def two():
        print(x)
        def three():
            print(x)
        three()
    two()
    



x = 50
one()