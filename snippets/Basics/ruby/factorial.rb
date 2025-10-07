# Title: Iterative factorial
# Topic: Basics
# Language: ruby
# Example: see bottom
# Iterative factorial - placeholder in ruby
# Function to calculate factorial iteratively
def factorial_iterative(n)
  result = 1
  for i in 1..n
    result *= i
  end
  result
end

# ---------- User interaction ----------
puts "Enter a non-negative integer:"
input = STDIN.gets&.chomp

begin
  n = Integer(input)
rescue ArgumentError, TypeError
  puts "Invalid input. Please enter a valid non-negative integer."
  exit 1
end

if n < 0
  puts "Please enter a non-negative integer."
  exit 1
end

# Compute factorial
result = factorial_iterative(n)

# Display result
puts "\nFactorial of #{n} is: #{result}"
