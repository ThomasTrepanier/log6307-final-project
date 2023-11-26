string = str(f)
important_words = ['NAME', 'DATE OF BIRTH']
last_phrase = None
for phrase in important_words:
   phrase_start = string.index(phrase)
   phrase_end = phrase_start + len(phrase)
   if last_phrase is not None:
      get_data(string, last_phrase, phrase_start)
   last_phrase = phrase_end

def get_data(string, previous_end_index, current_start_index):
   usable_data = string[previous_end_index: current_start_index]
   return usable_data
