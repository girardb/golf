### python version: 3.7
### pytest version: 3.10.0
# Run tests
```python
pytest challenge1_test.py
pytest challenge2_test.py
pytest challenge3_test.py
pytest challenge4_test.py
```

# First Challenge:
Accept two strings as input and return a single string with the second phrase exposed in the first one.

Example:
```
Input: She believed, He lied
>>> S[he] be[lie]ve[d]
```

# Second Challenge:
Accept a string as input and return an ascii art frame surrounding the sentence. The area and perimeter of the frame should be as small as possible.

Example:
```
input: Hello World in a frame

>>>
***************
* Hello World *
* in a frame  *
***************
```

# Third Challenge:
A two dimensional matrix is given to the algorithm. Sort each row and then sort the matrix according to the sum of the elements in the row.

Example:
```
input: 
[
    [ 2 4 1 ],
    [ 3 1 2 ],
    [ 1 1 1 ],
    [ 3 3 2 ]
]

>>>
[
    [ 1 1 1 ],
    [ 1 2 3 ],
    [ 1 2 4 ],
    [ 2 2 3 ]
] 
```

# Fourth Challenge:
Transform an equation with our normal conventions into an equation following the Reverse Polish notation.

Examples:
```
Input: (3 * 4) * 2 + 1
>>> 3 4 * 2 * 1 +
Input: (5 - 6) * 2 / (1 + 3)
>>> 5 6 - 2 * 1 3 + /
Input: (4 - 1) / (2 - 3)
>>> 4 1 - 2 3 - /
Input: ((5 - 3) * ((4 / 2 - 1) * 2))
>>> 5 3 - 4 2 / 1 - 2 * *
Input: (4 ^ 2) * 3
>>> 4 2 ^ 3 *
Input: 4 ^ (3 - 1)
>>> 4 3 1 - ^
```


