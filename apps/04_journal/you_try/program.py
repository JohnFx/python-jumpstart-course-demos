import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print("---------------------------------")
    print("            Journal App")
    print("---------------------------------")
    print()


def run_event_loop():
    
    cmd = None
    journal_name = "Default"
    journal_data = journal.load(journal_name)

    while cmd!='x': 
        print("\nWhat do you want to do with your journal? ")
        cmd = input("[R]eload, [S]ave, [L]ist entries, [A]dd an entry, E[x]it: ")            
        cmd = cmd.lower  ().strip()      

        if cmd =="r":
            journal_data = journal.load(journal_name)

        elif cmd =="l":
            list_entries(journal_data);

        elif cmd == "a":          
            add_entry(journal_data);

        elif cmd == "s":          
            journal.save(journal_name,journal_data)

        elif cmd =="x":
            print ("Goodbye")
            journal.save(journal_name,journal_data)
            break

        else:
            print ("I don't understand {}".format(cmd));

def list_entries(data):
    print();
    print("Your journal entries.")
    for idx,journal_entry in enumerate(data):
        print("{0}: {1}".format(idx+1,journal_entry))


def add_entry(data):
    text = input("Journal entry text: ")
    journal.add_entry(text,data)

if __name__ == '__main__':
    main()