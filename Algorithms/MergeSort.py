class MergeSort:

    def mergeSort(arr):

        if len(arr) > 1:

            # Finding the mid of the array
            mid = len(arr)//2

            # Dividing the array elements
            L = arr[:mid]

            # into 2 halves
            R = arr[mid:]

            # Sorting the first half
            MergeSort.mergeSort(L)

            # Sorting the second half
            MergeSort.mergeSort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):

                if L[i] <= R[j]:

                    arr[k] = L[i]

                    i += 1

                else:

                    arr[k] = R[j]

                    j += 1

                k += 1

            # Checking if any element was left
            while i < len(L):

                arr[k] = L[i]

                i += 1

                k += 1

            while j < len(R):

                arr[k] = R[j]

                j += 1

                k += 1

    def printList(arr):

        for i in range(len(arr)):

            print(arr[i], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Sorted Array is: ", end="\n")
    MergeSort.mergeSort(arr)
    MergeSort.printList(arr)