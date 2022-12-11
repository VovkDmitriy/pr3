def func():
    notes = []
    dates = []
    while(True):
        print("Додати нотатку:(Для виходу ввести !)")
        note = input()
        if note == "!":
            break
        print("Кількість днів")
        day = int(input())
        dates.append(day)
        notes = func2(notes, note)
        i = 0
        while(i < len(notes) - 1):
            j = 0
            while(j < len(notes) - i - 1):
                if(dates[j] > dates[j + 1]):
                    tempDay = dates[j]
                    tempNote = notes[j]
                    dates[j] = dates[j + 1]
                    notes[j] = notes[j + 1]
                    dates[j + 1] = tempDay
                    notes[j + 1] = tempNote
                j = j + 1
            i = i + 1
        k = 0
        while(k < len(notes)):
            print("Note: ", notes[k], "Days: ", dates[k])
            k = k + 1

def func2(list, note):
    list.append(note)
    return list
    

    

if __name__ == '__main__':
    func()
    



