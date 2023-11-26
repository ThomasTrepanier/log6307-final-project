class nouns:

    def get_nouns(self, sentences):
        start = time.time()
        docs = nlp.pipe(sentences, n_threads=-1)
        result = [ ' '.join([token.text for token in doc if token.tag_ in ['NN', 'NNP', 'NNS', 'NNPS']]) for doc in docs]
        print('Time Elapsed {} ms'.format((time.time() - start) * 1000))
        print(result)


if __name__ == '__main__':
    sentences = ['we went to the school yesterday',
                 'The weather is really cold',
                 'Can we catch the dog?',
                 'How old are you John?',
                 'I like diving and swimming',
                 'Can the world become united?']
    obj = nouns()
    obj.get_nouns(sentences)
