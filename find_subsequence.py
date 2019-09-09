import os
import argparse
#define  a function for subsequence calculation
def find_subsequence1(input_data,input_size,n1): 
    #Considering the first point
    sum_data=0 #variable for keeping temp sum data
    subseq_list = [] # a list for keeping every subsequence number  
    absolute_val_list=[] # a list for keeping absolute differences of the pair of subsequences
    max_sum = 0 # varibale for keeping max sum of subsequence
    for i in range(0,input_size): #Start point
        for j in range(i,input_size): #end point
            for k in range(i,j+1): # get the subsequences
                subseq_list.append(input_data[k]) 
            if(len(subseq_list)<=n1):  # check the length of subsequences
                if(args.values is not None): # check the input  of values, if values given then calculate _sum_ of the values
                    sum_data = sum(subseq_list) 
                else: # else calcualte the  _sum_ of the absolute values
                    for ii in range(len(subseq_list)-1):
                        val1 = subseq_list[ii]
                        val2 = subseq_list[ii+1]
                        if(val1>0) and (val2>0): # check if the value is positive or negative
                            absolute_val_list.append(val1-val2)
                        else:
                            absolute_val_list.append(abs(val1)+abs(val2))
                    sum_data = sum(absolute_val_list) # take the sum  
            max_sum_final=find_max_sum(sum_data,max_sum) # send it to the max function
            sum_data=0
            max_sum= max_sum_final
            subseq_list.clear() #clear the list for new values
            absolute_val_list.clear() 
            
    print("MAX_SUM:",max_sum_final)
# this is function for finding max
def find_max_sum(sum_data,max_sum):
    if(sum_data>max_sum):
        
        max_sum=sum_data
    else:
        pass
        
    return max_sum

if __name__== "__main__":
    
#init argument parser for taking argument from user
    parser = argparse.ArgumentParser()

    # argparse receiving list of input data and parameter (e.g., python main)
    parser.add_argument('--values',type=int,help="give how at most how many values to consider for   summation")
    parser.add_argument('--differences',type=int,help="give the differences for calculating the highest sum ")
    parser.add_argument('--input-filepath',help="give the input txt file")
    args = parser.parse_args()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    INPUT_PATH = os.path.join(os.getcwd(), 'data', args.input_filepath)
    n1 = args.differences
    n2= args.values
    listdata =[]
# read the input path and parse the data  with space
    with open(INPUT_PATH,'r') as f:
        for line in f:
            for val in line.split():
                listdata.append((int(val)))
    input_size = len(listdata)
    max_sum=0
    if(n1 is not None):
#send the data and input data size to subsequence find function
        find_subsequence1(listdata,input_size,n1)
