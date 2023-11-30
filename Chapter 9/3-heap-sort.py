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

def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    # Heapify, eli ensin lasketaan ensimmäinen indexi, joka ei ole lehti, lehtisilmukat alkavat puolesta välistä eteenpäin
    # start käy läpi taulukon idexejä, aloittaen viimeisestä solmusta jolla on lapsia, edeten juureen asti
    # shift downilla varmistetaan että solmu "start" täyttää maksimikeon ehdot, siirtämällä sitä tarvittaessa alaspäin
    for start in range(len(array) // 2 - 1, -1, -1):
        sift_down(array, start, len(array)-1)

    # Keko palauttaa suurimmat arvot, sijoitetaan taulukon loppuun, tässä viimeinen indexi
    end = len(array)-1 

    # Loopataan niin kauan kun keko ei ole tyhjä
    while end > 0:

        # Vaihdetaan juuren ja endin paikkja
        array[0], array[end] = array[end], array[0]

        # Vähennetään yksi alkio keosta
        end -= 1

        # Sift downilla sink juuren arvo
        sift_down(array, 0, end)

