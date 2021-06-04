from flask import Flask, request, render_template
import resumeranking

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/resumes', methods=['POST'])
def resumes():
    job_desc = request.form['job_desc']
    print(job_desc)

    df = resumeranking.start(job_desc)

    return render_template('home.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
