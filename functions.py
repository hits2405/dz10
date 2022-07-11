import json


def load_candidates():  # загрузит данные из файла и вернет
    with open("candidates.json", "r", encoding='utf-8') as f:
        candidates = json.load(f)
        return candidates


def get_all():  # покажет всех кандидатов
    uploads = (load_candidates())
    lists = ""
    for i in uploads[0:]:
        name_s = i['name']
        pk_s = i['pk']
        skill_s = i['skills']
        lists += f'Имя кандидата - {name_s}\n'
        lists += f'Позиция кандидата - {pk_s}\n'
        lists += f'Навыки - {skill_s}\n\n'
    return lists


def get_by_pk(pk: int) -> dict:  # вернет кандидата по pk
    uploads = (load_candidates())
    for i in uploads[0:]:
        if i['pk'] == pk:
            return i


def get_by_skill(skill_name: str) -> str:  # вернет кандидатов по навыку
    uploads = (load_candidates())
    lists = ""
    for i in uploads[0:]:
        if skill_name.lower() in i['skills'.lower()]:
            name_s = i['name']
            pk_s = i['pk']
            skill_s = i['skills']
            lists += (f'Имя кандидата - {name_s}\n')
            lists += (f'Позиция кандидата - {pk_s}\n')
            lists += (f'Навыки - {skill_s}\n\n')
    return lists


