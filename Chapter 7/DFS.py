def DFS(graph, u, visited=None):
    # Graph on verkko mitä tutkitaan
    # u on solmu josta lähdetään hakemaan
    # visited on dictionary jossa ylläpidetään tietoa siitä, onko solmussa käyty
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.
    """
    # Tarkistetaan onko visited dictionary jo alustettu, jos ei, se alustetaan ja
    # laitetaan aloitussolmuksi parametrina saatu u
    if visited is None:
        visited = {u : None} 
        
    # Käydään läpi kaikki u:n viereiset solmut
    for v in graph.get_adjacent_vertices(u):
        # Katsotaan onko tässä viereisessä solmussa käyty aiemmin
        if v not in visited:
            # Jos ei ole käyty, lisätään se dictionaryyn
            visited[v] = u
            # Kun saavutaan solmuun v, jatketaan siitä eteenpäin katsomista
            DFS(graph, v, visited)
        # Palautetaan lista
    return visited