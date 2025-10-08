#!/usr/bin/env ruby
# fibonacci.rb
# Title: Iterative + recursive Fibonacci
# Topic: Basics
# Language: ruby
# Example: see bottom

# Iterative approach: returns an array with the first n Fibonacci numbers
def fibonacci_iterative(n)
  a, b = 0, 1
  series = []
  n.times do
    series << a
    a, b = b, a + b
  end
  series
end

# Naive recursive approach: returns the single Fibonacci number for n
# (educational; exponential time for large n)
def fibonacci_recursive(n)
  return 0 if n == 0
  return 1 if n == 1
  fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
end

# Memoized recursive approach: fast, suitable for larger n
def fibonacci_memo(n, memo = {0 => 0, 1 => 1})
  return memo[n] if memo.key?(n)
  memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
  memo[n]
end

def fibonacci_memo_series(n)
  (0...n).map { |i| fibonacci_memo(i) }
end

# ---------- User interaction ----------
puts "Enter number of terms (non-negative integer):"
input = STDIN.gets&.chomp

begin
  n = Integer(input)
rescue ArgumentError, TypeError
  puts "Invalid input. Please run again and enter a non-negative integer."
  exit 1
end

if n < 0
  puts "Please enter a non-negative integer."
  exit 1
end

puts "Choose method: iterative / recursive / memo / both (default: both)"
method = STDIN.gets&.chomp&.strip&.downcase
method = "both" if method.nil? || method.empty?

# Warn about naive recursion performance
if method == "recursive" && n > 35
  puts "Warning: naive recursive method is exponential and may be very slow for n > ~35. Consider 'memo' or 'iterative'."
end

puts

if method == "iterative" || method == "both"
  puts "Fibonacci Series (Iterative):"
  puts fibonacci_iterative(n).join(", ")
  puts
end

if method == "recursive" || method == "both"
  puts "Fibonacci Series (Recursive - naive, prints terms):"
  puts (0...n).map { |i| fibonacci_recursive(i) }.join(" ")
  puts
end

if method == "memo" || method == "both"
  puts "Fibonacci Series (Recursive with memoization):"
  puts fibonacci_memo_series(n).join(", ")
  puts
end
