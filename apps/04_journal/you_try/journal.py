import os
def get_full_pathname(name):
    return os.path.join('C:/Users/jfuex/Source/Repos/python-jumpstart-course-demos/apps/04_journal/journals', name + '.jrl')

def load(name):
    """
        This method creates and loads a journal
        :param name: name of the journal to load
    """

    filename = get_full_pathname(name)
    journal_data = list()

    print("Reading from {}".format(filename))
    with open(filename,"r") as file_input:
        for entry in file_input:
            add_entry(entry.rstrip(),journal_data)            

    return journal_data;

def save(name, journal_data):
    filename = get_full_pathname(name)
    print("Saving to {}".format(filename))
    
    with open(filename,'w') as file_output:    
        for entry in journal_data:
            file_output.write(entry + '\n')

def add_entry(text,data):
    data.append(text)
    