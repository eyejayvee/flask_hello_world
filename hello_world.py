from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
  return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
  html = """
    <h1>
      Hello {}!
    </h1>
    <p>
      Here is a picture of a kitten. Awww...
    </p>
    <img src="http://placekitten.com/g/200/300">
  """ 
  return html.format(name.title())

@app.route("/jedi/<name>/<surname>")
def jedi(name, surname):
  html = """
  <h1>
    May the force be with you {}{}
  </h1>
  <p>
    "It is an honour to meet a Jedi of your race."
  </p>
  """
  
  return html.format(surname[:3].title(),name[:2])
  
  return ""


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)