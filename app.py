from flask import Flask, render_template, request

import katakana


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/kakusu2/", methods=['GET', 'POST'])
def kakusu_valu2():
    if request.method == 'POST':
        user_data = request.form
        kotae = katakana.katakana_kantei(user_data)
        if kotae[0] == "errer":
            return render_template("errer.html",kotae = kotae)
        else:
            return render_template("kantei.html",kotae = kotae)
    else:
        return render_template("no-kakusu.html")


        


if __name__ == "__main__":
    app.run()
