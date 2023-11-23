def BFS(graph, start):
    # Graph on taas grafi jota käydään läpi
    # Start on se solmu josta aloitetaan
    """
    Perform Breadth-First Search of the graph starting from Vertex u.
    """
    # Alustetaan sanakirja, pidetään kirjaa siitä missä on käyty
    # Alussa ainoa käyty on se mistä aloitetaan
    visited = { start : None }
    
    # Tehdään lista, jossa on ne solmut, jotka ovat samalla tasolla aloitus solmun kanssa
    level = [start]
    
    # Niin kauan kun listassa on solmuja
    while level:
        # Tähän kerätään seuraavan tason solmut
        next_level = []
        # Iteroidaan level listan vertices (se missä aluksi on vain start)
        for vert in level:
            # Käydään läpi kaikki solmun vert naapurit 
            for neighbor in graph.get_adjacent_vertices(vert):
                if neighbor not in visited:
                    # Lisätään visited dictionaryyn ja merkitään mistä solmusta se on saavutettu
                    visited[neighbor] = vert
                    # Lisätään tämä naapuri seuraavan tason solmut listaan
                    next_level.append(neighbor)
        # Kun tämä taso on käyty läpi, level muuttujaan laitetaan seuraavan tason (next_level) solmut
        level = next_level
    return visited