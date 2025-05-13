def PairedDeBruijnGraph(k, d, paired_reads):
    graph = {}

    for paired_read in paired_reads:
        prefix = (paired_read[0][:k-1], paired_read[1][:k-1])
        suffix = (paired_read[0][1:], paired_read[1][1:])

        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]

    return graph

def EulerianPath(graph):
    in_degrees = {}
    out_degrees = {}

    for node, neighbors in graph.items():
        out_degrees[node] = len(neighbors)
        if node not in in_degrees:
            in_degrees[node] = 0
        for neighbor in neighbors:
            if neighbor in in_degrees:
                in_degrees[neighbor] += 1
            else:
                in_degrees[neighbor] = 1

    start_node = None
    end_node = None
    for node in in_degrees:
        if node not in out_degrees or in_degrees[node] < out_degrees[node]:
            start_node = node
        elif in_degrees[node] > out_degrees[node]:
            end_node = node

    if end_node in graph:
        graph[end_node].append(start_node)
    else:
        graph[end_node] = [start_node]

    stack = [start_node]
    path = []

    while stack:
        current_node = stack[-1]
        if current_node in graph and graph[current_node]:
            next_node = graph[current_node].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())

    return path[::-1]

def PathToGenome(path, k, d):
    genome = path[0][0] + path[0][1][-1]

    for paired_read in path[1:]:
        genome += paired_read[0][-1]

    for paired_read in path:
        genome += paired_read[1][-1]

    return genome

def StringReconstructionFromReadPairs(k, d, paired_reads):
    graph = PairedDeBruijnGraph(k, d, paired_reads)
    path = EulerianPath(graph)
    text = PathToGenome(path, k, d)
    return text

# Given data
k = 3
d = 1
paired_reads = [
    ("ACC", "ATA"), ("ACT", "ATT"), ("ATA", "TGA"), ("ATT", "TGA"),
    ("CAC", "GAT"), ("CCG", "TAC"), ("CGA", "ACT"), ("CTG", "AGC"),
    ("CTG", "TTC"), ("GAA", "CTT"), ("GAT", "CTG"), ("GAT", "CTG"),
    ("TAC", "GAT"), ("TCT", "AAG"), ("TGA", "GCT"), ("TGA", "TCT"),
    ("TTC", "GAA")
]

result = StringReconstructionFromReadPairs(k, d, paired_reads)

# Output
print(result)
