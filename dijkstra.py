import heapq

def base_dijikstra(graph, start, error=0):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight + error  # error here, error = 0 => correct dijikstra
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

def wrong_dijkstra_empty(graph, start):
    # Returns an empty dictionary assuming no nodes are present.
    return {}

def wrong_dijkstra_single(graph, start):
    # Incorrectly assigns an infinite distance to a single node graph.
    return {start: float('infinity')}
