def summarize_array(array, summary_length):
    half_length = summary_length // 2
    if len(array) <= summary_length:
        return array
    else:
        first_half = array[:half_length]
        second_half = array[-half_length:]
        return np.concatenate([first_half, ['...'], second_half])

summary_length = 10
summarized_array = summarize_array(df.emb[0], summary_length)
print(summarized_array)
