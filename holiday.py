COST_PER_NIGHT=50
RENTAL_PER_DAY=30

DESTINATION_COST= {"NewYork":1000,"Paris":500, "Moscow":750, "Dubai":1000}

def flight_cost(city_flight):
      return(DESTINATION_COST[city_flight])
# define a function called hotel_cost with parameter num_nights
def hotel_cost(num_nights):
      X=num_nights*COST_PER_NIGHT
      return X
# define a function called car_rental with parameter rental_days
def car_rental(rental_days):
      y=rental_days*RENTAL_PER_DAY
      return y

# define function called holiday_cost with parameters city_flight,num_nights&rental)days
def holiday_cost(city_flight,hotel_nights,rental_days):
# sreate a variable called hotel_cost_result      
      hotel_cost_result=hotel_cost(num_nights)
# create a variable called car_result to hold cost of car rental using car_rental function
      car_rental_result=car_rental(rental_days)
# create a variable to hold cost of flight using function flight_cost.
      city_flight_result=flight_cost(city_flight) 
# create variable caled z by adding the other 3 function results          
      z=city_flight_cost_result+hotel_cost_result+car_rental_result
      return z
      
# ask user for city flight destination
city_flight=input("enter a city you want to travel to")
# ask user for nights in hotel
hotel_nights=int(input("number of nights in a hotel"))
# number of days car rental
car_rental=int(input("number of days you want to rent a car"))
# create variable holiday_cost_result also called z by adding other 3 functions
holiday_cost_result=city_flight_result+hotel_nights_result+car_rental_result
# print the holiday_cost_result
print(holiday_cost_result)
