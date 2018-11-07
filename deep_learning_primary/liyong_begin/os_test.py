import os
filelist=['E:/Data/Images/black_girl.jpg','E:/Data/Images/Archtecture']
for file in filelist:
	outfile=os.path.splitext(file)
	print(outfile)
print(os.pardir)
