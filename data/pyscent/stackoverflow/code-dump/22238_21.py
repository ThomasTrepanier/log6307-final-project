import pymongo
import threading

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["thread1"]
com = db["threadcol"]
start_time = time.time()
logs=[]

number_of_json_objects=1417750
number_of_threads=50

session=requests.session()

def scrap_write_log(session,start,end):
    for n in range(start, end):
        response = session.get("https:/xx.xxx.xxx/{}.json".format(n))
        if response.status_code == 200:
            try:
                logs.append(str(n) + "\t" + str(com.insert_one(json.loads(response.text))) + "\n")
                print(str(n) + "\t" + str(inserted) + "\n")
            except:
                logs.append(str(n) + "\t" + "Failed to insert" + "\n")
                print(str(n) + "\t" + "Failed to insert" + "\n")

thread_ranges=[[x,x+number_of_json_objects//number_of_threads] for x in range(0,number_of_json_objects,number_of_json_objects//number_of_threads)]

threads=[threading.Thread(target=scrap_write_log, args=(session,start_and_end[0],start_and_end[1])) for start_and_end in thread_ranges]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

with open("logging.log", "a") as f:
    for line in logs:
        f.write(line)
