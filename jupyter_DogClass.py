class Dog:  #约定俗成单词首字母大写的为类名
    """一次模拟小狗的简单尝试"""  #文档字符串说明类

    """
        __init__（）方法：
        一个特殊方法，每次建立实例就会运行一次;
        包含三个形参：self、name、age
        self自动传递到类中的方法和属性，所以必须有self形参而且必须在第一个
        注意注意！！！是双下划线        
    """

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name  #属性
        self.age = age  #以self开头的变量可以在整个类中使用

    def sit(self):
        """收到命令坐下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """收到命令打滚"""
        print(f"{self.name} is now rolling over")
