_type = {
    "a" : ['photo',['.png', '.jpg']], 
    "b" : ['video', ['.mkv', '.mp4']], 
    "c" : ["text" , ['.txt']], 
    "d" : ['code', ['.py', '.c', '.cpp', '.java', '.php', '.js', '.html', '.css']] 
}


const_prompt = '''I will provide you with a distorted movie name. Please search the internet to find the actual movie name and its release year. The output should be strictly in the format: Movie_name (released year). Ensure that there is no additional information, no descriptions, no styling, and no extra whitespace or newline characters.

Distorted Name: '''

instruction_manual = {
  'a' : 'uppercase',
  'b' : 'lowercase',
  'c' : 'GEM'
}