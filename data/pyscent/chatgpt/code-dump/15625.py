def summarize_array(array, summary_length):
    half_length = summary_length // 2
    if len(array) <= summary_length:
        return array
    else:
        return np.concatenate((array[:half_length], array[-half_length:]))

summary_length = 10  # Change this to control the length of the summary
summarized_array = summarize_array(df.emb[0], summary_length)
print(summarized_array)
