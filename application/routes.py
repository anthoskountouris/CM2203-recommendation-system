
from flask import render_template,redirect, url_for, Flask, request, flash
from application.forms import SearchForm
from application.models import Job


from application import app
from flask import render_template,redirect, url_for

from application.functions import create_dataset, string_into_integer, predict, integer_to_string, read_string_for_array


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/recommendations", methods=['POST', 'GET'] )
def recommendation():
    text = request.form.get('text')
    dataset = create_dataset(text)
    print(dataset)

    #setting all the values of the database into unquie numbers
    for i in range(len(dataset[0]) - 1):
        coloumn = string_into_integer(dataset, i)
    labelset = string_into_integer(dataset, len(dataset[0]) - 1)
    num_neighbors = 3
    row = dataset[-1]
    dataset.pop()
    label = predict(dataset, row, num_neighbors)
    print(integer_to_string(labelset, label))
    return render_template("recommendations.html", index=True, user_data = integer_to_string(labelset, label))

@app.route("/result/<d>", methods=['POST', 'GET'] )
def result(d):
    return render_template("results.html", index=True, predict_value = read_string_for_array(d))



@app.route('/home/find',methods=['POST','GET'])
def find():
    form = SearchForm()
    if request.method == 'GET':
        return render_template('find.html', title="Find", form=form)
    if request.method == 'POST':
        if request.form.get('search'):
            if form.validate_on_submit():
                keywords = [
                    ["business", "development", "develop", "manager", "information", "data", "security", "systems",
                     "project", "IT", "infrastructure", "project"],
                    ["engineer", "quantitive", "finance", "ICT", "support", "analyst", "technician", "monitoring",
                     "evaluation", "monitor", "advisor", "apprentice"],
                    ["contracts", "manager"],
                    ["database", "administrator"],
                    ["software", "engineer", "frontend", "developer", "javascript"],
                    ["staff", "nurse", "doctor"],
                    ["internal", "sales", "engineer"],
                    ["teacher", "education", "instructor", "professor"]
                ]
                categories = {0: "Project ManagementInformation Technology", 1: "Information Technology",
                              2: "ManagementManufacturing", 3: "ResearchAnalystInformation Technology",
                              4: "EngineeringInformation Technology", 5: "Health Care Provider",
                              6: "SalesBusiness Development", 7: "EducationTraining"}
                for i in range(0, len(keywords)):
                    if form.search_job.data in keywords[i]:
                        search_job = Job.query.filter(Job.function.contains(categories[i]))
                        return render_template("find.html", search_job=search_job, form=form, Job=Job)
                flash('No jobs found!')
                return render_template('find.html', title="Find", form=form, Job=Job)

