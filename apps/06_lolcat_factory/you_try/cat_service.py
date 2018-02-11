import requests
import shutil
import os
import hashlib

def is_duplicate_file(folder_path, file_data):

    test_hash_checksum = hashlib.md5(file_data).hexdigest()

    for filename in os.listdir(folder_path):        
        if test_hash_checksum==hashlib.md5(open( os.path.join(folder_path, filename),"rb").read()).hexdigest():
            return True
            break

    return False

def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    url = 'http://thecatapi.com/api/images/get?format=src&type=gif'
    retry_count = 0
    max_retry_count = 10
    
    while retry_count<max_retry_count:
        cat_data = get_data_from_url(url)

        if is_duplicate_file(folder,cat_data):
            retry_count=retry_count+1            
            print ("Duplicate cat detected. Retrying (attempt {} of {})".format(retry_count,max_retry_count))            
            continue
        else:
            save_image(folder,name,cat_data)
            break

    if retry_count==max_retry_count:
        print ("Gave up after {} retries.".format(max_retry_count))

def get_data_from_url(url):
    response =requests.get(url,stream=True)
    return response.raw.read()


def save_image(folder,name,data):
   filename = os.path.join(folder, name + '.jpg')    

   with open(filename,"wb") as file_output:
        file_output.write(data)
       # shutil.copyfileobj(data,file_output)

