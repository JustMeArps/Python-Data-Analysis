import numpy as np

#===these vectors are for testing 2D Nominal data type===
#---this is an array with NUMERIC data type--- (uncomment line 5-15)
the_matrix = np.array([[1, 2, 23],
                     [50, 97, 40],
                     [72, 15, 13],
                     [69, 74, 88],
                     [39, 86, 28],
                     [70, 0, 65],
                     [55, 34, 53],
                     [35, 99, 42],
                     [40, 15, 4],
                     [53, 74, 34]])
mixed_matrix = False

# #---this is an array with NOMINAL data type--- (uncomment line 18-28)
# the_matrix = np.array([['red','blue','yellow'],
#                     ['green','green','yellow'],
#                     ['blue','red','yellow'],
#                     ['yellow','yellow','blue'],
#                     ['red','green','blue'],
#                     ['yellow','red','green'],
#                     ['green','blue','red'],
#                     ['yellow','blue','green'],
#                     ['blue','yellow','yellow'],
#                     ['red','green','yellow']])
# mixed_matrix = False

#---this is an array with BINARY data type--- (uncomment line 31-41)
# the_matrix = np.array([['m', 'm', 'f'],
#                        ['f', 'm', 'f'],
#                        ['m', 'f', 'm'],
#                        ['f', 'm', 'm'],
#                        ['f', 'm', 'm'],
#                        ['m', 'f', 'f'],
#                        ['m', 'm', 'm'],
#                        ['f', 'f', 'f'],
#                        ['m', 'f', 'f'],
#                        ['f', 'm', 'f']])
# mixed_matrix = False

#---this is an array with ORDINAL data type--- (uncomment line 44-54)
# the_matrix = np.array([[1, 2, 3],
#                     [5, 8, 12],
#                     [16, 17, 19],
#                     [30, 34, 46],
#                     [49, 49, 52],
#                     [56, 57, 57],
#                     [70, 73, 81],
#                     [83, 85, 90],
#                     [94, 152, 153],
#                     [235, 362, 453]])
# mixed_matrix = False

#---this is an array with MIXED data type---(uncomment line 57-67)
# the_matrix = np.array([[4.8, "red", 1],
#                         [7.2, "blue", 0],
#                         [6.1, "green", 1],
#                         [5.5, "red", 0],
#                         [8.3, "blue", 1],
#                         [3.2, "green", 0],
#                         [9.0, "red", 1],
#                         [4.7, "blue", 0],
#                         [2.9, "green", 1],
#                         [5.9, "red", 0]])
# mixed_matrix = True

#function that checks for the data type, takes vector as argument (almost same as question 1)
def check_metrix(metriX):
    att_type = 0 #this is to store the data type (1)nominal, 2)binary, 3)ordina, 4)numeric

    flattened = metriX.flatten() #making the array 1D for testing purposes

    #to make the matrix 1D only for testing purposes
    isunique = np.unique(flattened)  # checking for binary using unique method


    if isunique.size == 2:  # if there are only two unique numbers, its binary
        att_type = 2  # number 2 for binary


    if att_type != 2:  #if the vector does not consist of binary attributes
        for element in flattened:
            #checking for numeric data types, can be ordinal (3) or numeric (4) (if not binary)
            if isinstance(element, (np.integer, np.floating)):

                #checking for ordinal (3) attributes by looking for pattern in ascending or descending order
                if np.all(metriX[:-1] <= metriX[1:]):
                    att_type = 3
                elif np.all(metriX[:-1] >= metriX[1:]):
                    att_type = 3

                #if the vector consists of numbers but is not an ordinal or binary then its numeric (4)
                if att_type != 3:
                    att_type = 4
            else:  #if not numeric then categorical, can be nominal (1) if not binary
                att_type = 1

    return att_type #returning the type of the attribute

