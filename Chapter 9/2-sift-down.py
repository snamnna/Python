def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure
    
    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node
    
    Returns: None
    """
    # Määritellään tällä hetkellä käsiteltäväksi se, josta aloitetaan
    current = start
    
    # Loopataan niin kauan, kun currentin vasemmalla puolella on jotain, mihin verrata
    while (left_child := 2 * current + 1) <= end:
        swap_index = current

        # Jos vasen lapsi on suurempi kuin currentin arvo, asetetaan swap osoittamaan vasemman lapsen arvoon
        if array[swap_index] < array[left_child]:
            swap_index = left_child
            
        # Lasketaan lapsen arvon binääri
        right_child = 2 * current + 2
        
        # Jos oikea lapsi on pienempi tai yhtäsuuri kuin loppu ja swappi on pienempi kuin right child, swapiksi valitaan right child
        if right_child <= end and array[swap_index] < array[right_child]:
            swap_index = right_child

        # Jos swappi ei ole muuttunut, lopetetaan
        if swap_index == current:
            return

        # Vaihdetaan nykyisen indeksin ja swap_indexin arvot keskenään
        array[current], array[swap_index] = array[swap_index], array[current]

        # Päivitetään current muuttujan arvoksi swap_index
        current = swap_index