num_things = int(input("How many activities do you have planned today? "))

if num_things > 1:
    break_time = int(input("How long are your breaks (in minutes)? "))
else:
    break_time = 0

todolist_times = []
hour_minute = []
names = []

print("Please input each activity in chronological order. Use 24-hr time.")

for i in range(num_things):
    num_string = "Activity " + str(i+1)
    activity_name = input(num_string + " name: ")
    start_time = input(num_string + " start time: ")
    start_hour_minutes = start_time.split(":")
    start_time = int(start_hour_minutes[0])*60 + int(start_hour_minutes[1])
    while i > 0 and start_time - todolist_times[i-1][1] < break_time:
        print("You need a", str(break_time), "minute break!")
        start_time = input(num_string + " start time: ")
        start_hour_minutes = start_time.split(":")
        start_time = int(start_hour_minutes[0])*60 + int(start_hour_minutes[1])
    end_time = input(num_string + " end time: ")
    end_hour_minutes = end_time.split(":")
    end_time = int(end_hour_minutes[0])*60 + int(end_hour_minutes[1])
    while end_time <= start_time:
        print("Invalid. End time has to be after start time!")
        end_time = input(num_string + " end time: ")
        end_hour_minutes = end_time.split(":")
        end_time = int(end_hour_minutes[0])*60 + int(end_hour_minutes[1])
    names.append(activity_name)
    time_range = (start_time, end_time)
    time_range_hm = (start_hour_minutes, end_hour_minutes)
    hour_minute.append(time_range_hm)
    todolist_times.append(time_range)

print("Schedule: ")

for i, j, k in zip(names, todolist_times, list(range(len(todolist_times)))):
    begin_time = j[0]
    end_time = j[1]
    str_begin = str(begin_time//60) + ":" + str(begin_time%60)
    str_end = str(end_time//60) + ":" + str(end_time%60)
    print("*\t" + i, "from", str_begin, "to", str_end)
    if k < len(todolist_times)-1:
        print("---break---")


