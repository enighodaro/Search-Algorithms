#!/usr/bin/python3

# Simple Vertex class
class Vertex:
  """ Lightweight vertex structure for a graph.
      Vertices can have the following labels:
        UNEXPLORED
        VISITED

      Note that in our simple implementation, the elements are always
      integers in the range [0 .. MatrixSize - 1], so we can use them directly
      as indices into the AM.
  """
  __slots__ = '_element', '_label'

  def __init__(self, element, label="UNEXPLORED"):
    """ Constructor. """
    self._element = int(element)
    self._label = label

  def element(self):
    """ Return element associated with this vertex. """
    return int(self._element)

  def getLabel(self):
    """ Get label assigned to this vertex. """
    return self._label

  def setLabel(self, label):
    """ Set label after the vertex has been created. """
    self._label = label

  def __str__(self):
    """ Used when printing this object. """
    return "(%2d, %s)" % (self._element,self._label)

#-------------------------------------------------------------------------------

# Simple Edge class
class Edge:
  """ Lightweight edge structure for a graph.
      Edges can have the following labels:
        UNEXPLORED
        DISCOVERY
        BACK
  """
  __slots__ = '_origin', '_destination', '_label'

  def __init__(self, u, v, label="UNEXPLORED"):
    """ Constructor.  Note that u and v are Vertex objects. """
    self._origin = u
    self._destination = v
    self._label = label

  def getLabel(self):
    """ Get label assigned to this edge. """
    return self._label

  def setLabel(self, label):
    """ Set label after the edge has been created. """
    self._label = label

  def endpoints(self):
    """ Return (u,v) tuple for source and destination vertices. """
    # ... Implement this
    return (self._origin.element(), self._destination.element())

  def isIncident(self, v):
    """ Return True if vertex v is incident upon this edge, else False. """
    # ... Implement this
    if v is self._origin or v is self._destination:
      return True
    else: 
      return False

  def opposite(self, v):
    """ Return the vertex that is opposite v on this edge. """
    if not isinstance(v, Vertex):
      raise TypeError('v must be a Vertex')
    if v not in [self._destination, self._origin]:
      raise ValueError('v not incident to edge')
    return self._destination if v is self._origin else self._origin

  def __str__(self):
    """ Used when printing this object. """
    return "(%2d, %2d, %s)" % (self._origin._element,self._destination._element,self._label)


#-------------------------------------------------------------------------------------------

class AMGraph:
  """ Partial Graph ADT represented by an adjacency matrix.
      From this point on, the term 'adjacency matrix' is denoted 'AM'.

      The AM will store 'Edge' objects at each position containing an edge,
      otherwise a 'None' will be stored in that position. """

  #------------------------- Graph implementation -------------------------
  # '_matrix' is a 2D array representing the AM
  __slots__ = '_matrix', '_edges', '_vertices'

  #-- c'tor
  def __init__(self, edgeCollection, vertexCollection):
    # We keep a collection of edges and vertices *only* for use with the
    # accessor methods for those objects; all other methods MUST use the AM directly
    self._edges    = edgeCollection
    self._vertices = vertexCollection

    # Parse the edge collection, and insert the edges into the
    # appropriate place in the AM (remember to insert 'None' at the appropriate
    # locations too, and to take 'mirroring' into account)

    # ... Implement this: Create AM, and fill it as required
    n = len(self._vertices)
    self._matrix = [[0]*n for i in range(n)]

    for u in range(n):
      for v in range(n):
        found = False
        for e in self._edges:
          pts=e.endpoints()
          
          if pts[0]==u and pts[1]==v or pts[0]==v and pts[1]==u :
            self._matrix[u][v]=pts
            found = True
            break
        
        if found == False:
          self._matrix[u][v] = None
            

  #-- Public methods
  def edges(self):
    """ Return a set of all edges of the graph. """
    # ... Implement this
    return self._edges

  def edgeCount(self):
    """ Return the number of edges in the graph. """
    # ... Implement this
    return len(self._edges)

  def vertices(self):
    """ Return a set of all vertices of the graph. """
    # ... Implement this
    return self._vertices

  def vertexCount(self):
    """ Return the number of vertices in the graph. """
    # ... Implement this
    return len(self._vertices)

  def getEdge(self, v1, v2):
    """ Return the edge from v1 to v2, or None if not adjacent. """
    # ... Implement this
    for e in self._edges:
      if e.isIncident(v1) and e.isIncident(v2):
        return e
    
    return None

  def incidentEdges(self, v):
    """ Return a collection of all edges incident to vertex v in the graph. """
    # ... Implement this
    arr = []
    for e in self._edges:
      if e.isIncident(v):
        arr.append(e)
    
    return arr 

  def print(self):
    """ Print the square matrix for this graph.
        Make sure to properly show the rows and columns,
        as well as labelling.
        The output should be neatly aligned in columns.
        If an AM entry contains an edge, output in the format (u,v).
        Otherwise, output a string such as '[NONE]'
        See the assignment for a sample of the required output.
    """
    # ... Implement this
    
    n = len(self._vertices)
    for u in range(n):
      for v in range(n):
        if self._matrix[u][v] == None:
          print('[None]', end = "  ")
        else: 
          print(f'{str(self._matrix[u][v]):8}', end = "")

      print()

  
