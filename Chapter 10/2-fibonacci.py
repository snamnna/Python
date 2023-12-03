def fib(n):
    """
    Calculate the Fibonacci's series value for integer n
    
    Parameters:
    - n: The number to use in the Fibonacci's series.
    
    Returns: The calculated value of the Fibonacci's series for n
    """
    # Jos annettu luku on pienempi kuin kaksi, annetaan vastaus automaattisesti olemaan 1
    if n < 2:
        return 1
    # Alustetaan kaksi muuttujaa kahdelle viimeksi käytetylle
    previous = previous_previous = 1
    
    # Lasketaan fibonacci annetuilla luvuilla
    # Jokaisella kierroksella tulee uusi fibonaccin luku result, joka on kahden edellisen luvun summa
    # Edellinen ja sitä edellinen luku päivitetään uusiin arvoihin
    for _ in range(n - 1):
        result = previous + previous_previous
        previous, previous_previous = result, previous
        
    # Palautetaan tämän kierroksen fibonacci
    return result