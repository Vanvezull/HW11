import json


#def homepage():



def load_candidates():
    """
    Загрузка полного списка кандидатов из файла json
    :return:
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate(uid):
    """
    Поиск кандидата по ID (функция)
    :param uid:
    :return:
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        if uid > len(candidates):
            return "Error: 404 Такого кандидата нет!"
        else:
            for candidate in candidates:
                if candidate['id'] == uid:
                    return candidate


def get_candidates_by_name(name):
    """
    Поиск кандидата по Имени (функция)
    :param name:
    :return:
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        candidates_list = []
        for candidate in candidates:
            if name.lower() in candidate['name'].lower():
                candidates_list.append(candidate)
        return candidates_list


def get_candidates_by_skill(skill):
    """
    Поиск кандидата по умению (функция)
    :param skill:
    :return:
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        candidate_skills = []
        for candidate in candidates:
            skills = candidate["skills"].lower().split(", ")
            if skill.lower() in skills:
                #", ".join(skills)
                candidate_skills.append(candidate)
        return candidate_skills
