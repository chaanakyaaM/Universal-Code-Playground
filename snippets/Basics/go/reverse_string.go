// Title: Reverse a string
// Topic: Basics
// Language: go
// Example: see bottom

// Reverse a string - placeholder in go

// Time Complexity: O(n)
// Space Complexity: O(n)

package main

import "fmt"

// reverse_string reverses the input string and returns the reversed result.
func reverse_string(s string) string {
    // Convert the string to a rune slice to support Unicode.
    str := []rune(s)
    // Use two pointers to swap runes from start and end.
    for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
        str[i], str[j] = str[j], str[i]
    }
    // Convert the reversed rune slice back to a string.
    return string(str)
}

func main() {
    // Input string
    input := "Hacktoberfest 🌍"
    // Print the reversed string
    fmt.Println(reverse_string(input))
}