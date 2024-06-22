def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the area with the current pair of lines
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)
        
        # Move the pointers to try and find a larger area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test cases
print(max_area([1, 5, 4, 3]))  # Output: 6
print(max_area([3, 1, 2, 4, 5]))  # Output: 12
