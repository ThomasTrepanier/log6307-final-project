import ray
import time

max_concurrent_downloads = 2

ray.init(num_cpus=4, resources={'Network': max_concurrent_downloads})

@ray.remote(resources={'Network': 1})
def download_content(url):
    # Download the file.
    time.sleep(1)
    return 'result from ' + url

@ray.remote
def process_result(result):
    # Process the result.
    time.sleep(1)
    return 'processed ' + result

urls = ['url1', 'url2', 'url3', 'url4']

result_ids = [download_content.remote(url) for url in urls]

processed_ids = [process_result.remote(result_id) for result_id in result_ids]

# Wait until the tasks have finished and retrieve the results.
processed_results = ray.get(processed_ids)
