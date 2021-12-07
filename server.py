from flask import Flask, render_template

app = Flask(__name__)
projects = [{"name": "Airplane", "description": "We build airplanes", "portrait": "/static/airplane.png"},
            {"name": "Car", "description": "We build cars", "portrait": "/static/car.png"},
            {"name": "3D Printer", "description": "We build 3D printers", "portrait": "/static/printer.png"},
            {"name": "DIY", "description": "We build DIY solar panels", "portrait": "/static/panel.png"}]

links = ["/projects", "https://youtube.com"]

@app.route("/")
def get_index():
    return render_template('index.html')

@app.route("/projects")
def get_projects():
    return render_template('projects.html', projects=projects)

@app.route("/siteinfo")
def get_siteinfo():
    return render_template('siteinfo.html')