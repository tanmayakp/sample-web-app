from flask import Flask
import json
 
app = Flask(__name__)
version  = 'v4'
# with open("config.json") as f:
#     version=json.load(f)['version']
#     print(version)

with open("version.txt") as f:
    version = f.readlines()[0]
 
@app.route('/')
def hello_world():
    return 'Hello there!, This is {}'.format(version)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')