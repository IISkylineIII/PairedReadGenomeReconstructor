# PairedReadGenomeReconstructor

Description

PairedReadGenomeReconstructor is a Python script that reconstructs a genome string from paired k-mer reads with a fixed distance d. The algorithm builds a Paired de Bruijn graph, finds an Eulerian path, and reconstructs the genome based on the path. This approach is commonly used in bioinformatics, particularly in genome assembly using paired-end reads.
Functionality
PairedDeBruijnGraph(k, d, paired_reads)

    Purpose: Builds a directed graph from paired k-mer reads with a specified gap d.

    Parameters:

        k (int): Length of each k-mer.

        d (int): Distance between the two k-mers in a pair.

        paired_reads (list): A list of tuples, each containing a pair of k-mers.

    Returns:

        graph (dict): A directed graph represented as an adjacency list, where nodes are pairs of prefix and suffix strings.

EulerianPath(graph)

    Purpose: Finds an Eulerian path in the graph.

    Parameters:

        graph (dict): A directed graph from the paired k-mers.

    Returns:

        path (list): A list of nodes representing the Eulerian path.

PathToGenome(path, k, d)

    Purpose: Reconstructs the genome string from the Eulerian path.

    Parameters:

        path (list): Eulerian path obtained from the graph.

        k (int): Length of each k-mer.

        d (int): Gap between paired k-mers.

    Returns:

        genome (str): Reconstructed genome string.

StringReconstructionFromReadPairs(k, d, paired_reads)

    Purpose: Full pipeline to reconstruct the genome string from paired reads.

    Parameters:

        k (int), d (int), paired_reads (list): As described above.

    Returns:

        text (str): Reconstructed genome string from paired reads.
    Returns:

        text (str): Reconstructed genome string from paired reads.
