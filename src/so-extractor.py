import datetime

class StackOverflowExtractor:
    def __init__(self, data_dir):
        self.base_url = "https://api.stackexchange.com/2.3"

    def search(self, type, number_of_answers, has_accepted_answer, nb_of_views):
        # Check StackAPI
        advanced_search_url = self.base_url + "/search/advanced"
        page_size = 100
        from_date = datetime.datetime(2018, 11, 23).timestamp()
        to_date = datetime.datetime(2023, 10, 31).timestamp()
        order = "desc"
        sort = "activity"
        accepted = has_accepted_answer
        answers = number_of_answers
        tagged = [f"{type}"]
        views = nb_of_views
        site = "stackoverflow"

        # Call the API and get the results

        # Return the results


        # https://api.stackexchange.com/2.3/search/advanced?pagesize=100&fromdate=1542931200&todate=1700697600&order=desc&sort=activity&accepted=True&answers=3&tagged=python&views=100&site=stackoverflow
