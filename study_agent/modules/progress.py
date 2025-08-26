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
