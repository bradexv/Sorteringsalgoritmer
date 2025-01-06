def sort(arrayToSort):
   
    if (len(arrayToSort) <= 1):
        return arrayToSort;

    
    index = len(arrayToSort) // 2;
   
    firstHalf = sort(arrayToSort[0 : (index)]); 
    secondHalf = sort(arrayToSort[index : len(arrayToSort)]);
    
    return Merge(firstHalf, secondHalf, arrayToSort);
    



def Merge(array1, array2, array):
    i = 0;
    j = 0;
    while i < len(array1) and (j < len(array2)):
        if array1[i] <= array2[j]:
            array[i + j] = array1[i];
            i = i + 1;

        else:
            array[i + j] = array2[j];
            j = j + 1;

    while i < len(array1):
        array[i + j] = array1[i];
        i = i + 1;

    while j < len(array2):
        array[i + j] = array2[j];
        j = j + 1;

    return array;
	
	