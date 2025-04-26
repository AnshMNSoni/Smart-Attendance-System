from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    headers = ['UID', 'Date', 'Time']
    
    if os.path.exists('rfid_log.csv'):
        with open('rfid_log.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            try:
                headers = next(reader)
                for row in reader:
                    if row:
                        data.append(row)
            except StopIteration:
                pass  # File exists but is empty

    return render_template('index.html', headers=headers, data=data)

if __name__ == '__main__':
    app.run(debug=True)
