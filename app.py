from flask import Flask, render_template, request


from kantei_main import kantei_uma
from kantei_main import kantei_kisyu



#配列をグローバル変数と指定
#uma
#kisyu

global uma
global kisyu
global kusei_nen
global kusei_tuki
global kusei_hi




uma = []
kisyu = []

kusei_nen = ""
kusei_tuki = ""
kusei_hi = ""

data_kusei = []



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/kakusu_select", methods=['GET', 'POST'])

#index.htmlからの遷移
def kakusu_select():
    if request.method == 'POST':
        # POSTデータを取得
        user_data = request.form
        kusei_nen = request.form.get('kusei_nen')
        kusei_tuki = request.form.get('kusei_tuki') 
        kusei_hi = request.form.get('kusei_hi')
        seletc_form_id = request.form.get('select_form_id')
     
        data_kusei.append(kusei_nen)
        data_kusei.append(kusei_tuki)
        data_kusei.append(kusei_hi)

        print(data_kusei)

        if seletc_form_id == "kisyu":
            return render_template("kisyu_form.html",data_kusei = data_kusei)
        elif seletc_form_id == "uma":
            return render_template("uma_form.html",data_kusei = data_kusei)
        else:
            return render_template("no-kakusu.html")
    else:
        return render_template("index.html")


@app.route("/kisyu_form", methods=['GET', 'POST'])
def kisyu_form():

    if request.method == 'POST':
        # POSTデータを取得
        #uma = request.form.getlist('uma')     
        kusei_nen = request.form.get('kusei_nen')
        kusei_tuki = request.form.get('kusei_tuki')
        kusei_hi = request.form.get('kusei_hi')

        
        kisyu = []
        for i in range(1, 19):
            kisyu.append(request.form['kisyu' + str(i)])


        kotae = kantei_kisyu(kisyu,kusei_nen,kusei_tuki,kusei_hi)
        
        if kotae[0] == "errer":
            return render_template("errer.html",kotae = kotae)
        elif kotae[0] != "errer":
            return render_template("kisyu_kantei.html",kotae = kotae)
    else:
        return render_template("no-kakusu.html")


@app.route("/uma_form", methods=['GET', 'POST'])
def uma_form():
    if request.method == 'POST':
        # POSTデータを取得
        kusei_nen = request.form.get('kusei_nen')
        kusei_tuki = request.form.get('kusei_tuki')
        kusei_hi = request.form.get('kusei_hi')

        
        uma = []
        for i in range(1, 19):
            uma.append(request.form['uma' + str(i)])   
   
        kotae = kantei_uma(uma,kusei_nen,kusei_tuki,kusei_hi)
  
    
        if kotae[0] == "errer":
            return render_template("errer.html",kotae = kotae)
        elif kotae[0] != "errer":
            return render_template("uma_kantei.html",kotae = kotae)
    else:
        return render_template("no-kakusu.html")       

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
