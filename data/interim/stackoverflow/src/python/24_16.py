def diff_matrix(L, V, mfccs):
    plt.figure()
    plt.semilogy(V, '.')
    for i in range(len(V)):
        plt.text(i, V[i], mfccs[L[i]].name.split('.')[0], fontsize = 8)
    plt.xticks([])
    plt.ylim([0.001, 1])
    plt.ylabel('Value')
