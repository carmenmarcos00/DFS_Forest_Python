
#Author: Carmen Marcos Sánchez de la Blanca
#Date: May-2020
#Test: crea_bosque(dfs)


import networkx as nx

##Entry sample date
dfs = dict()
dfs = {
1:[18,19],
2:[17,20],
3:[3,8],
4:[4,5],
5:[2,9],
6:[6,7],
7:[10,15],
8:[11,14],
9:[12,13],
10:[1,16]
}
dfs2 = dict()
dfs2 = {
1:[3,10],
2:[2,11],
3:[1,12],
4:[4,7],
5:[5,6],
6:[8,9]
}



def crea_bosque(diccionario):
  #Inicialize pre y post
  pre= []
  post =[]

  #Crea 2 aux. dict 
  dic_pre= dict()
  dic_post=dict()

  # Split key and values into 2 lists
  key_list = list(diccionario.keys())
  val_list = list(diccionario.values())


  #Inicialize max
  max= 0


  #Give values to the differents structs of aux. data
  for i in range (len(key_list)):
    #Split val_list into pre and post
    #Append pre and post data
    pre.append(val_list[i][0])
    post.append(val_list[i][1])


    #The key in both cases is the same as the input argument
    #Values: pre--> dic_pre, post ---> dict_pro
    dic_pre[i+1]=pre[i]
    dic_post[i+1]=post[i]

    #Find max to know  the maximum time (always a post)
    valorpost = post[i]
    if(valorpost>max):
      max = valorpost


  #Create the graph and add nodes
  g = nx.Graph()
  g.add_nodes_from(key_list)


  #I--> times
  for i in range(max):
    i=i+1

    if i in dic_pre.values() and i+1 in dic_pre.values():

      v1 =list(dic_pre.keys())[list(dic_pre.values()).index(i)]
      v2 =list(dic_pre.keys())[list(dic_pre.values()).index(i+1)]

      g.add_edge(v1,v2)

    elif i in dic_post.values() and i+1 in dic_post.values():

      v1 =list(dic_post.keys())[list(dic_post.values()).index(i)]
      v2 =list(dic_post.keys())[list(dic_post.values()).index(i+1)]

      g.add_edge(v1,v2)

  print('nodos:')
  print(g.nodes)
  print('aristas:')
  print(g.edges())
  #if you want to draw the forest
  #nx.draw(g)
