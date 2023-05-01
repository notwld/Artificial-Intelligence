from collections import deque
class myGraph:
    '''
    adj_list={'Ar':[('Ze',75),('Si',140),('Ti',118)],
                'Ze':[('Or',71),('Ar',75)],
                'Or':[('Ze',71),('Si',151)],
                'Si':[('Or',151),('Ar',140),('Fa',99),('Ri',80)],
                'Ri':[('Si',80),('Pi',97),('Cr',146)],
                'Cr':[('Ri',146),('Dr',120),('Pi',138)],
                'Pi':[('Ri',97),('Bu',101),('Cr',138)],
                'Fa':[('Si',99),('Bu',211)],
                'Ti':[('Ar',118),('Lu',111)],
                'Lu':[('Me',70),('Ti',111)],
                'Me':[('Dr',75),('Lu',70)],
                'Dr':[('Me',75),('Cr',120)],
                'Bu':[('Fa',211),('Pi',101)]
                }
                     
    hur_function={'Ar':266,
                'Ze':374,
                'Or':380,
                'Si':253,
                'Ri':193,
                'Cr':160,
                'Pi':100,
                'Fa':176,
                'Ti':329,
                'Lu':244,
                'Me':241,
                'Dr':242,
                'Bu':0
                }
           '''          
    
    def __init__(self, adjList,huFunc):
        self.adjList=adjList
        self.huFunc=huFunc
    def neighbors(self, node):
        return self.adjList[node]
    def a_star_search(self,startNode,destNode):
        
        open_nodes=set([startNode])
        closed_nodes=set([])
        g={}
        g[startNode]=0
        parents={}
        parents[startNode]=startNode
        
        while len(open_nodes)>0:
            tmp=None
            for v in open_nodes:
                if tmp==None or g[v]+huFunc[v]<g[tmp]+huFunc[tmp]:
                    tmp=v
            if tmp==None:
                prrint('Path doesn\'t exits')
                return None
            if tmp==destNode:
                path=[]
                
                while parents[tmp]!=tmp:
                    path.append(tmp)
                    tmp=parents[tmp]
                path.append(startNode)
                path.reverse()
                print('Path found: {}'.format(path))
                return path
            
            for (n,w) in self.neighbors(tmp):
                if n is not in open_nodes and n is not in closed_nodes:
                    open_nodes.add(n)
                    parents[n]=tmp
                    g[n]=g[tmp]+w
                    
                else:
                    
                
            
        
        
        
        
    