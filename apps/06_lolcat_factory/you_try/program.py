import os
import cat_service
import subprocess
import platform

def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: {}'.format(folder))
    download_cats(folder)
    display_cats(folder)
    
def print_header():
    print("---------------------------------")
    print("            Cat Factory")
    print("---------------------------------")
    print()


def get_or_create_output_folder(): 
    base_folder = os.path.dirname(__file__)
    folder='cat_pictures'
    full_path = os.path.join(base_folder,folder)
    print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path



def download_cats(folder):
    print('Contacting server to download cats...')

    cat_count=3

    for i in range(1,cat_count+1):        
        name = 'lolcat_{}'.format(i)
        print('Downloading cat {}'.format(name)) 
        cat_service.get_cat(folder,name)

    print('Done\n')

def display_cats(folder):
    #open folder
    print('Displaying cats')
    if platform.system() == 'Windows':
        subprocess.call(['start',folder],shell=True)
    else:
        print ("I don't support your OS")

if __name__ == '__main__': 
    main()

