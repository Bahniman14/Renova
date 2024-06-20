import os
import google.generativeai as genai
from constants import const_prompt
from private import api_key


def GEM(current_filename):
   os.environ["GOOGLE_API_KEY"] = api_key
   genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
   model = genai.GenerativeModel(model_name="gemini-1.5-flash") 
   question = const_prompt + current_filename
   response = model.generate_content([question])
#    print(response.text)
   return response.text

def Rename_function(folder_directory, _type, instructions): #prompt is for other format files like  
    # Check if the folder exists
    if not os.path.isdir(folder_directory):
        print(f"Error: The folder {folder_directory} does not exist.")
        return

    # Iterate over all files in the folder
    for filename in os.listdir(folder_directory):
        file_path = os.path.join(folder_directory, filename)
        
        # Check if it's a file (and not a directory)
        if os.path.isfile(file_path):
            # Check if the file extension matches any in the _type list
            file_name, file_extension = os.path.splitext(filename)
            if file_extension in _type:
                # Create the new filename based on the instructions
                if instructions == "uppercase":
                    new_file_name = file_name.upper()
                elif instructions == "lowercase":
                    new_file_name = file_name.lower()
                elif instructions == 'GEM':
                    new_file_name = GEM(file_name)
                    print('before omit:')
                    print(new_file_name)

                    new_file_name = new_file_name[:-1]
                    print('after omit:')
                    print(new_file_name)
                
                new_filename = new_file_name + file_extension
                new_file_path = os.path.join(folder_directory, new_filename)
                
                # Rename the file
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {filename} to {new_filename}")
                except Exception as e:
                    print(f"Error renaming file {filename}: {e}")


