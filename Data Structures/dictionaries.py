name = "Bidhas Mongar"
age = 19
height = 161
is_student = True

personal_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
#adding Key-Value Pair 
print(personal_info)
personal_info["Favourite Color"] = "Yellow"
print(personal_info)
#using try and except to handle KeyError
try:
    print(personal_info["hobby"])
except KeyError as e:
    print(f"Error:{e}")