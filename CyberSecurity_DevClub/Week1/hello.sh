#!/bin/bash

echo "Hello, World!"
echo "Current user: $(whoami)"
echo "Current working directory: $(pwd)"
echo "Current date: $(date)"

# variables
name="RedDragonNM"
age=18
current_date=$(date)

echo "My name is $name, I am $age years old."
echo "Today is: $current_date"

# user input
read -p "Enter your favorite color: " color
echo "Your favorite color is $color."

# conditionals
read -p "Enter a number: " number
if [ $number -gt 10]; then
    echo "The number is greater than 10"
elif [ $number -eq 10 ]; then
    echo "The number is equal to 10"
else
    echo "The number is less than 10"
fi

# loops
for i in {1..5}; do
    echo "Number: $i"
done


for file in *.md; do
    echo "File name: $file"
    head $file
done

counter=1
while [ $counter -le 5 ]; do
    echo "Counter: $counter"
    ((counter++))
done

# function
greet_user() {
    local name=$1
    echo "Hello $name"
}

calculate_sum() {
    local num1=$1
    local num2=$2
    local sum=$((num1 + num2))
    echo $sum
}

greet_user "RedDragonNM"
result=$(calculate_sum 5 10)
echo "Sum: $result"
