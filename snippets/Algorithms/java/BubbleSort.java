import java.util.Scanner;

/**
 * Program Title: Bubble Sort Algorithm
 * Author: [Sreenivasulu-03]
 * Date: 2025-10-08
 *
 * Description: This program sorts an array of integers in ascending order
 * using the Bubble Sort algorithm. It repeatedly compares adjacent elements
 * and swaps them if they are out of order. Though not the fastest, it is one
 * of the simplest sorting techniques and great for learning basic sorting logic.
 *
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
 */

public class BubbleSort {

    /**
     * Sorts the array using the Bubble Sort algorithm.
     * @param arr The array to sort.
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;

        // Outer loop for number of passes
        for (int i = 0; i < n - 1; i++) {
            // Inner loop for comparisons
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap the two elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    /**
     * Prints the elements of the array.
     */
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter the elements:");

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("\nOriginal array:");
        printArray(arr);

        bubbleSort(arr);

        System.out.println("\nSorted array:");
        printArray(arr);

        sc.close();
    }
}
