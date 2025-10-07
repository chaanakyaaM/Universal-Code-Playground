import java.util.Scanner;

/**
 * Program Title: Merge Sort Algorithm
 * Author: [Sreenivasulu-03]
 * Date: 2025-10-07
 *
 * Description: This program sorts an array of integers using the Merge Sort
 * algorithm. It demonstrates recursion, divide-and-conquer strategy, and
 * array manipulation in Java.
 *
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 */
public class MergeSort {

    /**
     * Sorts an array using Merge Sort algorithm.
     * @param arr The array to sort.
     * @param left The starting index of the array segment.
     * @param right The ending index of the array segment.
     */
    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;

            // Sort first half
            mergeSort(arr, left, mid);
            // Sort second half
            mergeSort(arr, mid + 1, right);

            // Merge the sorted halves
            merge(arr, left, mid, right);
        }
    }

    /**
     * Merges two sorted subarrays into a single sorted segment.
     * @param arr The array containing the subarrays.
     * @param left Start index of the first subarray.
     * @param mid End index of the first subarray.
     * @param right End index of the second subarray.
     */
    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        // Copy data to temp arrays
        for (int i = 0; i < n1; ++i)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left;

        // Merge temp arrays back into arr
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        // Copy remaining elements of L[], if any
        while (i < n1) {
            arr[k++] = L[i++];
        }

        // Copy remaining elements of R[], if any
        while (j < n2) {
            arr[k++] = R[j++];
        }
    }

    /**
     * Prints the elements of an array.
     * @param arr The array to print.
     */
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the number of elements: ");

            while (!sc.hasNextInt()) {
                System.out.print("Invalid input! Enter a numeric value: ");
                sc.next();
            }
            int n = sc.nextInt();
            int[] arr = new int[n];

            System.out.println("Enter " + n + " integers:");
            for (int i = 0; i < n; i++) {
                while (!sc.hasNextInt()) {
                    System.out.print("Invalid input! Enter an integer: ");
                    sc.next();
                }
                arr[i] = sc.nextInt();
            }

            mergeSort(arr, 0, n - 1);

            System.out.println("Sorted array:");
            printArray(arr);

        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
