gravity_planet_count=0
for key, value in final_dict.items():
  if "gravity"in value:
    gravity_planet_count+=1

print(gravity_planet_count)    

type_planet_count=0
for key, value in final_dict.items():
  if"planet_type" in value:
    type_planet_count+=1

print(type_planet_count)    

planet_not_gravity_support=[]
for planet_data in planet_data_rows:
  if planet_data not in low_gravity_planets:
    planet_not_gravity_support.append(planet_data)

type_no_gravity_planet_count=0
for planet_data in planet_not_gravity_support:
  if planet_data[6].lower()=="terrestrial"or planet_data[6].lower()=="super earth":
    type_no_gravity_planet_count+=1

    print(type_no_gravity_planet_count)
print(type_planet_count/type_no_gravity_planet_count)    

goldilock_planet_count=0
for key, value in final_dict.items():
  if"goldilock" in value:
    goldilock_planet_count+=1

print(goldilock_planet_count)    

speed_planet_count=0
for key, value in final_dict.items():
  if"speed" in value:
    speed_planet_count+=1

print(speed_planet_count)    