import os
import collections
searchResult = collections.namedtuple("SearchResult","file,line,text")

def main():
    print_header()
    folder = get_folder_from_user()

    if not folder: 
        print("Sorry we can't search that location.")
        return 

    text= get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return
        
    print("Searching {} for {}.".format(folder,text))
    match_count =0
    for match in search_folders(folder,text):
        match_count +=1
        print ('--------- Match ------------')
        print ('File: {}'.format(match.file))
        print ('Line: {}'.format(match.line))
        print ('Match: {}'.format(match.text.rstrip()))        
    print ('Match Count: {:,}'.format(match_count))

def print_header():
    print("---------------------------------")
    print("            File Searcher")
    print("---------------------------------")
    print()

def get_folder_from_user():
    folder=input("What folder do you want to search? ")
    folder = folder.strip()
    
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)

def get_search_text_from_user():
    text =input("What are you searching for [single phrases only]?" )
    return text.lower()

def search_folders(folder,text):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder,item)
        #print ("Searching file {}".format(full_item))

        if os.path.isdir(full_item):
            yield from search_folders(full_item,text)          
        else:      
            yield from search_file(full_item,text)           
  
def search_file(filename,search_text):
    matches =[]
    try:
        with open(filename,'r',encoding='utf-8') as fin:
            line_num=0
            for line in fin:
                line_num+=1
                if line.lower().find(search_text)>=0:           
                    #print ("{} - {}".format(filename,line_num))         
                    yield searchResult(file=filename, line=line_num,text = line)
                    
    except UnicodeDecodeError:
        pass
                
if __name__ == "__main__": 
    main()