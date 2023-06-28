from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/project1')
def project1():
    return render_template("project1.html")

@app.route('/project2')
def project2():
    return render_template("project2.html")

@app.route('/project3')
def project3():
    return render_template("project3.html")

@app.route('/project4')
def project4():
    return render_template("project4.html")

@app.route('/project5')
def project5():
    return render_template("project5.html")

if __name__ == "__main__":
    app.run(host='192.168.0.191', port=5000, debug=True)
