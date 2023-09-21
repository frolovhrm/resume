"""Считаем колличество переговорок.
На входе список со временем начала и окончание встречь.
"""

print("\033c", end="")

work_time = [9, 17]  # рабочее время
meetings_time = ([10, 15], [9, 11], [16, 18])  # запланированные встречи [начало, окончание]
meetings_time +=([15, 18], [10, 15], [9, 11])
added = True
list_meets = {}


"""создает список из рабочего дня"""
def makeDay(work_time):
    work_day = []
    for i in range(work_time[0], work_time[1] + 1):
        work_day += [(i)]
    return work_day

""" создает список из времени встречи """
def makeMeetLineTime(s, f):
    lineTime = []
    for i in range(s, f):
        lineTime += [i]
    return lineTime

"""печатаем отчет о всех встечах"""
def printCheck(dict_meet, meet_times):
    print("Встреча\t   Время\tПереговорка")
    for key, value in dict_meet.items():
        print(f"{key + 1: ^7}\t   {meet_times[key - 1][0]:>2}-{meet_times[key - 1][1]:>2}\t{value + 1: ^11}")


print(f"Список встреч [начало, окончание] - {meetings_time} \n")
print(f"Количество встреч - {len(meetings_time)}\n")

# это списоок встреч для всех переговорках, создаем первое событие
meeting_day = [makeMeetLineTime(meetings_time[0][0], meetings_time[0][1])]


for meeting in range(len(meetings_time)):    # ищем место для каждой встречи
    if meeting == 0:
        list_meets[0] = 0  # добавляем в номер встречи номер переговорки
        continue

    for m in range(len(meeting_day)):   # проверяем все переговорки
        listOneMeet = makeMeetLineTime(
            meetings_time[meeting][0], meetings_time[meeting][1]) # спосок времени очередной встречи

        # если пересечений в этой переговорке нет, добавляем сюда встречу 
        if set(listOneMeet).isdisjoint(set(meeting_day[m])):
            for i in listOneMeet:
                meeting_day[m].append(i)
            meeting_day[m].sort()
            list_meets[meeting] = m + 1 # добавляем в номер встречи номер переговорки
            added = True
            break
        else:
            added = False
            continue

    if added == False:  # если места нет во всех переговорках, то создаем новую переговорку
        meeting_day.append(listOneMeet)
        list_meets[meeting] = m + 1  # добавляем в номер встречи номер переговорки
        # print(f"Новая переговорка{meeting_day}\n")

print(f"Всего потребуется переговорок - {len(meeting_day)}\n")

print(meetings_time)
printCheck(list_meets, meetings_time)
print("")
