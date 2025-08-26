def ask_difficulty(subjects):
    print("Informe a dificuldade de cada topico (1 = facil, 5 = muito dificil):")
    for subject in subjects:
        for topic in subject["topics"]:
            while True:
                try:
                    diff = int(input(f"{subject['subject']} - {topic['name']}: "))
                    if 1 <= diff <= 5:
                        topic['difficulty'] = diff
                        break
                    else:
                        print("Digite um numero entre 1 e 5.")
                except ValueError:
                    print("Digite um numero valido.")
    return subjects

def update_progress(subjects):
    print("Informe o progresso de cada topico (0 a 100%):")
    for subject in subjects:
        for topic in subject["topics"]:
            while True:
                try:
                    prog = float(input(f"{subject['subject']} - {topic['name']}: "))
                    if 0 <= prog <= 100:
                        topic['progress'] = prog / 100
                        break
                    else:
                        print("Digite um valor entre 0 e 100.")
                except ValueError:
                    print("Digite um numero valido.")
    return subjects
