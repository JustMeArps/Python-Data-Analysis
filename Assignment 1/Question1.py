import numpy as np

#creating vector arrays for testing each data type
#---these vectors are for testing for NOMINAL data type---
vec1 = np.array(["Toronto", "Vancouver", "Montreal"])
vec2 = np.array(["Toronto", "Calgary", "Montreal"])

#---these vectors are for testing for BINARY data type---
# vec1 = np.array(["F", "M", "M", "F"])
# vec2 = np.array(["F", "F", "M", "M"])

#---these vectors are for testing for ORDINAL data type---
# vec1 = np.array(["low", "medium", "high"])
# vec2 = np.array([0,4,5])

#---these vectors are for testing for NUMERIC data types---
# vec1 = np.array([9,4,6])
# vec2 = np.array([2,6,1])


#dictionary to for ordinal data types
dict1 = {'low', 'small', "short", 'bad', 'fair', 'cold'}
dict2 = {'medium', 'moderate', 'good'}
dict3 = {'high', 'big', 'tall', 'excellent', 'hot'}

#initialising the type variable as integer to later store the type of the data
type_vects = 0

#for loop to check if any of the strings in the vector match out dictionary for ordinal data types
for i in range(len(vec1)):
    if vec1[i] in dict1: #checking for dictionary
        vec1[i] = 1 #changing the data from strings and giving them integer value for later calculations
    elif vec1[i] in dict2:
        vec1[i] = 2
    elif vec1[i] in dict3:
        vec1[i] = 3

#same as above for second vector
for i in range(len(vec2)):
    if vec2[i] in dict1:
        vec2[i] = 1
    elif vec2[i] in dict2:
        vec2[i] = 2
    elif vec2[i] in dict3:
        vec2[i] = 3

#if statements for checking the vectors if they are ordinal string and storing them as int
if np.array_equal(vec1, np.array(['1','2','3'])):
    vec1 = vec1.astype(int)

if np.array_equal(vec2, np.array(['1', '2', '3'])):
    vec2 = vec2.astype(int)

#function that checks for the data type, takes vector as argument
def check_vect(vect):
    att_type = 0

    isunique = np.unique(vect)  # checking for binary using unique method

    if isunique.size == 2:  # if there are only two unique numbers, its binary
        att_type = 2  # number 2 for binary

    if att_type != 2:  #if the vector does not consist of binary attributes
        for element in vect:
            #checking for numeric data types, can be ordinal (3) or numeric (4) (if not binary)
            if isinstance(element, (np.integer, np.floating)):

                #checking for ordinal (3) attributes by looking for pattern in ascending or descending order
                if np.all(vect[:-1] <= vect[1:]):
                    att_type = 3
                elif np.all(vect[:-1] >= vect[1:]):
                    att_type = 3

                #if the vector consists of numbers but is not an ordinal or binary then its numeric (4)
                if att_type != 3:
                    att_type = 4

            else:  #if not numeric then categorical, can be nominal (1) if not binary
                att_type = 1
    return att_type #returning the type of the attribute

#function that calulcates the distance/similarities between the two vectors for binary and nominal data type, takes both vectors for argument
def nom_bi_distance(arr1, arr2):

    match = 0 #initialising the variable for matches
    mismatch = 0 #initialising the variable for mismatches

    if len(arr1) == len(arr2): #an if statement to check if the vectors are the same size

        #for loop for checking each element in both vectors for matching with the other
        for i in range(len(arr1)):
            #checking for matches and mismatches and storing them in the right variables
            if arr1[i] == arr2[i]:
                match += 1 #counting matches
            elif arr1[i] != arr2[i]:
                mismatch += 1 #counting mismatches

        #suming all the compared matches and mismatches
        comp = match + mismatch
        #finding the similarity between the two vectors by dividing the total matches by comparisons
        sim = np.round(match/comp, 2)
    return sim #return the similarities

#funtion that takes in the two vectors and calculates the distance between numerical data types
def num_distance(arr1, arr2):
    difference = 0 #initialising variable for difference
    sum_of_diff = 0 #intialising variable for sum

    #checking to make sure the vectors are the same length
    if len(arr1) == len(arr2):

        #a for loop for each element in the vector
        for i in range(len(arr1)):
            #finding the absolute difference between vector one and vector two
            difference = abs(arr1[i] - arr2[i])
            #calculating the sum by raising the difference in the power of p(h) and adding it to the original sum
            sum_of_diff = pow(difference,len(arr1)) + sum_of_diff

        #calculating the final difference between the attributes by rooting the sum
        diff = np.round(pow(sum_of_diff, 1/len(arr1)), 2)

    return diff #return the final difference calculated between the two vectors

#function that takes the two vectors and calculates the difference between the ordinal data types
def ord_distance(arr1, arr2):
    difference = 0 #initialising the difference variable
    sum_of_diff = 0 #initialising the sum variable

    #if statement that checks if the vectors have the same length
    if len(arr1) == len(arr2):

        #for loop for each element in the vector
        for i in range(len(arr1)):
            #calculating the absolute difference between each index of the vectors
            difference = abs(arr1[i] - arr2[i])
            #calculating the sum by raising the difference by the power of two and adding it to already stored difference
            sum_of_diff = pow(difference,2) + sum_of_diff

        #finding the final difference by square rooting the sum
        diff = np.round(pow(sum_of_diff, 1/2),2)

    return diff #return the difference

# stores the return for each function that finds the type of the vectors for both vectors
type_vect1 = check_vect(vec1)
type_vect2 = check_vect(vec2)

# if they have the same type, this is the outpput for each data type, with the data type, similarity and distance
if type_vect1 == type_vect2:
    type_vects = type_vect1
    print("")
    print("Vector one is:", vec1, " and vector 2 is:",  vec2)
    print("")
    if type_vects == 1:
        print("-The data type is Nominal-")
        print("The Simple Matching Coefficient is",nom_bi_distance(vec1, vec2),", so vector 1 and vector 2 are", int(nom_bi_distance(vec1, vec2)*100),"% similar.")
    elif type_vects == 2:
        print("-The data type is Binary-")
        print("The Simple Matching Coefficient is",nom_bi_distance(vec1, vec2),", so vector 1 and vector 2 are", int(nom_bi_distance(vec1, vec2)*100),"% similar.")
    elif type_vects == 3:
        print("-The data type is Ordinal")
        print("The distance between the two vectors, calculated using Euclidean Distance, is ", ord_distance(vec1, vec2), ". ")
        print("Using Euclidean distance, the smaller the distance between two vectors, the more similar they are.")
    elif type_vects == 4:
        print("-The data type is Numeric-")
        print("The distance between the two vectors, using Minkowski Distance Formula is",num_distance(vec1, vec2), ". ")
        print("The smaller the distance between the two vectors, the more similar they are.")