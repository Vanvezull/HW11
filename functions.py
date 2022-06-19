import json


#def homepage():



def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate(uid):
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        if uid > len(candidates):
            return "Error: 404 Такого кандидата нет!"
        else:
            for candidate in candidates:
                if candidate['id'] == uid:
                    return candidate


def get_candidates_by_name(name):
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        candidates_list = []
        for candidate in candidates:
            if name.lower() in candidate['name'].lower():
                candidates_list.append(candidate)
        return candidates_list


def get_candidates_by_skill(skill):
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        candidate_skills = []
        for candidate in candidates:
            skills = candidate["skills"].lower().split(", ")
            if skill.lower() in skills:
                #", ".join(skills)
                candidate_skills.append(candidate)
        return candidate_skills


#print(get_candidates_by_skill("go"))