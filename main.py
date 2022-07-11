from flask import Flask
from functions import get_all, get_by_skill, get_by_pk

app = Flask(__name__)


@app.route("/")  # главная со всеми кандидатами
def page_index():
    a = get_all()
    return f'<pre>{a}</pre>'


@app.route("/candidates/<int:pk>")  # выбор кандидата по номеру
def candidates(pk):
    a = get_by_pk(pk)
    url = a['picture']
    name = a['name']
    pk = str(a['pk'])
    skills = a['skills']
    return f'<img src=({url})>\n<pre>Имя кандидата - {name}\nПозиция кандидата - {pk}\nНавыки - {skills}</pre>'


@app.route("/skills/<skill_name>") # выбор кандидата по навыкам
def skills_name(skill_name):
    a = get_by_skill(skill_name)
    return f'<pre>{a}</pre>'


if __name__ == '__main__':
    app.run()
