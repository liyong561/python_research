import numpy as np
import matplotlib.pyplot as plt

def test01():
	# 最简单的·绘图函数
	x1 = np.linspace(1,100,100)
	plt.plot(range(x1.size),x1)
	plt.show()
def test02():
	diction = {'simple':1,'media':2,'difficult':3}
	for value in diction.values():
		print(value)
test02()