import cloudpickle
from flask import Flask, render_template, request
 
with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)
 
app = Flask(__name__)
 
@app.route('/')
def index():
  return render_template('index.html', nome='Job Change')
 
@app.route('/predicao', methods=['POST'])
def predicao():
  city = request.form['city']
  city_development_index = request.form['city_development_index']
  relevent_experience = request.form['relevent_experience']
  experience = request.form['experience']
  enrolled_university = request.form['enrolled_university']
  education_level = request.form['education_level']
  major_discipline = request.form['major_discipline']
  company_size = request.form['company_size']
  company_type = request.form['company_type']
  last_new_job = request.form['last_new_job']
  training_hours = request.form['training_hours']
 
  array=[[str(city), str(city_development_index), str(relevent_experience), str(experience), str(enrolled_university), str(education_level), str(major_discipline), str(company_size), str(company_type), str(last_new_job), str(training_hours)]]
 
  predicao = model.predict(array)
 
  return render_template('resposta.html', predicao=predicao[0])
 
app.run(debug=True)
 
# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
