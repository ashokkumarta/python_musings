#nested classes
class one:
    
    class two:
        pass
    
    def get_two(self):
        return two()

if __name__ == '__main__':
    a = one()
    b = a.get_two()
    print(type(b))
