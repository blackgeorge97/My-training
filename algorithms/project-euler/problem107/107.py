NETWORK_FILE = open('p107_network.txt', 'r')
NETWORK_STRING = NETWORK_FILE.read()
NODE_NUMBER = 40
network_data = []
line = []
total_weight = 0
new_weight = 0
counter = 0
while counter < len(NETWORK_STRING):
    if NETWORK_STRING[counter] == ',':
        counter += 1
    elif NETWORK_STRING[counter] == '-':
        line.append('-')
        counter += 1
    elif NETWORK_STRING[counter] == '\n':
        network_data.append(line)
        line = []
        counter += 1
    else:
        start = counter
        while NETWORK_STRING[counter] != ',' and NETWORK_STRING[counter] != '\n':
            counter += 1
        line.append(int(NETWORK_STRING[start:counter]))
for i in range(0, 40):
    for j in range(i,40):
        if network_data[i][j] != '-':
            total_weight += network_data[i][j]
visited_nodes = [0]
while len(visited_nodes) < NODE_NUMBER:
    min = 1000000
    for node in visited_nodes:
        for witness in range(0, 40):
            if network_data[node][witness] != '-':
                if witness not in visited_nodes and network_data[node][witness] < min:
                    min = network_data[node][witness]
                    last_visited_node = witness
    new_weight += min
    visited_nodes.append(last_visited_node)
saving = total_weight - new_weight
print(total_weight, new_weight, saving)
