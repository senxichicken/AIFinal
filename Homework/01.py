'''複製，以下使用了ChatGPT來解答'''

import random


courses = [
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

newSlots = [""] * len(slots)

def schedule(target_hours, start_time):
    i = 0
    while i < len(courses):
        if courses[i]["hours"] == target_hours:
            for j in range(start_time, len(slots), 7):
                if newSlots[j] == "":
                    newSlots[j:j+target_hours] = [courses[i]["name"]] * target_hours
                    courses.remove(courses[i])
                    i -= 1
                    break
        i += 1

schedule(4, 0)
schedule(3, 1)
schedule(3, 4)
schedule(2, 2)
schedule(2, 4)
schedule(2, 0)
for i in range(1, 7): schedule(1, i)
schedule(1, 0)

for i in range(len(newSlots)):
    if i % 7 == 0: print()
    print(slots[i] + ": " + newSlots[i])

courses_copy = courses[:]
slots_copy = slots[:]


def is_slot_available(slot_index, target_hours):
    return all(newSlots[slot_index + i] == "" for i in range(target_hours))

def calculate_conflicts():
    conflicts = 0
    for i in range(len(newSlots)):
        if newSlots[i] != "":
            for j in range(i + 1, len(newSlots)):
                if newSlots[j] == newSlots[i]:
                    conflicts += 1
    return conflicts


def evaluate_schedule():
    conflicts = calculate_conflicts()
    return conflicts


def hill_climbing():
    current_conflicts = evaluate_schedule()
    
    
    max_iterations = 1000
    iterations = 0
    
    while current_conflicts > 0 and iterations < max_iterations and courses_copy:
        
        course_index = random.randint(0, len(courses_copy) - 1)
        course = courses_copy[course_index]
        
        slot_index = random.randint(0, len(slots_copy) - course["hours"] * 7)
        
        
        if is_slot_available(slot_index, course["hours"]):
            newSlots[slot_index:slot_index+course["hours"]] = [course["name"]] * course["hours"]
            courses_copy.pop(course_index)
            
            
            new_conflicts = evaluate_schedule()
            if new_conflicts < current_conflicts:
                current_conflicts = new_conflicts
            else:
                
                newSlots[slot_index:slot_index+course["hours"]] = [""] * course["hours"]
                courses_copy.insert(course_index, course)
        
        iterations += 1


hill_climbing()


print("Time Slots\tMonday\tTuesday\tWednesday\tThursday\tFriday")
print("-----------------------------------------------------------------------------------")
for i in range(len(newSlots) // 7):
    print(f"Slot {i+1:02d} ({slots[i*7]} - {slots[i*7+4]})\t", end="")
    for j in range(5):  
        print(f"{newSlots[i*7+j]:<10}\t", end="")
    print()

'''
輸出
Time Slots      Monday  Tuesday Wednesday       Thursday        Friday
-----------------------------------------------------------------------------------
Slot 01 (A11 - A15)     電子            電子            電子            電子            媒體
Slot 02 (A21 - A25)                     線代            線代            線代            工數
Slot 03 (A31 - A35)                     離散            離散            離散            動畫
Slot 04 (A41 - A45)                     視窗            視窗            視窗            嵌入
Slot 05 (A51 - A55)                     科學            科學            科學            網站
Slot 06 (B11 - B15)                     系統            系統            系統            網頁
Slot 07 (B21 - B25)                     計概            計概            計概            演算
Slot 08 (B31 - B35)                     軟工            軟工            軟工            結構
Slot 09 (B41 - B45)                     行動            行動            行動            智慧
Slot 10 (B51 - B55)                     網路            網路            網路            機率
'''