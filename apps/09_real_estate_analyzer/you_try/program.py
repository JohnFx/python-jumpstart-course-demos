from data_types import Purchase
from statistics import mean
from os import path
import csv

try:
    import statistics
except:
    #error code instead
    import statistics_standin_for_py2 as statistics

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)
    pass


def print_header():
    print('-------------------------------------')
    print('    Real Estate Data Mining App')
    print('-------------------------------------')


def get_data_file():
    base_folder = path.dirname(path.dirname(__file__))
    return path.join(base_folder,'data','SacramentoRealEstateTransactions2008.csv')

    
def load_file(filename):
      with open(filename,'r',encoding='utf-8') as fin:
          reader = csv.DictReader(fin)
          purchases = []
          for row in reader:                              
                p = Purchase.create_from_dict(row)
                purchases.append(p)

          return purchases          


def query_data(data): #list[Purchase]):
    #data.sort(key=get_price)
    data.sort(key=lambda p: p.price)
    #most expensive house
    high_purchase = data[-1]
    print("The most expensive house is: ${:,.2f} with {} beds and {} baths".format(high_purchase.price,high_purchase.beds,high_purchase.baths))

    #least expensive house
    low_purchase = data[0]
    print("The least expensive house is: ${:,.2f} with {} beds and {} baths".format(low_purchase.price,low_purchase.beds,low_purchase.baths))

    #average house price
    prices = [
        p.price #projection or items
        for p in data #the set to process               
    ]

    average_price = statistics.mean(prices)
    print("The least averate price is: ${:,.2f}".format(average_price))

    #average price of 2 bedroom houses
    two_bed_homes = (
        p #projection or items
        for p in data #the set to process   
        if announce(p,'2-bedrooms, found {}'.format(p.beds)) and (p.beds==2) #test condition
    )

    homes=[]
    for h in two_bed_homes:
       if len(homes)>5:
            break
       homes.append(h)

    average_price = statistics.mean((announce(p.price,'price') for p in homes))
    average_baths = statistics.mean((p.baths for p in homes))
    average_beds = statistics.mean((p.beds for p in homes))
    average_sqft= statistics.mean((p.sq__ft for p in homes))

    print('The least averate price of a 2 bedroom home is: ${:,.2f}, beds={},baths={}, sqft={:,}'.format(average_price,round(average_beds),round(average_baths,1),round(average_sqft,1)))

def announce(item,msg):
        print('Pulling item {} of {}'.format(item,msg))
        return item

if __name__ == '__main__':
    main()
