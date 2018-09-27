class Spring:

    def __init__(self):
        self.name = None
        self.age = None

    def set_name(self, name):
        name = "liyong"
        return name

    def get_name(self):
        print(self.name)  # 应该有self

    def get_name2(self):
        self.name = self.set_name("dfs")


sp = Spring()
# sp.get_name("good") 自带一个self参数
sp.get_name()