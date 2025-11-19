# Python - Everything is object

A project exploring Python's object model, mutability, immutability, references, and how Python handles different types of objects.

## Description

This project examines the fundamental concepts of how Python works with objects. It explores the differences between mutable and immutable types, object identity vs equality, references, aliases, and how Python passes variables to functions.

## Learning Objectives

By the end of this project, you should be able to explain:

- What is an object
- The difference between a class and an object or instance
- The difference between immutable and mutable objects
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (memory address in CPython)
- What are the built-in mutable types
- What are the built-in immutable types
- How Python passes variables to functions

## Key Concepts

### Objects and Values
In Python, everything is an object. Understanding how objects are created, referenced, and modified is crucial.

### Mutable vs Immutable
- **Immutable types**: int, float, str, tuple, frozenset
- **Mutable types**: list, dict, set

### Identity vs Equality
- `==` checks if two objects have the same value (equality)
- `is` checks if two variables point to the same object (identity)

### References and Aliasing
```python
a = [1, 2, 3]
b = a  # b is an alias for a
a[0] = 'x'
print(b)  # ['x', 2, 3]
```

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- First line of all files: `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable

### .txt Answer Files
- Only one line
- No Shebang on the first line
- All files should end with a new line

## Project Structure

| Task | File | Description |
|------|------|-------------|
| 0 | 0-answer.txt | Function to print the type of an object |
| 1 | 1-answer.txt | Function to get variable identifier |
| 2 | 2-answer.txt | Do two different integers point to the same object? |
| 3 | 3-answer.txt | Do two identical integers point to the same object? |
| 4 | 4-answer.txt | Assignment: do variables point to same object? |
| 5 | 5-answer.txt | Arithmetic operation: same object? |
| 6 | 6-answer.txt | String equality with `==` |
| 7 | 7-answer.txt | String identity with `is` (same reference) |
| 8 | 8-answer.txt | String equality (different variables) |
| 9 | 9-answer.txt | String identity (different variables) |
| 10 | 10-answer.txt | List equality with `==` |
| 11 | 11-answer.txt | List identity with `is` |
| 12 | 12-answer.txt | List equality (same reference) |
| 13 | 13-answer.txt | List identity (same reference) |
| 14 | 14-answer.txt | List append mutation |
| 15 | 15-answer.txt | List concatenation reassignment |
| 16 | 16-answer.txt | Integer incrementation in function |
| 17 | 17-answer.txt | List modification in function |
| 18 | 18-answer.txt | List reassignment in function |
| 19 | 19-copy_list.py | Function to copy a list |
| 20-28 | 20-28-answer.txt | Questions about tuples, identity, and mutability |

## Repository

- **GitHub repository**: holbertonschool-higher_level_programming
- **Directory**: python-everything_is_object

## Author

Victor - Holberton School Student
