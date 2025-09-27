public class MergeSort {
    public static void mergeSort(int[] arr)
    {
        int length = arr.length;
        if (length == 1) return;

        // Get mid length
        int mid = length / 2;

        // Split arr into 2 half arrays
        int[] left = new int[mid];              // size of first half
        int[] right = new int[length - mid];    // size of other half

        // Two index for left and right
        int i = 0;
        int j = 0;

        for (;i < length; i++)
        {
            if (i < mid)
            {
                left[i] = arr[i];
            }
            else
            {
                right[j] = arr[i];
                j++;
            }
        }

        mergeSort(left);
        mergeSort(right);
        Merge(left, right, arr);

    }

    public static void Merge(int[] left, int[] right, int[] arr)
    {
        int leftSize = arr.length / 2;
        int rightSize = arr.length - leftSize;
        int i = 0, l = 0, r = 0;

        while (l < leftSize && r < rightSize)
        {
            if (left[l] < right[r])
            {
                arr[i] = left[l];
                i++;
                l++;
            }
            else
            {
                arr[i] = right[r];
                i++;
                r++;
            }
        }

        while (l < leftSize)
        {
            arr[i] = left[l];
            i++;
            l++;
        }

        while (r < rightSize)
        {
            arr[i] = right[r];
            i++;
            r++; 
        }
    }
    public static void main(String[] args) {
        int[] arr = {8, 2, 5, 3, 4, 7, 6, 1};

        mergeSort(arr);
        // Print
        for (int i : arr)
        {
            System.out.print(i + " ");
        }
    }
}
