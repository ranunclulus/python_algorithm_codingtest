import queue
def solution(priorities, location):
    printer = queue.Queue()

    max_prio = max(priorities)
    while(sum(priorities) != -len(priorities)):
        for i in range(len(priorities)):
            if priorities[i] == max_prio and max_prio != -1:
                printer.put(i)
                priorities[i] = -1
                max_prio = max(priorities)

    for i in range(printer.qsize()):
        num = printer.get()
        if num == location:
            return i + 1