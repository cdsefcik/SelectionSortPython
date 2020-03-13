#Python Selection Sort

def selectionSort(array):
    
    for i in range(len(array)):

        minValue = i

        for k in range(i + 1, len(array)):
            if array[minValue] > array[k]:
                minValue = k

        array[i], array[minValue] = array[minValue], array[i]

    return array

                
