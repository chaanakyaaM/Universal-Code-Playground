// Title: Reverse a string
// Topic: Basics
// Language: go
// Example: see bottom

// Reverse a string - placeholder in go

package main

import "fmt"

func reverseString(s string) string {
    // Convert the string to a byte slice since strings are immutable in Go.
    str := []byte(s)
    // Use two pointers to swap characters from start and end.
    for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
        str[i], str[j] = str[j], str[i]
    }
    // Convert the reversed byte slice back to a string.
    return string(str)
}

func main() {
    // Input string
    input := "Hacktoberfest"
    // Print the reversed string
    fmt.Println(reverseString(input))
}	
