from flask import Flask, render_template

app=Flask(__name__)


data_mahasiswa=[
    {
        'nama: ', 'acan jaikar',
        'alamat :', 'sasa'
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data mahasiswa")
def data_mahasiswa():
    return render_template("mahasiswa.html", data_mahasiswa=data_mahasiswa)

if __name__=="__main__":
    app.run(debug=True)