#function that takes the array and computes the distance between the ordinal data or numeric data types using Minkowski method
def num_ord_metrix(matriX):
    #creating empty array to store the simple distance matrix
    dis_matrix = np.empty((10,10))
    h=2 #creating h as 2 for Euclidean distance

    #nested for loop to find the pairs in the array
    for i in range(len(matriX)):
        for j in range(len(matriX)):
            dis_matrix[i,j] = np.round(np.power(np.sum(np.power(np.abs(matriX[i] - matriX[j]), h)), 1/h),1) #calculating and storing the distance
    return dis_matrix #returning the distance

#function that takes the array and computes the distance between the binary data or nominal data types using coefficient method
def nom_bi_metrix(matriX):
    # creating empty array to store the simple distance matrix
    dis_matrix = np.empty((10, 10))
    match = 0 #creating match variable with value of 0

    #nested for loop to find and compare each pair
    for i in range(len(matriX)):
        for j in range(len(matriX)):
            dis_matrix[i,j] = np.round((1-np.sum(matriX[i] == matriX[j])/3),1) #calculating the similarities

    return dis_matrix #returning the similarity

#function that takes the array and normalizes all the attributes into floating points between 0 and 1
def mixed_matrix_distance(matriX):
    #this is to tell if the array contains mixed types
    if mixed_matrix == True:
        #splitting the 2d array into 3 individual arrays
        split_array = np.array_split(matriX, 3, axis=1)
        num_matrix = split_array[0].astype(float) #storing each split into individual arrays
        nom_matrix = split_array[1]
        bin_matrix = split_array[2]

        #this block of code is normalizing the numeric data to make sure its between 1 and 0
        num_norm = np.empty((1,10)) #creting empty array to later store the normalized values of numeric data type
        max_num = max(num_matrix) #finding the maximum value
        min_num = min(num_matrix) #finding the minimum value
        num_norm = np.round((num_matrix - min_num)/(max_num-min_num), 1) #calculaing the normalized values and rounding it to 1 decimal places


        #this is for labeling and normalizing the nominal data type
        unique_nom = np.unique(nom_matrix) #finding the unique words that repeat and only storing each one time
        labels = np.arange(len(unique_nom)) #making array that stores labels (number 1 to n) for the size of the nominal data type

        mapping = dict(zip(unique_nom, labels)) #creating dictionary that maps the nominal values with numeric labels
        nom_mapped = np.empty(nom_matrix.shape, dtype=int) #creating empty array to later store the mapped values that correspond with the nominal data
        nom_mapped = np.vectorize(mapping.get)(nom_matrix) #assigning the label to its corresponding nominal data

        nom_norm = np.empty((1, 10)) #an empty array that stores normalized labels for nominal data
        max_nom = max(nom_mapped) #finding the maximum
        min_nom = min(nom_mapped) #finding the minimum
        nom_norm = np.round((nom_mapped - min_nom) / (max_nom - min_nom),1) #calculating the normalized values

        #storing them back together into a 2d array
        normalized_matrix = np.empty((10,3))#creating an empty 2d array to store the normalized mixed data
        normalized_matrix = np.column_stack((num_norm, nom_norm, bin_matrix.astype(np.float16))) #putting the normalized numeric, nominal and binary back into an array

        dis_matrix = num_ord_metrix(normalized_matrix) #calling the function to calculating numeric distance and store into single distance matrix

        return dis_matrix


#outputs that check for each type
if check_metrix(the_matrix) == 1 and mixed_matrix == False:
    print("")
    print("This is a single distance matrix with nominal data")
    print(nom_bi_metrix(the_matrix))
elif check_metrix(the_matrix) == 2 and mixed_matrix == False:
    print("")
    print("This is a single distance matrix with binary data")
    print(nom_bi_metrix(the_matrix))
elif check_metrix(the_matrix) == 3 and mixed_matrix == False:
    print("")
    print("This is a single distance matrix with ordinal data")
    print(num_ord_metrix(the_matrix))
elif check_metrix(the_matrix) == 4 and mixed_matrix == False:
    print("")
    print("This is a single distance matrix with numeric data.")
    print(num_ord_metrix(the_matrix))
    print("")
elif mixed_matrix == True:
    print("")
    print("This is a single distance matrix with numeric data.")
    print(mixed_matrix_distance(the_matrix))
    print("")
