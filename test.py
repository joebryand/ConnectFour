import pandas as pd


lijstje = []

depth_0 =  [[(1, 3),  (4, 6),  (6, 4), (1, 9)], 
            [(1, 9),  (1, 9),  (1, 9), (1, 9)], 
            [(0, 10), (0, 10), (2, 8), (0, 10)], 
            [(6, 3),  (2, 8),  (9, 1), (0, 10)]]

depth_1 =  [[(2, 8), (2, 8), (7, 3),  (1, 9)], 
            [(2, 8), (2, 8), (5, 4),  (0, 10)], 
            [(1, 9), (1, 8), (6, 3),  (0, 10)], 
            [(7, 3), (8, 2), (10, 0), (5, 4)]]

depth_2 =  [[(2, 6), (6, 4), (7, 3), (0, 7)], 
            [(4, 6), (0, 9), (7, 3), (0, 10)], 
            [(1, 9), (2, 8), (8, 2), (1, 9)], 
            [(3, 6), (6, 3), (8, 2), (3, 7)]]

depth_3 =  [[(3, 7), (3, 7),  (5, 4),  (1, 9)], 
            [(3, 7), (3, 7),  (5, 5),  (1, 9)], 
            [(2, 8), (3, 6),  (5, 4),  (0, 9)], 
            [(9, 1), (10, 0), (10, 0), (2, 7)]]

depth_4 =  [[(2, 4),  (9, 1),  (10, 0), (5, 5)], 
            [(0, 10), (4, 6),  (2, 5),  (1, 9)], 
            [(1, 9),  (2, 7),  (6, 4),  (2, 8)], 
            [(4, 3),  (10, 0), (9, 1),  (4, 6)]]

depth_5 =  [[(6, 3),  (7, 2),  (7, 3), (5, 5)], 
            [(6, 3),  (7, 2),  (7, 1), (6, 4)], 
            [(1, 8),  (4, 3),  (4, 5), (1, 9)], 
            [(10, 0), (10, 0), (9, 1), (1, 4)]]

algorithms = ["possible_connect_fours", "connected_pieces", "random", "combination"]

for i,depth in enumerate([depth_0,depth_1,depth_2,depth_3,depth_4,depth_5]):
    for red_player, row in enumerate(depth):
        for yellow_player, outcome in enumerate(row):
            lijstje.append([i,algorithms[yellow_player],algorithms[red_player],outcome[1],outcome[0],10-outcome[1]-outcome[0]])


for row in lijstje:
    print(row)
df = pd.DataFrame(lijstje,index= list(range(len(lijstje))),columns= ["Depth","Yellow_algorithm","Red_algorithm","Win_yellow","Win_red","Draw"])


