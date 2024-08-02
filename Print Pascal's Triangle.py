def generate_pascals_triangle(rows):
    triangle = []

    for i in range(rows):
        # Start each row with 1
        row = [1] * (i + 1)
        
        # Each element (except the first and last) is the sum of the two elements above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Append the row to the triangle
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * len(triangle[-1])))

# Main code
if __name__ == "__main__":
    # Input from the user
    num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
    
    # Generate Pascal's Triangle
    triangle = generate_pascals_triangle(num_rows)
    
    # Print Pascal's Triangle
    print_pascals_triangle(triangle)
