#!/usr/bin/env python
# coding: utf-8

# #  Create a null vector of size 10 but the fifth value which is 1.

# In[3]:


import numpy as np

size = 10
position = int(input("Enter the position (0 to 9) for the value 1: "))

if 0 <= position < size:
    null_vector = np.zeros(size)
    null_vector[position] = 1
    print("Null vector:", null_vector)
else:
    print("Invalid position. Please enter a value between 0 and 9.")


# 2 WAY

# In[2]:


import numpy as np

# Get user input for the position of the non-zero element
position = int(input("Enter the position (0-9) of the non-zero element: "))

# Create a null vector of size 10
null_vector = np.zeros(10)

# Set the specified position to 1
null_vector[position] = 1

print("Resulting vector:", null_vector)


# # 2. Create a vector with values ranging from 10 to 49

# In[5]:


import numpy as np

# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

print("Vector:", vector)


# In[8]:


import numpy as np

# Get user input for the range start and end
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

# Create a vector with values ranging from start to end (inclusive)
vector = np.arange(start, end + 1)

print("Resulting vector:", vector)


# # 3. Create a 3x3 matrix with values ranging from 0 to 8

# In[9]:


import numpy as np

# Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape(3, 3)

print("Resulting matrix:")
print(matrix)


# 2 WAY

# In[11]:


import numpy as np

# Get user input for the matrix values
values = [int(input(f"Enter value for row {i+1}, column {j+1}: ")) for i in range(3) for j in range(3)]

# Reshape the values list into a 3x3 matrix
matrix = np.array(values).reshape(3, 3)

print("Resulting matrix:")
print(matrix)


# # 4. Find indices of non-zero elements from [1,2,0,0,4,0]

# In[12]:


import numpy as np

arr = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(arr)

print("Indices of non-zero elements:", non_zero_indices)


# 2 WAY

# In[13]:


import numpy as np

# Get user input for the list
input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Convert the list to a NumPy array
array = np.array(input_list)

# Find the indices of non-zero elements
non_zero_indices = np.nonzero(array)[0]

print("Indices of non-zero elements:", non_zero_indices)


# # 5. Create a 10x10 array with random values and find the minimum and maximum values.

# In[15]:


import numpy as np

# Get user input for the range of random values
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

# Create a 10x10 array with random values in the specified range
array = np.random.randint(min_value, max_value + 1, size=(10, 10))

# Find the minimum and maximum values in the array
min_val = np.min(array)
max_val = np.max(array)

print("Generated array:")
print(array)
print("Minimum value:", min_val)
print("Maximum value:", max_val)


# 2 way

# In[14]:


import numpy as np

# Create a 10x10 array with random values between 0 and 1
array = np.random.rand(10, 10)

# Find the minimum and maximum values in the array
min_value = np.min(array)
max_value = np.max(array)

print("Array:")
print(array)
print("Minimum value:", min_value)
print("Maximum value:", max_value)


# # 6. Create a random vector of size 30 and find the mean value.

# In[16]:


import numpy as np

# Create a random vector of size 30
random_vector = np.random.random(30)

# Calculate the mean value of the random vector
mean_value = np.mean(random_vector)

print("Random vector:", random_vector)
print("Mean value:", mean_value)


# In[17]:


import numpy as np

# Get user input for the range of random values
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

# Create a random vector of size 30 with values in the specified range
vector = np.random.randint(min_value, max_value + 1, size=30)

# Calculate the mean value of the vector
mean_value = np.mean(vector)

print("Generated random vector:")
print(vector)
print("Mean value:", mean_value)


# In[ ]:




