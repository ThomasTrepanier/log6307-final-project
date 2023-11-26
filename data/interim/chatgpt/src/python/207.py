import matplotlib.pyplot as plt

def calculate_probability(rank1, rank2):
    diff = abs(rank1 - rank2)
    y = (0.5 / 15) * diff + 0.5
    if rank1 < rank2:
        return y, 1 - y
    else:
        return 1 - y, y

def lptr(rank1, rank2):
    diff = abs(rank1 - rank2)
    y = (0.5 / 15) * diff + 0.5
    if rank1 < rank2:
        return y, 1 - y
    else:
        return 1 - y, y

# Input rankings
rankings = list(range(1, 17))

# Calculate probabilities using the two algorithms
algorithm1_probs = [calculate_probability(rank1, rank2)[0] for rank1 in rankings for rank2 in rankings]
algorithm2_probs = [lptr(rank1, rank2)[0] for rank1 in rankings for rank2 in rankings]

# Plotting the probabilities
plt.plot(rankings, algorithm1_probs, label='Algorithm 1')
plt.plot(rankings, algorithm2_probs, label='Algorithm 2')
plt.xlabel('Ranking')
plt.ylabel('Probability')
plt.title('Probabilities of Winning by Ranking')
plt.legend()
plt.show()
