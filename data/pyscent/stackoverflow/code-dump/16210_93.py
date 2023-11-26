def triplet(d3):

    if d3 in ("ATA","ATC", "ATT"):
        return "I"
    if d3 in ("CTA","CTC","CTG","CTT","TAA","TTG"):
        return "L"
    if d3 in ( "GTA","GTC","GTG","GTT"):
        return "V"
    if d3 in ("TTC","TTT"):
        return "F"
    if d3 == "ATG":
        return "M"

    return "X"

r=""
for i in range(0,len(dna),3):

    r+=triplet(dna[i:i+3])

print(r)  
