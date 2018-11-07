from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
x_dim, y_dim = m.screen_size()  # get the size of screen
m.move(x_dim/2, y_dim/2)
m.click(x_dim/2, y_dim/2)  # 代表左右键点击事件
print(x_dim, y_dim)
k.type_string("Hello,Worls")