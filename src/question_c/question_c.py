#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna1, dna2):

    positions = {}

    dna1 = dna1.upper()
    dna2 = dna2.upper()

    count = 1

    for index in range(len(dna1)): 
        if dna1[index:index + len(dna2)] == dna2:
            positions[f'position{count}'] = index+1
            count += 1 

    return positions

