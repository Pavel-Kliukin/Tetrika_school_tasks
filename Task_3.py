def appearance(intervals):

    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    # Находим самое первое событие (начало урока или самый первый вход в систему ученика либо учителя)
    # Это будет нулевая точка отсчёта на временной оси
    start = min(min(lesson), min(pupil), min(tutor))

    # Уменьшаем все временные точки на величину start (привязываем к нулевой точке отсчёта)
    lesson = list(map(lambda x: x - start, lesson))
    pupil = list(map(lambda x: x - start, pupil))
    tutor = list(map(lambda x: x - start, tutor))
    # БЫЛО:
        # 'lesson': [1594663200, 1594666800],
        # 'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        # 'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
    # СТАЛО:
        # 'lesson': [0, 3600],
        # 'pupil': [140, 189, 190, 195, 196, 3272],
        # 'tutor': [90, 230, 243, 3273]

    # Находим самое последнее событие на временной оси (конец урока или выход из системы ученика либо учителя)
    finish = max(max(lesson), max(pupil), max(tutor))
    time_line = []  # Это временная ось от самого первого события до самого последнего
    for i in range(finish+1):
        time_line.append([0, 0, 0])

    # Помечаем на временной оси все секунды урока:
    for time in range(lesson[0]+1, lesson[1]+1):
        time_line[time][0] = 1
    # Помечаем на временной оси все секунды присутствия ученика:
    for i in range(0, len(pupil), 2):
        for time in range(pupil[i]+1, pupil[i+1]+1):
            time_line[time][1] = 1
    # Помечаем на временной оси все секунды присутствия учителя:
    for i in range(0, len(tutor), 2):
        for time in range(tutor[i]+1, tutor[i+1]+1):
            time_line[time][2] = 1
    # Считаем секунды в которые одновременно был урок и присутствовали ученик с учителем:
    appearance_time = 0
    for i in time_line:
        if i == [1, 1, 1]:
            appearance_time += 1

    return appearance_time
