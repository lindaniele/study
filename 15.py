class Master(object):
    def __init__(self):
        self.jishu="古法煎饼果子的配方"
    def make(self):
        print("[古法]按照'%s'制作出一份煎饼果子"%self.jishu)
class School(object):
    def __init__(self):
        self.jishu="现在煎饼果子的配方"
    def make(self):
        print("[现代]按照'%s'制作出一份煎饼果子" % self.jishu)
class Prentice(Master,School):
    def __init__(self):
        self.jishu ="猫式煎饼果子的配方"
    def make(self):
        self.__init__()
        print("[猫式]按照'%s'制作出一份煎饼果子" % self.jishu)
    def old_make(self):
        Master.__init__(self)
        print("[古法]按照'%s'制作出一份煎饼果子" % self.jishu)
    def new_make(self):
        School.__init__(self)
        print("[现代]按照'%s'制作出一份煎饼果子" % self.jishu)
damao=Prentice()
# print(damao.jishu)
damao.make()
damao.old_make()
damao.new_make()