# from Graph import Vertex, Edge, Graph

def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
    """
    Calculate the shortest past (in distance value) between given vertices
    
    Parameters:
    - source_vertex: The source vertex
    - destination_vertex: The destination vertex
    - graph: The graph in question
    
    Returns: a tuple containing the minimum distance between vertices and a list of
             vertices that form the minimum path from one vertex to the other.
    """
    # Haetaan kaikki vertices
    unvisited_vertices = graph.get_vertices()
    
    # Luodaan sanakirjataulu löydetyistä lyhimmistä etäisyyksistä ja poluista
    shortest_path_table = {vertex: {'shortest': float('inf'), 'previous': None} for vertex in unvisited_vertices}
    
    # Alustetaan lähtösolmun polkuetäisyys 0
    shortest_path_table[source_vertex]['shortest'] = 0
    
    # Käydään läpi niin kauan kun on unvisited vertices eli solmuja
    while unvisited_vertices:
        # Haetaan solmu, jolla on tähän asti lyhin polkuetäisyys
        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_path_table[vertex]['shortest'])
        # Haetaan sen solmun etäisyys
        distance_from_source = shortest_path_table[current_vertex]['shortest']
        
        # Käydään läpi sen vierekkäiset solmut, jotka ovat vielä tutkimattomia
        unvisited_adjacent_vertices = (v for v in graph.get_adjacent_vertices(current_vertex) if v in unvisited_vertices)
        
        for adjacent_vertex in unvisited_adjacent_vertices:
            # Haetaan kaari solmujen välillä
            edge = graph.get_edge(current_vertex, adjacent_vertex)
            # Lasketaan etäisyys vierekkäiseen solmuun nykyisen solmun kautta etäisyys nykyisestä solmusta + etäisyys näiden kahden solmun välillä, eli kaaren arvo
            tentative_distance = distance_from_source + edge.value()
            
            # Jos etäisyys on lyhyempi kun jo laskettu, päivitetään taulukko
            if tentative_distance < shortest_path_table[adjacent_vertex]['shortest']:
                shortest_path_table[adjacent_vertex]['shortest'] = tentative_distance
                shortest_path_table[adjacent_vertex]['previous'] = current_vertex
        
        # Poistetaan nykyinen solmu käymättömien listalta, sillä siellä on käyty
        unvisited_vertices.remove(current_vertex)
    
    # Tarkistetaan polku käänteisessä järjestyksessä
    path = []
    current = destination_vertex
    while current:
        path.append(current)
        current = shortest_path_table[current]['previous']
    
     # Palautetaan lyhin etäisyys ja lyhin polku lähtösolmusta kohdesolmuun
    return (shortest_path_table[destination_vertex]['shortest'], path[::-1])