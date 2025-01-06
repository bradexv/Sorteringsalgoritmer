def sort(A):
   
#Implementering av insertion sort
    for i in range (1, len(A)):
        j = i;
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1];
            j = j - 1;

    return A;