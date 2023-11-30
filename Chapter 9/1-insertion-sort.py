def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    # Aloitetaan arrayn toisesta elementistä, eli index 1
    for key_index in range (1, len(array)):
        
        # Tallennetaan läpi käytävän indexin arvo
        key = array[key_index]
        
        # Käydään läpi jo lajiteltu osa taulukosta (eli vasemmalle) jotta löydettäisiin oikea paikka key:lle
        # Looppia jatketaan niin kauan kun back index on suurempi kuin nolla ja kun back index - 1 on suurempi kuin key
        back_index = key_index
        while back_index > 0 and array[back_index - 1] > key:
            back_index -= 1
        
        # Jos löydetään paikka jonne asetetaan, siirretään toisia arvoja oikellae
        if back_index < key_index:
            array[back_index + 1 : key_index + 1] = array[back_index : key_index]
            
            #Asetetaan key oikeaan paikkaan
            array[back_index] = key
