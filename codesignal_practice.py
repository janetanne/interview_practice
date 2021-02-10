######## adjacentElementsProduct ########
# Given an array of integers, find the pair of adjacent elements 
# that has the largest product and return that product.

### first solution ###  
def adjacent_elements_product(input_array):
    """Given a list of integers, return the largest product of adjacent elements."""

    product_list = []

    for x_index, x in enumerate(input_array):
        if x_index < len(input_array) - 1:
            new_product = x * input_array[x_index+1]
            product_list.append(new_product)
    
    return max(product_list)

# feedback: storing a whole list when i really need the max. no need to keep the list! hogs memory!

### second solution ###
def adjacent_elements_product2(input_array):
    """Given a list of integers, return the largest product of adjacent elements."""
    
    max_product = None
        
    for x_index, x in enumerate(input_array):
        if x_index < len(input_array) - 1:
            new_product = x * input_array[x_index+1]
            
            if max_product is None or new_product > max_product:
                max_product = new_product
            
    return max_product

# feedback: the if statement for checking the index against the array length is not necessary

### third solution ###

def adjacent_elements_product3(input_array):
    """Given a list of integers, return the largest product of adjacent elements."""
    
    max_product = None
        
    for i in range(len(input_array)-1):
        new_product = input_array[i] * input_array[i+1]
        
        if max_product is None or new_product > max_product:
            max_product = new_product
                
    return max_product

# feedback: i personally like this solution the best as it's easy to understand in different languages

### fourth solution
def adjacent_elements_product4(input_array):
    return max([input_array[i] * input_array[i+1] for i in range(len(input_array)-1)])

# feedback: this uses list comprehension and is definitely the most elegant. 
# but would i be able to understand it 10 years from now? probably not.

######## shapeArea ########