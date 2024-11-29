

def frange(start, stop, step=0.25):
    if step == 0:
        print("Please select a valid step count")
    else:
        return_list = [start]
        y = start
        while y < stop-step:
            y += step
            return_list.append(round(y,2))
        return return_list
        
print(list(frange(1, 3)))