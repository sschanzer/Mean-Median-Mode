#! /usr/bin/env python3

'''
Calculate the Mean, Median, and Mode of a given list
'''

def Mean_Medium_Mode(arr):

  arr = sorted(arr)
  idx = []

  for i in range(len(arr)):
    idx.append(i)

  # Mean 
  mean = sum(arr) / len(arr)
  mean = '{:.2f}'.format(mean)

  # Medium 
  if len(arr) % 2 == 0:
    med_1 = idx[len(idx) // 2]
    med_2 = idx[len(idx) // 2 + 1]
    med = (med_1 + med_2) / 2
    medium = '{:.2f}'.format(med)
  else:
    med = idx[len(idx) // 2]
    medium = '{:.2f}'.format(med)

  

  # Mode
  # Count occurance of values in the array
  occurances = []
  
  i = 0
  while i < len(arr):
    occurances.append(arr.count(arr[i]))
    i += 1

  # make dictionary with keys = arr and values = occurances
  arr_occurances = dict(zip(arr, occurances)) 

  # filter the dictionary to get keys with highest occurances
  mode = {k for (k, v) in arr_occurances.items() if v == max(occurances)}


  return ['Mean:', mean, 'Medium:', medium, 'Mode(s):', mode]


if __name__ == '__main__':
    print(Mean_Medium_Mode([1,1,2,3,4,4,6]))
    print(Mean_Medium_Mode([1,2,2,3,4,7,9]))
    print(Mean_Medium_Mode([6,11,3,8,4,6,8,4,8,5,7,6]))

