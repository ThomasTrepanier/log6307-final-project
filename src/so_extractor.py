import datetime
import re
from stackapi import StackAPI
from dotenv import load_dotenv
import json 
from html import unescape
import os

from model import string_in_english

class StackOverflowExtractor:
    def __init__(self, raw_dir, interim_dir):
        load_dotenv(dotenv_path='../environment/.env')
        self.key = os.getenv('KEY')
        self.api = StackAPI('stackoverflow', key=self.key)
        self.api.page_size = 100

        self.raw_dir = raw_dir
        self.interim_dir = interim_dir
        self.code_pattern = re.compile(r'<pre><code>(.*?)</code></pre>', re.DOTALL)


    def fetch_search(self, type, start_page, max_page, number_of_answers, has_accepted_answer, nb_of_views):
        url = 'search/advanced'

        self.api.max_pages = max_page
        from_date = int(datetime.datetime(2018, 11, 23).timestamp())
        to_date = int(datetime.datetime(2023, 10, 31).timestamp())
        order = "desc"
        sort = "activity"
        accepted = has_accepted_answer
        answers = number_of_answers
        tagged = [f"{type}"]
        views = nb_of_views

        result = self.api.fetch(url, page=start_page, fromdate=from_date, todate=to_date, order=order, sort=sort, accepted=accepted, answers=answers, tagged=tagged, views=views, site='stackoverflow')
        with open(f"{self.raw_dir}/so_search_{type}.json", "w") as f:
            json.dump(result, f)


    def fetch_answers(self, start_page, max_page, question_ids, type):
        self.api.max_pages = max_page
        sort = "activity"
        order = "desc"

        if not os.path.exists(f"{self.raw_dir}/answers"):
            os.mkdir(f"{self.raw_dir}/answers")

        for i, sub_set in enumerate(question_ids):
            ids = ";".join(sub_set)
            url = 'questions/{ids}/answers'
            result = self.api.fetch(url, page=start_page, ids=ids, sort=sort, order=order, site='stackoverflow', filter='withbody')

            with open(f"{self.raw_dir}/answers/{type}_{i}.json", "w") as f:
                json.dump(result, f)

    def extract_question_ids(self, type):
        with open(f"{self.raw_dir}/so_search_{type}.json", "r") as f:
            data = json.load(f)
        question_ids = []
        i = 0
        while i < len(data['items']):
            sub_set = []
            for j in range(100):
                sub_set.append(str(data['items'][i]['question_id']))
                i += 1
                if i == len(data['items']):
                    break
            question_ids.append(sub_set)

        return question_ids
       
    def extract_code_from_answers(self, path, file_index, type):
        with open(path, "r") as f:
            data = json.load(f)
        code_snippets = []

        for i in range(len(data['items'])):
            code_snippets.append(self.__extract_code_from_body(data['items'][i]['body']))
        
        if not os.path.exists(f"{self.interim_dir}/snippets"):
            os.mkdir(f"{self.interim_dir}/snippets")
            
        with open(f"{self.interim_dir}/snippets/{type}_{file_index}.json", "w") as f:
            json.dump(code_snippets, f)
    
    def __extract_code_from_body(self, body):
        # Find all matches in the body
        matches = self.code_pattern.findall(body)
        matches = [unescape(match) for match in matches]
        matches = [match for match in matches if string_in_english(match)]
        # Return the list of code snippets
        return matches