# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
#        print(successorGameState, "11111111")
#        print(newPos,'2222222')
#        print(newFood.asList(), '33333333')
#        print(newGhostStates, '44444444444')
#        print(newScaredTimes.asList(), '55555555555')
#        return successorGameState.getScore()
        if currentGameState.isWin():
        	return float("inf")
        walls =  currentGameState.getWalls()
        if walls[newPos[0]][newPos[1]] == True:
        	return float("-inf")
        for newGhostPost in newGhostStates:
        	if util.manhattanDistance(newPos, newGhostPost.getPosition()) <= 1 and newGhostPost.scaredTimer == 0:
        		return float("-inf")
        distPosFood=[]
        for foodPos in newFood.asList():
        	distPosFood.append(util.manhattanDistance(newPos, foodPos))
        	
        distGhostFood = []
        for foodPos in newFood.asList():
        	tempDist = []
        	for newGhostPost in newGhostStates:
        		tempDist.append(util.manhattanDistance(foodPos, newGhostPost.getPosition()))
        	distGhostFood.append(min(tempDist))
        if len(distPosFood) >= 1:
        	mx = max(distPosFood) + 103
        else:
        	mx = 103
        
        for i in range(0 , min(len(distPosFood), len(distGhostFood))):
        	if distGhostFood[i] <= 1:
        		distPosFood[i] += float("inf")
        	elif distGhostFood[i] <= distPosFood[i]:
        		distPosFood[i] += mx
        if len(distPosFood) >= 1:
       		return successorGameState.getScore() - min(distPosFood) + (currentGameState.getNumFood() -successorGameState.getNumFood())*103 + (successorGameState.getNumFood() >= 1)*103
       	else:
       		return successorGameState.getScore() + (currentGameState.getNumFood() - successorGameState.getNumFood())*103 + (successorGameState.getNumFood() >= 1)*103
        	
        

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        maxValue, Action = self.getNextAction(gameState, 0, 0)
        return Action
        util.raiseNotDefined()
    def getMiniMax(self, gameState, currentLevel, agentIndex):
     	if currentLevel == self.depth:
     		return self.evaluationFunction(gameState)
     	elif gameState.isWin() or gameState.isLose():
     		return self.evaluationFunction(gameState)
     	else:
     		value, action = self.getNextAction(gameState, currentLevel, agentIndex)
     		return value
     	return
     	
    def getNextAction(self, gameState, currentLevel, agentIndex):
     	currentMax = float("-inf")
     	nextAction = None
     	currentMin = float("inf")
     	totalAgents = gameState.getNumAgents()
     	if agentIndex == 0:
     		 for action in gameState.getLegalActions(agentIndex):
     		 	currentValue = self.getMiniMax(gameState.generateSuccessor(agentIndex, action), currentLevel, (agentIndex+1)%totalAgents);
     		 	if currentValue > currentMax:
     		 		currentMax = currentValue;
     		 		nextAction = action
     		 return currentMax, nextAction
     	else:
     		if agentIndex == totalAgents - 1:
     			currentLevel +=1;
     		for action in gameState.getLegalActions(agentIndex):
     		 	currentValue = self.getMiniMax(gameState.generateSuccessor(agentIndex, action), currentLevel, (agentIndex+1)%totalAgents);
     		 	if currentValue < currentMin:
     		 		currentMin = currentValue;
     		 		nextAction = action
     		return currentMin, nextAction
     	return None
     

class AlphaBetaAgent(MultiAgentSearchAgent):
	alpha = float("-inf")
	beta = float("inf")
	
	def getAction(self, gameState):
		self.alpha = float("-inf")
		self.beta = float("inf")
		maxValue, Action = self.getNextAction(gameState, 0, 0, self.alpha, self.beta)
		self.alpha = max( self.alpha, maxValue)
		return Action
		util.raiseNotDefined()
		
	def getMiniMax(self, gameState, currentLevel, agentIndex, alpha, beta):
		if currentLevel == self.depth:
			return self.evaluationFunction(gameState)
		elif gameState.isWin() or gameState.isLose():
			return self.evaluationFunction(gameState)
		else:
			value, action = self.getNextAction(gameState, currentLevel, agentIndex, alpha, beta)
			return value
		return
	
	def getNextAction(self, gameState, currentLevel, agentIndex, alpha, beta):
		currentMax = float("-inf")
		nextAction = None
		currentMin = float("inf")
		totalAgents = gameState.getNumAgents()
		if agentIndex == 0:
			for action in gameState.getLegalActions(agentIndex):
				currentValue = self.getMiniMax(gameState.generateSuccessor(agentIndex, action), currentLevel, (agentIndex+1)%totalAgents, alpha, beta);
				if currentValue > currentMax:
					currentMax = currentValue;
					nextAction = action
				if currentMax > beta:
					return currentMax, nextAction
				alpha = max(alpha, currentMax)
			return currentMax, nextAction
		else:
			if agentIndex == totalAgents - 1:
				currentLevel +=1;
			for action in gameState.getLegalActions(agentIndex):
				currentValue = self.getMiniMax(gameState.generateSuccessor(agentIndex, action), currentLevel, (agentIndex+1)%totalAgents, alpha, beta);
				if currentValue < currentMin:
					currentMin = currentValue;
					nextAction = action
				if currentMin < alpha:
					return currentMin, nextAction
				beta = min(beta, currentMin)
			return currentMin, nextAction
		return None

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

