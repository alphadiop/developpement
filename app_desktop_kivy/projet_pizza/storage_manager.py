import json
import os


class StorageManager:
    def load_data(self,data_name):
        filename = self.get_filename(data_name)
        try:
            file = open(filename,"r")
            data = file.read()
            file.close()
        except:
            return None
        return json.loads(data) #deserialiser les données provenant du reseau

    def save_data(self,data_name,data_content):
        filename = self.get_filename(data_name)
        data_str = json.dumps(data_content) # serialiser
        file = open(filename,"w")
        data = file.write(data_str)
        file.close()

    def get_filename(self,data_name):
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, data_name + ".json")
        ## print(f"file_path : {file_path}")
        return data_name + ".json"