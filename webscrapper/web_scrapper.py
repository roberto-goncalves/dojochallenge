import sys, urllib, json, random, re, time, os


endpoint = os.environ['ENDPOINT']
file_path = os.environ['FILEPATH']

while True:

 response = urllib.urlopen(endpoint)
 data = json.loads(response.read())
 random_fortune = data[random.randrange(len(data))]

 with open(file_path) as f:
  replaced = f.read()

 regex = re.compile('<[\w\W]+\>(.+)<\/\w+>')
 match = regex.match(replaced)  # This returns a list of all matches
 str_to_replace = match.group(1)  # 1 index is the string in between the tags
 replaced = replaced.replace(str_to_replace, random_fortune['message'])

 with open(file_path, "w") as f:
  f.write(replaced)

 time.sleep(10)
