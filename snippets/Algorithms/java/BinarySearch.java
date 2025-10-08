import java.util.Scanner;

/**
 * Program Title: Binary Search Algorithm
 * Author: [Sreenivasulu-03]
 * Date: 2025-10-07
 *
 * Description: This program implements the Binary Search algorithm to find
 * the position of a target element in a sorted array. It demonstrates
 * arrays, loops, and efficient search algorithms in Java.
 *
 * Time Complexity: O(log n)
 * Space Complexity: O(1)
 */
public class BinarySearch {

    /**
     * Performs binary search on a sorted array.
     * @param arr The sorted array.
     * @param target The value to search for.
     * @return The index of the target if found, otherwise -1.
     */
    public static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1; // Target not found
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the number of elements (sorted array): ");

            while (!sc.hasNextInt()) {
                System.out.print("Invalid input! Enter a numeric value: ");
                sc.next();
            }
            int n = sc.nextInt();
            int[] arr = new int[n];

            System.out.println("Enter " + n + " sorted integers:");
            for (int i = 0; i < n; i++) {
                while (!sc.hasNextInt()) {
                    System.out.print("Invalid input! Enter an integer: ");
                    sc.next();
                }
                arr[i] = sc.nextInt();
            }

            System.out.print("Enter the element to search for: ");
            while (!sc.hasNextInt()) {
                System.out.print("Invalid input! Enter an integer: ");
                sc.next();
            }
            int target = sc.nextInt();

            int result = binarySearch(arr, target);
            if (result != -1) {
                System.out.println("Element found at index: " + result);
            } else {
                System.out.println("Element not found in the array.");
            }

        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
