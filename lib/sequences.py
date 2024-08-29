#!/usr/bin/env python3

def print_fibonacci(length):
       if length == 0:
        print([])
        return
    
       if length < 0:
        print("Length should be a positive integer.")
        return
    
       fibonacci_sequence = [0, 1]
    
       while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    # Adjust the sequence to the requested length
       print(fibonacci_sequence[:length])