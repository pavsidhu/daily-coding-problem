def interleave(list):
  queue = []
  pointer = 1
  
  while pointer < len(list):
    queue = list[pointer:]
    list = list[0:pointer]
    list.append(queue[-1])
    queue.pop()
    list += queue
    pointer += 2

  return list
