import requests
import threading
import math
import multiprocessing
import random
import uuid


TARGET_URL = "http://localhost:3000"

#Retrieve file content
def retrieve_file_content(file_path):
    data = None
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def find_existing_routes(routes):
    available_routes = ""
    for route in routes:
        print("processing...")
        res = requests.get(f"{TARGET_URL}/{route}") #Send request
        if res.status_code != 404: #Verify if status is not 404 which corresponds to not found 
            random_value = random.randint(0, 1000)
            available_routes = available_routes + route+"\n" #Append availables routes
            path = requests.get(f"{TARGET_URL}/{route}/{random_value}")
            if path.status_code != 404:
                available_routes = available_routes + f"{route}/:id \n"
            for r in routes:
                query = requests.get(f"{TARGET_URL}/{route}?{r}={random_value}")
                if query.status_code != 404:
                    available_routes = available_routes + f"{route}?{r}=? \n"

    filename = str(uuid.uuid4())+".txt"
    with open(f"routes_availables/{filename}", "w") as available :
        available.write(available_routes)


if __name__ == "__main__":
    random_routes = retrieve_file_content("dir_list.txt").split("\n") #get the word list file content
    threads = [] # initiate a list of thread
    workers_count = multiprocessing.cpu_count() # count cpu

    length = len(random_routes)
    quota = math.floor(length / workers_count) #number of routes to treat for each thread
    index_from = 0

    for i in range(0, workers_count):
        batch = random_routes[index_from:index_from+quota] #slice random_routes
        thread = threading.Thread(target=find_existing_routes, args=(batch, )) #create a thread
        index_from = index_from+quota
        threads.append(thread) #store each thread into the list

    #Execute each thread
    for thr in threads:
        thr.start()