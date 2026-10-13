/** This class contains utility methods for searching integer arrays. */
class IntArraySearching 
{
    private:
        // Prevents instantiation of this class.
        IntArraySearching() { }

    public:    
        /**
         * Searches the specified array for the specified key
         * using the sequential search algorithm.
         * @param arr The array to be searched
         * @param size The size of the array
         * @param key The value to be searched for
         * @return index of the key if found; otherwise, -1
         */
        static int sequentialSearch(int arr[], int size, int key) 
        {
            for (int idx = 0; idx < size; idx++) 
            {
                if (key == arr[idx])
                    return idx;  // Key found
            }
    
            return -1;  // Key not found
        }
    
        /**
         * Searches the specified array for the specified key
         * using the binary search algorithm.
         * Precondition: The array is sorted in ascending order.
         * @param arr The array to be searched
         * @param size The size of the array
         * @param key The value to be searched for
         * @return index of the key if found.
         * Otherwise, the index will be (-(insertion point) - 1)
         */
        static int binarySearch(int arr[], int size, int key) {
            int lo = 0;
            int hi = size - 1;
    
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
    
                if (key < arr[mid])
                    hi = mid - 1;
                else if (key > arr[mid])
                    lo = mid + 1;
                else
                    return mid;  // Key found
            }
    
            return -(lo + 1);  // Key not found
        }
};
