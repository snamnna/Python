def interpolation_search(array, value, start = None, end = None):
    """
    Performs an Interpolation search in the the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    # Asetetaan alku ja loppu jos niitä ei ole vielä asetettu
    if start is None:
        start = 0
    
    if end is None:
        end = len(array) - 1
        
    # Lasketaan uusi modpoint teoriassa annetulla kaavalla
    middle = start + int((end - start) * ((value-array[start])/(array[end]-array[start])))
    
    # Jos middle on pienempi kuin start tai suurempi kuin end
    if middle < start or middle > end:
        return None
    
    # Jos osuttiin heti oikeaan, palautetaan middle
    if array[middle] == value:
        return middle
    
    # Jos etsitty arvo on pienempi kuin middle ja sen vasemmalla puolella on vähintään yksi, etsitään vasemmalta
    if value < array[middle] and middle >= start + 1:
        return interpolation_search(array, value, start = start, end = middle - 1)
    
    #Jos etsitty arvo on suurempi kuin middle ja sen jälkeen oikealla on vähintään yksi, etsitään oikealta puolelta
    if value > array[middle] and middle <= end - 1:
        return interpolation_search(array, value, start = middle + 1, end = end)
    
    # Palautetaan tyhjä jos numeroa ei löytynyt
    return None