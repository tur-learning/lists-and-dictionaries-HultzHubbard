from utils import *

filename = "rome.json"
rome_data = load_data(filename)

# cprint(type(rome_data))

# print(rome_data.keys())
# print(rome_data.values())
# print(rome_data.items())

features = rome_data.get("features", None) # if doesn't find "features", return "None"
# features = rome_data["features"] # riskier, could return error
# print(type(features))
# print(len(features))

element = features[0]
# print(type(element))
# print_dict(element)

# print(element.keys())
el_properties = element.get("properties", None)
# print_dict(el_properties)
el_name = el_properties.get("name", "Unknown Name")
el_geometry = element.get("geometry", None)
el_type = el_geometry.get("type", "Unknown Shape")

# print("Name: ", el_name, "; Shape:", el_type)

data = []
nasoni = []

for el in features:
    el_properties = el.get("properties", None)
    el_name = el_properties.get("name", "drinking_water")

    el_geometry = el.get("geometry", None)
    el_coords = el_geometry.get("coordinates", None)
    el_coords = extract_coords(el_coords)

    # data.append(el_dict)

    if el_name != "drinking_water":
        el_dict = {
        "name": el_name,
        "coordinates": el_coords
        }

        data.append(el_dict)
        # print("NAME: ", el_name, "; COORDINATES: ", el_coords)
    elif el_name == "drinking_water":
        el_dict = {
            "name": el_name,
            "coordinates": el_coords
        }

        nasoni.append(el_dict)


# print_dict(data)
# print(nasoni)

search_name = "colosseo"

for el in data:
    if el["name"].lower() == search_name:
        print_dict(el)
# for el in nasoni:
    # calculate distance from colosseo
    # find which one is closest