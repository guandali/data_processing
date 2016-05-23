#pyplot is the plotting module 
import matplotlib.pyplot as plt
import random 

#Generate data 
xs = range(10) # from 0...9
ys1 = range(10) #Same as above
ys2 = [random.randint(0,20)  for i in range(10)] # generating 10 random 

#Create a 10-inch x 5-inch figure 
fig = plt.figure(figsize=(10,5))

#Draw a line graph 
plt.plot(xs, ys1,  label='line 1')
plt.plot(xs, ys2,  label= 'line 2')

#Create legend 
plt.legend(loc='upper center', ncol = 4)

#Finally, render and store the figure in an image 
plt.savefig('twolines.png', format='png') 


