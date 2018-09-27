import numpy as np


vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
vec3 = np.array([7, 8, 9])
vec4 = vec3.T
print(vec3)
print(vec4)
vec01 = np.matrix([1, 2, 3])
vec02 = np.matrix([4, 5, 6])

vec3 = np.outer(vec01, vec02)
vec4 = np.cross(vec2, vec1)   # 叉乘函数
print(vec3)
print(vec4)



assert np.linalg.norm(vec1-vec2) == np.sqrt(np.sum(np.square(vec1-vec2)))

