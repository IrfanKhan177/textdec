from flask import Flask, render_template ,request
app = Flask(__name__)

@app.route("/")
def hello():
    
    param ={'title':'Home'}
    return render_template('index.html',param=param)

@app.route("/analyzed")
def analyzed():
  text = request.args.get('text','default')
  rem = request.args.get('rem','off')
  if rem == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    ana =""
    for char in text:
      if char not in punctuations:
        ana = ana + char
    param = {
      'hed':'Analyzed text',
      'antext':ana,'title':'Without Punctuations',
    }
  
    return render_template('ana.html',param=param)
  else:
    return "Choose any option."
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port='5000')
