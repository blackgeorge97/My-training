NODE_NUMBER = 40
with open('p107_network.txt', 'r') as f:
    contents = f.read()
lines = contents.split('\n')
network_data = [line.split(',') for line in lines] 
total_weight = 0
new_weight = 0
for i in range(0, 40):
    for j in range(i,40):
        if network_data[i][j] != '-':
            total_weight += int(network_data[i][j])
visited_nodes = [0]
while len(visited_nodes) < NODE_NUMBER:
    min = 1000000
    for node in visited_nodes:
        for candidate_node in range(0, 40):
            if network_data[node][candidate_node] != '-':
                if candidate_node not in visited_nodes and int(network_data[node][candidate_node]) < min:
                    min = int(network_data[node][candidate_node])
                    last_visited_node = candidate_node
    new_weight += min
    visited_nodes.append(last_visited_node)
saving = total_weight - new_weight
print(total_weight, new_weight, saving)
