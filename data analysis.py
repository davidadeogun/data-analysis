with open("life-expectancy.csv") as lives:
    inter = iter(lives)  #To iterate through the dataset, I used the built in function 'iter'
    next_inter = next(inter)  #and 'next'
    
    second_data = []    #converts raw data from csv into list
    min = 10000
    max = 0
    countryName = ""
    year  = 0

    #This formats the data into the desired output
    #and appends the formatted data to the variable "second_data"
    for line in lives:
        stripped_life = line.strip()  #Strips the raw data
        parts = stripped_life.split(",")  #splits the data into 4 parts, separated by a comma
        
        #Below is each of the sections available in the raw data, assigned to a variable
        country = parts[0]    #remains a string
        code = parts[1]     #remains a string
        year = int(parts[2]) #converts the year into an integer
        expectancy = float(parts[3])  #Converts this into a float

        second_data.append([country, code, year, expectancy])  #Moves each of the sections into a list and append to the list variable
                                                                   #For example, I can't change a string of year into an int
#This checks the data and prints the max life expectancy
for element in second_data:
    if (element[3] > max):
        max = element[3]
        year = element[2]
        countryName = element[0]
print(f"The overall max life expectancy is: {max} from {countryName} in {year}")


#This checks the data and prints the min life expectancy
for element in second_data:
    if (element[3] < min):
        min = element[3]
        year = element[2]
        countryName = element[0]
print(f"The overall min life expectancy is: {min} from {countryName} in {year}")

print()
year_of_interest = int(input("Enter the year of interest: "))
new_countryName = ""
max_year = 0
min_year = 10000
print()
count_life_expectancy = [x[3] for x in second_data] #counts the each life expectancy in the data

#sums the occurences up and divide the total by the number of occurences
average_life_expectancy = sum(count_life_expectancy) / len(count_life_expectancy)

print(f"The average life expectancy across all countries was {average_life_expectancy :.2f}") #Prints the average
# looping in the data list
for element in second_data:
    # checking if the current element is greater than a year_of_interest
    if element[2] == year_of_interest:
        # check if current element is greater than max_year
        if element[3] > max_year:
            # updating max_year_pop
            max_year = element[3]
            # updating max_year_countryName
            new_countryName = element[0]
# prints the result
print()
print(f"For the year {year_of_interest}: ")
print(f"The max life expectancy was in {new_countryName} with {max_year :2f}")

for element in second_data:
    # checking if the current element is greater than a year_of_interest
    if element[2] == year_of_interest:
        # check if current element is greater than max_year
        if element[3] < min_year:
            # updating max_year_pop
            min_year = element[3]
            # updating max_year_countryName
            new_countryName = element[0]
# prints the result
print(f"The min life expectancy was in {new_countryName} with {min_year :.2f}")