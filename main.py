from flask import Flask, render_template, request, session, redirect, url_for
import json
import io
from datetime import datetime
from PIL import Image

# DETECTION SCRIPTS
import anpr
import google_sheets_api


# FLASK APPLICATION
app = Flask(__name__)


# HOME PAGE
@app.route("/")
def homePage():
    return render_template("index.html")


# DASHBOARD - POWER BI
@app.route("/dashboard")
def showDashboard():
    return render_template("dashboard.html")


# DETECTION FROM IMAGES
@app.route("/from-image")
def imagePage():
    return render_template("detection-form.html", data_type="Image")

# DETECTION FROM VIDEOS


@app.route("/from-video")
def videoPage():
    return render_template("detection-form.html", data_type="Video")


# RESULTS
@app.route("/results", methods=['POST'])
def showResults():
    try:
        if request.method == 'POST':
            f = request.files['formFile']
            f.save('static/uploads/'+f.filename)
            file_type = request.form['file_type']
            global text, date, time, states
            date = datetime.now().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")
            with open("./static/jsons/states_abbreviations.json")as file:
                states = json.load(file)

            if file_type == 'Image':
                text, regions = anpr.detect_from_image(
                    './static/uploads/'+f.filename)
                image_pil = Image.fromarray(regions)
                # text = ['HR 26 DA 2330']
                image_pil.save("./static/downloads/"+f.filename)
                return render_template('results.html', text=text, date=date, time=time, states=states, fn=f.filename, file_type=file_type)

            if file_type == 'Video':
                text = anpr.detect_from_video('./static/uploads/'+f.filename)
                # text = ['HR 26 DA 2330']
                return render_template('results.html', text=text, date=date, time=time, states=states, fn=f.filename, file_type=file_type)
    except:
        return '<html><head><link rel="stylesheet" href="./static/css/styles.css" /></head><body><script type="text/javascript">alert("Either you did not attach the image or used the wrong file format. Please upload a png or jpeg file.");window.location = "/from-image";</script></body></html>'


# SAVING DATA TO GOOGLE SHEETS
@app.route("/saveData")
def save_data():
    try:
        global text, date, time, states
        for plate in text:
            google_sheets_api.append_data(
                plate, date, time, states.get(plate[:2]))
        return '<html><head><link rel="stylesheet" href="./static/css/styles.css" /></head><body><script type="text/javascript">alert("Data has been saved and update successfully.");window.location = "/";</script></body></html>'
    except:
        return '<html><head><link rel="stylesheet" href="./static/css/styles.css" /></head><body><script type="text/javascript">alert("Unable to save the data, please try again");window.location = "/";</script></body></html>'


# DATABASE - VIEW ALL STORED PLATES
@app.route("/database")
def show_database():
    try:
        data = google_sheets_api.fetch_data()
        return render_template("database.html", data=data)
    except:
        return '<html><head><link rel="stylesheet" href="./static/css/styles.css" /></head><body><script type="text/javascript">alert("Server Busy: Too many requests made to the Google API, Please try again after a minute or so");window.location = "/";</script></body></html>'


# TECHNOLOGIES USED
@app.route("/technologies")
def technologies():
    return render_template("technologies.html")


# SEARCH
@app.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        query = request.form['plate_query']
        message, result = google_sheets_api.execute_query(query)
        return render_template("search_query.html", message=message, result=result)


# CHAT
@app.route("/chat")
def chat():
    data = google_sheets_api.fetch_data()
    return render_template("chat.html", data=str(data))


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
