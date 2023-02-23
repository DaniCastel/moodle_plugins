"""
This script obtains all Moodle plugins and generates a csv with the list of plugins and the latest version
Author: Daniela Castellanos
"""
import requests
import json
from collections import OrderedDict
import csv


API_URL = "https://download.moodle.org/api/1.3"
API_PLUGINS_ROUTE = "/pluglist.php"

def create_csv(plugins):
    with open("latest_versions.csv", "w") as csv_file:
        fieldnames = ["component_id", "name", "version"]
        writer = csv.DictWriter(csv_file, delimiter='|', fieldnames=fieldnames)
        writer.writeheader()

        for plugin in plugins:
            print(plugin)
            component_id = plugin["component"]
            name = plugin["name"]
            last_version = plugin["versions"].pop()

            writer.writerow({
                'component_id': component_id,
                'name': name,
                'version': last_version["version"],
            })

    print("File generation finished!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    plugins = OrderedDict()
    response = requests.get(API_URL + API_PLUGINS_ROUTE)
    response.json()

    # f = open('plugins.json')
    # data = json.load(f)
    data = response.json()
    plugins = data['plugins']

    create_csv(plugins)

    # f.close()


