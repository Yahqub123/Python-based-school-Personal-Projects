#Name: Yahqub Oyebola
#Objective: The goal is to sort a list in ascending order by splitting it into two halves then sorting each.

def mergeSort(alist):
    if len(alist) > 1:
        # I check if the size of 'alist' is greater that one then I split 'alist' into 2 different list.
        # Then, I store the first half of the elements in 'alist' into the 'Left_list_of_elements' variable and I
        # store the second half of 'alist' values into the 'Right_list_of_elements' variable below.
        Left_list_of_elements = alist[:(len(alist)//2)]
        Right_list_of_elements = alist[len(alist)//2:]# I use the ':' symbol to seperate my range of elements

        mergeSort(Left_list_of_elements) # Then I recursively call the meregeSort() function just so i can split my divided
                                        # sub_lists (both left and right) into a smaller list of elements
        mergeSort(Right_list_of_elements)
        pos_of_left_list= 0
        pos_of_right_list = 0
        position_in_alist = 0

        #The following while loops compare the values of elements in the 'left_list' to the values in the 'right_list'
        #to see which is the lower or greater of the two values then adds these values to the coresponding
        #positions in 'alist'.

        while pos_of_left_list < len(Left_list_of_elements) and pos_of_right_list < len(Right_list_of_elements):
            if Left_list_of_elements[pos_of_left_list] < Right_list_of_elements[pos_of_right_list]:
                alist[position_in_alist]= Left_list_of_elements[pos_of_left_list]
                pos_of_left_list += 1
                position_in_alist += 1
            else: #if value in the right_list is bigger, then set that to 'alist' at that position
                alist[position_in_alist] = Right_list_of_elements[pos_of_right_list]
                pos_of_right_list += 1
                position_in_alist += 1

        while  pos_of_left_list < len(Left_list_of_elements):
            alist[position_in_alist] = Left_list_of_elements[pos_of_left_list]
            position_in_alist += 1
            pos_of_left_list += 1

        while pos_of_right_list < len(Right_list_of_elements):
            alist[position_in_alist] = Right_list_of_elements[pos_of_right_list]
            position_in_alist += 1
            pos_of_right_list += 1
alist = [54,26,93,17,77,31,900,55,20]
mergeSort(alist)
print(alist)
