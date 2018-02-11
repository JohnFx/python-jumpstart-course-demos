import requests
import bs4
import collections
import game24




WeatherReport = collections.namedtuple('WeatherReport','Location,Condition,Temperature')

def main():
    
    print_header()

    zip_code = input("What zipcode do you want the weather for? ")
    html = get_html_from_web(zip_code)
    report = get_weather_from_html(html)
    display_forecast(report)


def print_header():
    print("---------------------------------")
    print("            Weather App")
    print("---------------------------------")
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    print()
    print("Downloading weather report for {} ...".format(zipcode))

    if response.status_code>=400 and response.status_code<600: 
        return None
    else: 
        return response.text
       
def get_weather_from_html(html):

    if html==None:
        return WeatherReport(Location="Unknown",Temperature="Unknown",Condition="Unknown")

    else:
        soup = bs4.BeautifulSoup(html,'html.parser')
        location = soup.find(class_='city-header').find('h1').get_text().strip()
    
        temperature = soup.find(class_='current-temp').find(class_='wu-value').get_text().strip()
        temperature_scale = soup.find(class_='current-temp').find(class_='wu-label').get_text().strip() 

        conditions = soup.find(class_='condition-icon').find('p').get_text().strip()
        print(location);
        print("{} {}".format(temperature,temperature_scale));
        print(conditions);
    
        return WeatherReport(Location=location,Temperature=temperature + temperature_scale,Condition=conditions)


def display_forecast(report):
    print ("Location: {}".format(report.Location))
    print ("Conditions: {}".format(report.Condition))
    print ("Temperature: {}".format(report.Temperature))
    print()

if __name__ == "__main__": 
   main()

#get rid of keyerror