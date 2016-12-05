'''

Stanley Zeng
CS 1114
sz1911

Purpose of program
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    myFile = open(complete_weather_filename)
    File = open(cleaned_weather_filename, "w")
    for i in myFile:
        myString = i
        mySplit = myString.split(",")
        City = mySplit[0]
        Date = mySplit[1]
        High = mySplit[2]
        Low = mySplit[3]
        if (mySplit[8].isdigit == False):
            Prep = 0
        else:
            Prep = mySplit[8]
        File.write(City + "," + Date + "," + High + "," + Low + "," + Prep)
    


# Part B
def f_to_c(f_temperature):
    return ((f_temperature * 1.8) + 32)
    
def in_to_cm(inches):
    return (2.54 * inches)

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    myFile = open(imperial_weather_filename)
    File = open(metric_weather_filename, "w")
    for i in myFile:
        myString = i
        mySplit = myString.split(",")
        City = mySplit[0]
        Date = mySplit[1]
        High = f_to_c(float(mySplit[2]))
        Low = f_to_c(float(mySplit[3]))
        if (mySplit[8].isdigit == False):
            Prep = 0
        else:
            Prep = in_to_cm(float(mySplit[8]))
        File.write(City + "," + Date + "," + str(High) + "," + str(Low) + "," + str(Prep))
    


"""
# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    # prints average highs and lows in each month for the given city



# Part D
# Write your question (as a comment), and implement a function to answer it



def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    # add your code here
    

    
main()
"""