#导入Mymod自定义模块
from JiChu import Mymod
from JiChu.Mymod import output_stu


print(__name__)
L= Mymod.input_stu()
output_stu(L)
