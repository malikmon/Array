input_arr = [1,1,1,1,1,2,2,2,3,3,3,4,5,6,7,7,7,7,8]
 #output_arr = [1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0,0,0,0] 
 
temp = input_arr[0]
len_arr = len(input_arr)
count = 1
out_arr = [0]*len_arr
out_arr[0] = temp

 
for i in range(1,len_arr):
    if input_arr[i] == temp:
        input_arr[i] = 0
    else:
        temp = input_arr[i]
        out_arr[count] = temp
        count += 1
        
print("input_arr is", input_arr )
#print("distinct count is", count)
print("output arr", out_arr)
