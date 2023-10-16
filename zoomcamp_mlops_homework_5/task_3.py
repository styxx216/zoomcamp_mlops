from flask import Flask
print('start')
app = Flask('churn-app') # give an identity to your web service
@app.route('/ping',methods=['GET'])
def ping():
    return 'PONG'

app.run(debug=True, host='localhost', port=9696)