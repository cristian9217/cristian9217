/** This class contains utility methods for sorting integer arrays. */
class IntArraySorting 
{
    private:
        // Prevents instantiation of this class.
        IntArraySorting() {}
    
         /**
          * Swaps the two elements of the specified array located at the specified indexes.
          * @param arr The array with the elements to be swapped
          * @param idx1 The index of the first element
          * @param idx2 The index of the second element
          */
         static void swap(int arr[], int idx1, int idx2) 
         {
              int temp = arr[idx1];
              arr[idx1] = arr[idx2];
              arr[idx2] = temp;
         }
    
    public:
        /**
         * Sorts the elements of the specified array using the bubble sort algorithm.
         * @param arr The array to be sorted
         */
        static void bubbleSort(int arr[], int size) 
        {
            bool swapped = true;
        
            while (swapped) {
                swapped = false;
        
                for (int idx = 0; idx < size - 1; idx++) {
                    if (arr[idx] > arr[idx + 1]) {
                        swap(arr, idx, idx + 1);
                        swapped = true;
                    }
                }
            }
        }

       /**
        * Sorts the elements of the specified array using the selection sort algorithm.
        * @param arr The array to be sorted
        */
       static void selectionSort(int arr[], int size) 
       {
            for (int pos = 0; pos < size - 1; pos++) {
                int minIdx = pos;
        
                for (int idx = pos + 1; idx < size; idx++) {
                    if (arr[idx] < arr[minIdx]) {
                        minIdx = idx;
                    }
                }
        
                if (minIdx != pos) {
                    swap(arr, minIdx, pos);
                }
            }
        }

       /**
        * Sorts the elements of the specified array using the insertion sort algorithm.
        * @param arr The array to be sorted
        */
        static void insertionSort(int arr[], int size) 
        {
            for (int idx = 1; idx < size; idx++) {
                int pos = idx;
                int tempElem = arr[idx];
      
                while (pos > 0 && arr[pos - 1] > tempElem) {
                    arr[pos] = arr[pos - 1];
                    pos--;
                }
      
                arr[pos] = tempElem;
            }
        }

};
