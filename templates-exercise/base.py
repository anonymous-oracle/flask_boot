from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    flags = {'upper':0, 'lower':0, 'number':0}
    name = request.args.get('username')
    for l in name:
        if ord('A') <= ord(l) and ord(l) <= ord('Z') and not flags['upper']:
            flags['upper']=1
            continue
        if ord('a') <= ord(l) and ord(l) <= ord('z') and not flags['lower']:
            flags['lower']=1
            continue
    if ord('0')<= ord(name[-1]) and ord('9')>=ord(name[-1]):
        flags['number']=1
    remarks = []
    if not flags['upper']:
        remarks.append('username should contain an uppercase alphabet')
    if not flags['lower']:
        remarks.append('username should contain a lowercase alphabet')
    if not flags['number']:
        remarks.append('username should end with a number')
    if remarks==[]:
        signal = 0
        return render_template('report.html', signal=signal)
    else:
        signal = 1
        return render_template('report.html', signal=signal, remarks=remarks)


if __name__=="__main__":
    app.run(debug=True)