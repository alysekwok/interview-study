# There are a total of numCourses courses you have to take, labeled from 0 to 
# numCourses - 1. You are given an array prerequisites 
# where prerequisites[i] = [ai, bi] indicates that you must take course bi first 
# if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should 
# also have finished course 1. So it is impossible.

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # create graph
    graph = {}
    for prereq in prerequisites:
        if prereq[1] not in graph: 
            graph[prereq[1]] = [prereq[0]]
        else:
            graph[prereq[1]].append(prereq[0])
    # print(graph)

def checkCycle(graph, current, visited):
    pass
 
    # determine if graph is cyclic using bfs
    # visited = set()
    # for course in graph:
    #     visited.add(course)
    #     for neighbor in graph[course]:
    #         # print(neighbor)
    #         if neighbor in visited:
    #             return False
            
    # return True

# def dfs(course, visited, graph):
#     if course in visited:
#         return False
#     visited.add(course)
#     for neighbor in graph[course]:
#         print(neighbor)
#         dfs(neighbor, visited, graph)
#     return True

# numCourses = 2
# prerequisites = [[1,0], [0,1]]
# print(canFinish(numCourses, prerequisites))

# numCourses1 = 2
# prerequisites1 = [[1,0]]
# print(canFinish(numCourses1, prerequisites1))

# numCourses2 = 20
# prerequisites2 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
# print(canFinish(numCourses2, prerequisites2))

numCourses3 = 5
prerequisites3 = [[1,4],[2,4],[3,1],[3,2]]
print(canFinish(numCourses3, prerequisites3))