#-------------------------------------------------------------------------------

def DFS(g):
  # Implement the depth-first search algorithm from the class notes.
  # Collect the edges that form the DFS tree of 'g' and return the collection.
  # ... Implement this
  arr = []
  
  def DFS(g,v):
    v.setLabel("VISITED")
    for e in g.incidentEdges(v):
      if e.getLabel()=="UNEXPLORED": 
        w=e.opposite(v)
        if w.getLabel()=="UNEXPLORED":
          e.setLabel("DISCOVERY")
          arr.append(e)
          DFS(g,w)
        else:
          e.setLabel("BACK")
          
      
  for ver in g.vertices():
    if ver.getLabel()=="UNEXPLORED":
      DFS(g,ver)
      
  return arr

#-------------------------------------------------------------------------------

#-- Main method

vertices = []
for i in range(13):
  vertices.append(Vertex(i))

print("This program implements a graph corresponding to the picture given \n" +
      "in file and runs the implemented the depth-first search (DFS) algorithm \n" +
      "on the graph, printing out the resulting tree, i.e Discovery edges \n" +
      "Also prints whether the graph is connected based on DFS traversal. \n")

# Create edge objects corresponding to the graph given in the question,
# and add them to the collection; note that an edge object is formed from
# two Vertex objects
# ... Implement this, using the vertices from the list above
edges = []
edges.append(Edge(vertices[0],vertices[1]))
edges.append(Edge(vertices[0],vertices[2]))
edges.append(Edge(vertices[0],vertices[5]))
edges.append(Edge(vertices[0],vertices[6]))
edges.append(Edge(vertices[3],vertices[4]))
edges.append(Edge(vertices[3],vertices[5]))
edges.append(Edge(vertices[4],vertices[5]))
edges.append(Edge(vertices[4],vertices[6]))
edges.append(Edge(vertices[4],vertices[11]))
edges.append(Edge(vertices[6],vertices[7]))
edges.append(Edge(vertices[7],vertices[8]))
edges.append(Edge(vertices[7],vertices[9]))
edges.append(Edge(vertices[9],vertices[10]))
edges.append(Edge(vertices[9],vertices[11]))
edges.append(Edge(vertices[9],vertices[12]))
edges.append(Edge(vertices[11],vertices[12]))

g = AMGraph(edges, vertices)

# Print all edges
print("Edges:", g.edgeCount())
for e in g.edges():
  print(e)
print()

# Print all vertices
print("Vertices:", g.vertexCount())
for v in g.vertices():
  print(v)
print()

# Print the actual graph (in matrix form)
print("Adjency matrix: 13x13")
g.print()
print()

# Call DFS on g, to get the discovery edges
discovery = DFS(g)
print("DFS edges:")
for e in discovery:
  print(e)
print()

# Determine whether the graph is connected
# ... Implement this, using the DFS traversal results
# if discovery is a spanning forest of the graph then the graph is connected
# that is all vertices are represented 
connect = False
for i in g.vertices():
  for e in discovery:
    if e.isIncident(i):
      connect = True
print("Graph is connected:", connect)
