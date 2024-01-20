import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    def program_agencies(self):
        # Decode the bytes to a string
        programs = json.loads(self.get_programs().decode('utf-8'))
        programs_list = [program["agency"] for program in programs]
        return programs_list

# Create an instance of GetPrograms
programs_instance = GetPrograms()

# Call program_agencies method to get the list of agencies
agencies = programs_instance.program_agencies()

# Print unique agencies
for agency in set(agencies):
    print(agency)
