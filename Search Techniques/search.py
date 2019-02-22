# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()





def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


visited ={}
parent = {}
path = {}
walk = []

def getWalk(problem, currentState):
	start = problem.getStartState()
	if start == currentState:
		return
	walk.append(path[currentState])
	getWalk(problem, parent[currentState])
	return
	

DONE = False

def doDFS(problem, currentState):
	global DONE
#	print 'currrentState:', currentState
	goal = problem.isGoalState(currentState)
	if goal== True:
		getWalk(problem, currentState)
		DONE = True
#		print 'Walk:',walk
		return
	visited[currentState] = True
	successors = problem.getSuccessors(currentState)
	for succ in successors:
		nextState = succ[0]
		if DONE == False:
			if nextState not in visited or visited[nextState] is not True:
				path[nextState] = succ[1]
				parent[nextState] = currentState
				doDFS(problem, nextState)
	return
	



def depthFirstSearch(problem):
	
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    global path
    global parent
    global visited
    global DONE
    global walk
    walk = []
    DONE = False
    path = {}
    parent = {}
    visited = {}
#    print "Start:", problem.getStartState()
#    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    doDFS(problem, problem.getStartState())
#    print 'parents:', parent
#    print 'paths:', path
#    print 'visited:', visited
    # util.raiseNotDefined()
    walk.reverse()
    return walk
    
Q = []
def doBFS(problem):
	Q.append(problem.getStartState())
	visited[problem.getStartState()] = True
	for cs in Q:
		if problem.isGoalState(cs)== True:
			getWalk(problem, cs)
#			print 'Walk1: ', walk
			return
		successors = problem.getSuccessors(cs)
#		print 'Succs:',successors
		for tmpcs in successors:
#			print 'tmpcs[0]:', tmpcs[0]
			nextState = tmpcs[0]
			if nextState not in visited or visited[nextState] is not True:
				Q.append(nextState)
				parent[nextState] = cs
				path[nextState] = tmpcs[1]
				visited[nextState] = True
	return
	

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    global path
    global parent
    global visited
    global Q
    Q = []
    global walk
    walk = []
    path = {}
    parent = {}
    visited = {}
#    print "Start:", problem.getStartState()
#    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    doBFS(problem)
#    print 'parents:', parent
#    print 'paths:', path
#    print 'visited:', visited
    walk.reverse()
    return walk
#    util.raiseNotDefined()

pathCost = {}
def doUCS(problem):
	pq = util.PriorityQueue()
	pq.push(problem.getStartState(), 0)
	pathCost[problem.getStartState()] = 0
	'''u = pq.pop()
	print 'U:', u'''
	while pq.isEmpty() is not True:
		u = pq.pop()
#		print 'u: ', u
		if problem.isGoalState(u) is True:
			getWalk(problem, u)
#			print 'Walks: ', walk
#			print 'parent: ', parent
#			print 'paths: ',path
			return
			
		successors = problem.getSuccessors(u)
		for succ in successors:
			v = succ[0]
			d = succ[1]
			c = succ[2]
			tmpCost = pathCost[u] + c
			if v not in pathCost or tmpCost < pathCost[v]:
				pathCost[v] = tmpCost
				parent[v] = u
				path[v] = d
				pq.push(v, tmpCost)
	return


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    global path
    global parent
    global visited
    global pathCost
    global walk
    walk = []
    path = {}
    parent = {}
    visited = {}
    pathCost = {}
#    print "Start:", problem.getStartState()
#    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    doUCS(problem)
#    print 'parents:', parent
#    print 'paths:', path
#    print 'pathCost: ', pathCost
    walk.reverse()
    return walk
#    util.raiseNotDefined()


goalFound = False


def doIDS(problem , cs , mH):
	global goalFound
	global visited
	global pathCost
	global parent
	global path
	global walk
	global DONE
	# print 'cs: ', cs ,mH
	if problem.isGoalState(cs) == True:
		goalFound = True
		DONE = True
		getWalk(problem, cs)
		return
	if pathCost[cs] == mH:
		return
	visited[cs] = True
	successors = problem.getSuccessors(cs)
	for succ in successors:
		nextState = succ[0]
		if DONE == False:
			if nextState not in visited or visited[nextState] is not True:
				path[nextState] = succ[1]
				parent[nextState] = cs
				# print 'cs' , cs in pathCost , nextState
				pathCost[nextState] = pathCost[cs] + 1
				doIDS(problem, nextState , mH)
	return
	
	

def iterativeDeepeningSearch(problem):
	global goalFound
	global visited
	global pathCost
	global parent
	global path
	global walk
	global DONE
	goalFound = False
	mxHeight = 0
	while goalFound == False:
		visited = {}
		pathCost = {}
		parent = {}
		path = {}
		walk = []
		DONE = False
		pathCost[problem.getStartState()] = 0
		doIDS(problem, problem.getStartState(), mxHeight)
		mxHeight = mxHeight + 1
	# print 'parent: ', parent
	# print 'paths: ',path
	# print 'pathCost: ', pathCost
	# print 'visited: ', visited
	# print 'goalFound: ', goalFound
	# print 'DONE: ',DONE
	walk.reverse()
	# print 'WALK: ', walk
	return walk
	


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    
def doAStartSearch(problem, heuristic):
	global path
	global parent
	global visited
	global pathCost
	global walk

	pq = util.PriorityQueue()
	pq.push(problem.getStartState(), heuristic(problem.getStartState(), problem))
	pathCost[problem.getStartState()] = 0
	while pq.isEmpty() is not True:
		u = pq.pop()
#		print 'u: ', u
		if problem.isGoalState(u) is True:
			getWalk(problem, u)
#			print 'Walks: ', walk
#			print 'parent: ', parent
#			print 'paths: ',path
			return
			
		successors = problem.getSuccessors(u)
		for succ in successors:
			v = succ[0]
			d = succ[1]
			c = succ[2]
			tmpCost = pathCost[u] + c
			if v not in pathCost or tmpCost < pathCost[v]:
				pathCost[v] = tmpCost
				parent[v] = u
				path[v] = d
				pq.push(v, tmpCost+heuristic(v, problem))
	return


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    global path
    global parent
    global visited
    global pathCost
    global walk
    walk = []
    path = {}
    parent = {}
    visited = {}
    pathCost = {}
    doAStartSearch(problem , heuristic)
    walk.reverse()
    return walk
    util.raiseNotDefined()
    

def doGBFS(problem, heuristic):
	global path
	global parent
	global visited
	global pathCost
	global walk
	pq = util.PriorityQueue()
	pq.push(problem.getStartState(), heuristic(problem.getStartState(), problem))
	while pq.isEmpty() is not True:
		u = pq.pop()
#		print 'u: ', u
		if problem.isGoalState(u) is True:
			getWalk(problem, u)
#			print 'Walks: ', walk
#			print 'parent: ', parent
#			print 'paths: ',path
			return
			
		successors = problem.getSuccessors(u)
		for succ in successors:
			v = succ[0]
			d = succ[1]
			c = succ[2]
			if v not in visited :
				visited[v] = True
				parent[v] = u
				path[v] = d
				pq.push(v, heuristic(v, problem))
	return

    
def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    global path
    global parent
    global visited
    global pathCost
    global walk
    walk = []
    path = {}
    parent = {}
    visited = {}
    pathCost = {}
    doAStartSearch(problem , heuristic)
    walk.reverse()
    return walk
	
	


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
gbfs = greedyBestFirstSearch
