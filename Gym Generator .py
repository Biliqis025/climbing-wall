
import random 
from datetime import datetime,timedelta  


# Creating connection 
# Creating gym names and id number  

gym_names = [ 
    {'name':'Planet Fitness', 'id':1},
    {'name':'East Bank Club','id':2},
    {'name':'La.Fitness','id':3},
    {'name':'Anytime Fitness','id':4}
]    
  
Directions = ['North','South','East','West']
wall_type =['Vert','Slab','Overhang'] # Notes

for gym in gym_names:
    no_of_walls=random.randint(1,5)  #  add randomnumbers
    gym['walls'] = [f"{random.choice(Directions)} {random.choice(wall_type)}" 
                          for _ in range(no_of_walls)]
for gym in gym_names:
    print(f"Gym: {gym['name']}") 

hold_color=['red','orange','yellow','green','blue']
Manufacturer=['Escape','SoIll','Atomik','EuroHolds','Metolious']
hold_type=['1a','2b','3c','4d','5e']
startdate= datetime(2024,11,21)
enddate= datetime(2024,11,22) 

for gym in gym_names:  # adding lanes to each of the walls 
    gym["lanes"] = {}
    for wall in gym["walls"]:
        num_lanes = random.randint(1, 2)  
        gym["lanes"][wall] = [f"Lane {i+1}" for i in range(num_lanes)]
for gym in gym_names:
    print(f"lanes: {gym}")


# adding hold_setes to each gym
        # need to work on this 
for gym in gym_names:
    num_hold_sets = random.randint(3, 5)  # random numbers 
    gym["holds"] = []
    for _ in range(num_hold_sets):  # Using _ instead of i because it is an undefined variable.
        color = random.choice(hold_color)
        manufacturer = random.choice(Manufacturer)
        hold_count = random.randint(25, 50) 
        {
            "color": color,
            "manufacturer": manufacturer,
            "holds": [f"{color} {i+1}" for i in range(hold_count)],
            "type": random.choice(hold_type),
        }
        gym["holds"].append(num_hold_sets)

for holds in gym["holds"]:
        print(f" Holds:{holds}")

    # generating Random attribute for the routes
# figure this part out 
def random_date(start, end):
    
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

route_setters = ['Bloom', 'Stella', 'Aisha', 'Musa', 'Techa','Flora']
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

for gym in gym_names:
    gym["routes"] = []
    for wall, lanes in gym["lanes"].items():
        for lane in lanes:
            num_routes = random.randint(1, 3)  
            for _ in range(num_routes):
                route = {
                    "name": f"Route_{random.randint(1000, 9999)}", 
                    "lane": lane,
                    "setter": random.choice(route_setters), 
                    "difficulty": random.randint(5, 12), 
                    "date_set": random_date(start_date, end_date),
                    "date_down": random_date(start_date, end_date),
                }
                
                if route["date_down"] < route["date_set"]:
                    route["date_down"] = route["date_set"] + timedelta(days=random.randint(1, 30))
                
                gym["routes"].append(route)
for route in gym["routes"]:
        print(f"  Route: {route}")



#for gym in gym_names:
   # print(gym)
#for gym in gym_names:
    #print(f"Gym: {gym['name']}, Hold Sets: {gym['holds']}")



for wall, lanes in gym["lanes"].items():
        print(f"  Wall: {wall}, Lanes: {lanes}")



        

   #to generate and insert sqls      
def generate_insert_gym_data(gym):
    return f"INSERT INTO gym (gymID) VALUES ('{gym['id']}');"

def generate_insert_wall_data(gym):
    insert_queries = []
    for wall in gym['walls']:
        insert_queries.append(f"INSERT INTO wall (name, gymID) VALUES ('{wall}', '{gym['id']}');")
    return insert_queries


def generate_insert_lane_data(gym): # 
    insert_queries = []            # this creates a list to hold the sqls that has been generated 
    for wall, lanes in gym["lanes"].items(): # forst for loop for esch hold set in the gym
        for lane in lanes:                 # sub for loop for individual hold in the hold set 
            wall_name = wall.split()[1]  
            insert_queries.append(f"INSERT INTO lane (num, wall_name, gymID) VALUES ({lane.split()[1]}, '{wall_name}', '{gym['id']}');") 
            # to generate sql statement for each table with values from sql
    return insert_queries

def generate_insert_hold_data(gym):
    insert_queries = []
    hold_id = 1  
    for hold_set in gym["holds"]:
        for hold in hold_set["holds"]:
            insert_queries.append(f"INSERT INTO hold (id, manufacturer, type) VALUES ({hold_id}, '{hold_set['manufacturer']}', '{hold_set['type']}');")
            hold_id += 1
    return insert_queries

def generate_insert_route_data(gym):
    insert_queries = []
    for wall, lanes in gym["lanes"].items():
        for lane in lanes:
            route_name = f"Route {random.randint(1, 100)}"
            setter = f"Setter {random.randint(1, 10)}"
            difficulty = random.randint(5, 15)  #  random numbers 
            date_set = random_date(startdate, enddate)  # for random dates
            date_down = random_date(startdate, enddate)
            insert_queries.append(f"INSERT INTO route (name, lane_num, wall_name, gymID, setter, difficulty, date_set, date_down) "
                                  f"VALUES ('{route_name}', {lane.split()[1]}, '{wall}', '{gym['id']}', '{setter}', {difficulty}, '{date_set}', '{date_down}');")
    return insert_queries


# 