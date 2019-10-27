
import numpy as np
import matplotlib.pyplot as plt
from random import sample

X = np.random.random_sample((5, 6))

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111, projection="polar")
ax.set_title('TASK 4') 
plt.thetagrids(np.arange(0, 360, 360.0/X.shape[1]), labels=np.arange(0, X.shape[1], 1)) 

R = np.empty([0, X.shape[1]]) 
F = np.empty([0, X.shape[1]])
vector_bool = np.empty([X.shape[1], 1])
vector_bool.fill(True)
for i in range(X.shape[0]):
    vec_bool = X[i]<=X
    num = np.dot(vec_bool, vector_bool)
    if (np.sum(num==X.shape[1])<=1):
        R = np.vstack((R, X[i]))
    else:
        F = np.vstack((F, X[i]))

pol_x = np.arange(0, X.shape[1]) 
pol_x = np.append(pol_x, 0) 
pol_x = 2 * 3.14 * pol_x/ X.shape[1]

for d in R:
    pol_y = np.append(d, d[0])
    ax.plot(pol_x, pol_y, label = "pareto", color="red")

for fd in F:    
    pol_y = np.append(fd, fd[0])
    ax.plot(pol_x, pol_y, label='not', color="blue")

ax.legend(loc='center right', bbox_to_anchor=(0.0, 0.5), shadow=True, ncol=2)
plt.show()