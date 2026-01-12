from flask import Flask,render_template, request
app - Flask(__name__)
@app.router("/", methods=["GET", "POST"])
def index ():
  result +""
    if request.method == "POST":
        news = request. form.get("news")
        #demo output 
        return render_template("index.html",result=result)
        if __name__ == "__main__":
            app.run(debug=True)
