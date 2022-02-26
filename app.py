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
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404  
if __name__=="__main__":
    app.run(port="5000")
    
        
