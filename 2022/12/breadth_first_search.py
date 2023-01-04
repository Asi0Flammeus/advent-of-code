from collections import deque

def find_shortest_path(grid, start, end):
  # Create a queue to store the nodes that will be visited
  potential_nodes = []
  queue = deque([start])
  # Create a set to store the nodes that have already been visited
  visited = set(start)

  # While the queue is not empty
  while queue:
    potential_nodes.append(queue)
    # Dequeue the first node from the queue
    node = queue.popleft()
    potential_nodes.append(list(node))
    # Check if the node is the target point
    if node == end:
        potential_nodes = potential_nodes[1::2]
        return build_path(potential_nodes, grid)
    # Otherwise, consider the node's neighbors (i.e., the cells immediately above, below, left, and right of the node)
    for neighbor in get_neighbors(grid, node):
      if neighbor not in visited:  # If the neighbor has not been visited
        # Enqueue the neighbor and mark it as visited
        queue.append(neighbor)
        visited.add(neighbor)
  # If the target point is not reached, return "not found"
  return "not found"

def get_neighbors(grid, node):
  # Get the row and column indices of the node
  row, col = node
  # Consider the cells immediately above, below, left, and right of the node
  neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
  # Filter out any cells that are out of bounds or have a value greater than 1 higher than the current cell
  neighbors = [n for n in neighbors if is_valid(grid, n, node)]
  return neighbors

def is_valid(grid, node, prev_node):
  # Get the row and column indices of the node
  row, col = node
  prev_row, prev_col = prev_node
  # verify that the node is withing the grid boundaries
  if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
      # verify that the node is accesible (elavation only 1 above or equal or lower)
      if grid[row, col] <= grid[prev_row, prev_col] + 1:
          return True
  return False

def build_path(potential_nodes, grid):
    # start from the end to build back the path
    path = []
    path.append(potential_nodes.pop())
    for node in reversed(potential_nodes):
        prev_node = path[-1]
        if ((prev_node[0] - 1 == node[0] or prev_node[0] + 1 == node[0]) and prev_node[1] == node[1]) or ((prev_node[1] - 1 == node[1] or prev_node[1] + 1 == node[1]) and prev_node[0] == node[0]):
            if is_valid(grid,prev_node,node):
                path.append(node)
    return list(reversed(path))


