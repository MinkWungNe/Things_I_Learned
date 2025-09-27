public class QuickSort {
    // Partition function
    static int partition(int[] arr, int low, int high) {
        
        // Chọn key là cuối dãy
        int pivot = arr[high];
        System.out.println(" pivot " + pivot);
        
        // Index of smaller element and indicates the right position of pivot found so far
        int i = low ;
        System.out.println("i = " + i);
        // Traverse arr[low..high] and move all smaller elements to the left side. Elements from low to i are smaller after every iteration
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                swap(arr, i, j);
                i++;
            }
        }
        
        // Move pivot after smaller elements and return its position
        swap(arr, i, high);  
        return i ;
    }

    // Swap function
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // The QuickSort function implementation
    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            System.out.println(low + " " + high);
            // pi is the partition return index of pivot
            int pi = partition(arr, low, high);

            // Recursion calls for smaller elements and greater or equals elements
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length;
      
        quickSort(arr, 0, n - 1);
        
        for (int val : arr) {
            System.out.print(val + " ");  
        }
    }

    /*   [10, 7, 8, 9, 1, 5]
     *   [ 1]    &    [10, 7, 8, 9]
     * 
     * 
     * 
     * 
     * 
     */
}
