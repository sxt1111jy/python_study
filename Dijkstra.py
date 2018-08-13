import heapq
import sys

'''
迪杰斯特拉算法是由荷兰计算机科学家狄克斯特拉于1959 年提出的，因此又叫狄克斯特拉算法。
是从一个顶点到其余各顶点的最短路径算法，解决的是有向图中最短路径问题。迪杰斯特拉算法
主要特点是以起始点为中心向外层层扩展，直到扩展到终点为止。
'''
class Graph:
	def __init__(self):
		self.vertices = {}
		
	def add_vertex(self, name, edges):
		self.vertices[name] = edges
	
	def get_shortest_path(self, startpoint, endpoint):
		#distances使用字典的方式保存每一个顶点到startpoint点的距离
		distances = {}
		
		#从startpoint到某点的最优路径的前一个结点
		#eg:startpoint->B->D->E,则previous[E]=D,previous[D]=B,等等
		previous = {}
		
		#用来保存图中所有顶点的到startpoint点的距离的优先队列
		#这个距离不一定是最短距离
		nodes = []
		
		#Dikstra算法 数据初始化
		for vertex in self.vertices:
			if vertex == startpoint:
				#将startpoint点的距离初始化为0
				distances[vertex] = 0
				heapq.heappush(nodes, [0, vertex])
			elif vertex in self.vertices[startpoint]:
				#把与startpoint点相连的结点距离startpoint点的距离初始化为对应的弧长/路权
				distances[vertex] = self.vertices[startpoint][vertex]
				heapq.heappush(nodes, [self.vertices[startpoint][vertex], vertex])
				previous[vertex] = startpoint
			else:
				#把与startpoint点不直接连接的结点距离startpoint的距离初始化为sys.maxsize
				distances[vertex] = sys.maxsize
				heapq.heappush(nodes, [sys.maxsize, vertex])
				previous[vertex] = None
		
		while nodes:
			#取出队列中最小距离的结点
			smallest = heapq.heappop(nodes)[1]
			if smallest == endpoint:
				shortest_path = []
				lenPath = distances[smallest]
				temp = smallest
				while temp != startpoint:
					shortest_path.append(temp)
					temp = previous[temp]
				#将startpoint点也加入到shortest_path中
				shortest_path.append(temp)
			if distances[smallest] == sys.maxsize:
				#所有点不可达
				break
			#遍历与smallest相连的结点，更新其与结点的距离、前继节点
			for neighbor in self.vertices[smallest]:
				dis = distances[smallest] + self.vertices[smallest][neighbor]
				if dis < distances[neighbor]:
					distances[neighbor] = dis
					#更新与smallest相连的结点的前继节点
					previous[neighbor] = smallest
					for node in nodes:
						if node[1] == neighbor:
							#更新与smallest相连的结点到startpoint的距离
							node[0] = dis
							break
					heapq.heapify(nodes)
		return shortest_path, lenPath
if __name__ == '__main__':
	g = Graph()
	g.add_vertex('a', {'b':6, 'd':2, 'f':5})
	g.add_vertex('b', {'a':6, 'c':4, 'd':5})
	g.add_vertex('c', {'b':4, 'e':4, 'h':6})
	g.add_vertex('d', {'a':2, 'b':5, 'e':6, 'f':4})
	g.add_vertex('e', {'d':6, 'c':4, 'g':5, 'h':4})
	g.add_vertex('f', {'a':5, 'd':4, 'g':9})
	g.add_vertex('g', {'f':9, 'e':5, 'h':5})
	g.add_vertex('h', {'c':6, 'e':4, 'g':5})
	start = 'a'
	end = 'e'
	shortestPath, len = g.get_shortest_path(start, end)
	print('{}->{}的最短路径是：{}，最短路径为：{}'.format(start, end, shortestPath, len))
