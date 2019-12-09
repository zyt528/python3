import optparse

class customer(object):
    buy_dict = {}

    def buy(self, pro_name, price):
        self.buy_dict[pro_name] = price


class testA(object):
    # def __init__(self):
    #     print("created")
    #
    # def __del__(self):
    #     print("deleted")
    value = 0

    def printf(self):
        print(self)
        print(self.value)

class testB(object):
    def printf(self):
        self.value = 0
        print(self.value)

class vipcust(object):
    def _disct(self, prod_name, price):
        if prod_name=='apple':
            return price*0.9
        elif prod_name=='peach':
            return price*0.8
        elif prod_name=='banana':
            return price*0.7
        else:
            return price

    def buy_some(self, prod_name, price):
        disct_price = self._disct(prod_name, price)
        self.prod_dict[prod_name]=disct_price

class A(object):
    def printf(self):
        print("A")

class B(object):
    def printf(self):
        print("B")

class C(A, B):
    def printf(self):
        print("C")
        A.printf(self)
        B.printf(self)

class picprint(object):
    def __init__(self):
        self.list_total = [[] for x in range(9)]

    def getprintstr(self, string):
        self.num_str = string

    def __unionpic(self, prc_list):
        for step in range(9):
            self.list_total[step] += [","] + prc_list[step]

    def printstr(self):
        num_fact = numfact()
        for eve_char in self.num_str:
            num_obj =num_fact.factory(eve_char)
            self.__unionpic(num_obj.draw())
            print_str = ''
            for sub_list in self.list_total:
                for every_char in sub_list:
                    print_str += every_char
                print_str = '\n'
        print(print_str)

class numfact(object):
    def factory(self, which):
        if int(which) == 0:
            return zeropic()
        elif int(which) == 1:
            return onepic()
        elif int(which) == 2:
            return twopic()
        elif int(which) == 3:
            return threepic()
        elif int(which) == 4:
            return fourpic()
        elif int(which) == 5:
            return fivepic()
        elif int(which) == 6:
            return sixpic()
        elif int(which) == 7:
            return sevenpic()
        elif int(which) == 8:
            return eightpic()
        elif int(which) == 9:
            return ninepic()

class numpic(object):
    def __init__(self):
        self.pic_list = [['' for i in range(9)] for x in range(9)]

    def setpos(self, i, j):
        self.pic_list[i][j] = '*'

    def draw(self):
        return self.pic_list

    def drawline(self, line):
        for step in range(9):
            self.setpos(line, step)

    def drawrow(self, row, row_type):
        if row_type == 0:
            for step in range(9):
                self.setpos(step, row)
        elif row_type == 1:
            for step in range(5):
                self.setpos(step, row)
        else:
            for step in range(4, 9):
                self.setpos(step, row)

class zeropic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 0)
        self.drawline(8)
        self.drawrow(8, 0)
        return self.pic_list

class onepic(numpic):
    def draw(self):
        self.drawrow(8, 0)
        return self.pic_list

class twopic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(8, 1)
        self.drawline(4)
        self.drawrow(0, 2)
        self.drawline(8)
        return self.pic_list

class threepic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(8, 0)
        self.drawline(4)
        self.drawline(8)
        return self.pic_list

class fourpic(numpic):
    def draw(self):
        self.drawrow(0, 1)
        self.drawline(4)
        self.drawrow(8, 0)
        return self.pic_list

class fivepic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 1)
        self.drawline(4)
        self.drawrow(8, 2)
        self.drawline(8)
        return self.pic_list

class sixpic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 0)
        self.drawline(4)
        self.drawrow(8, 2)
        self.drawline(8)
        return self.pic_list

class sevenpic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(8, 0)
        return self.pic_list

class eightpic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 0)
        self.drawrow(8, 0)
        self.drawline(4)
        self.drawline(8)
        return self.pic_list

class ninepic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 1)
        self.drawrow(8, 0)
        self.drawline(4)
        return self.pic_list

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-n", "--number", action="store", type="string", dest="num")
    option, args = parser.parse_args()
    print_str = picprint()
    print_str.getprintstr(option.num)
    print_str.printstr()
