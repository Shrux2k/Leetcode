We have two arrays. 

Left one we sum from left to right. 
Right one we sum from right to left.

The idea is if pivot exists, leftside + pivot = rightside + pivot.

For example, arr = [1, 3, 7, 6, 5, 6]
left = [1, 4, 11 ,17, 22, 28]
right = [28, 27, 24, 17, 11, 6]

If there is a pivot, it should have the same index, then we return it, otherwise return -1;

​
