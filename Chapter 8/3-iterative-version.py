def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    # Määritellään alku ja loppu
    start = 0
    end = len(array) - 1
    
    # Loopataan niin kauan kun start on endin vasemmalla puolella, eli pienempi
    while start <= end:
        # Lasketaan missä on keskikohta
        middle = start + (end - start + 1) // 2
        
        # Jos etsitty löydetään heti keskeltä, palautetaan se
        if array[middle] == value:
            return middle
        
        # Jos etsittävä on pienempi kuin keskikohta
        if value < array[middle]:
            end = middle - 1 
            
        # Jos etsittävä on suurempi kuin keskikohta
        if value > array[middle]:
            start = middle + 1
            
    # Palautetaan None jos haluttua ei ikinä löydetty
    return None