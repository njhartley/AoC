def add_path_to_directories(path, directories):
    if path not in directories.keys():
        directories[path] = 0
    return directories


def solution():
    f = open('./Day7 Input.dat', 'r')
    f.readline()
    directories_size = {"/":0}
    current_stack = ["/"]
    current_path = "/"
    for line in f:
        if line.startswith("$ cd"):
            if not line.startswith("$ cd .."):
                current_path += f"/{line.split()[-1]}" if current_path != "/" else line.split()[-1]
                current_stack.append(current_path)
                directories_size = add_path_to_directories(current_path, directories_size)

##            elif line.strip() == "$ cd /":
##                current_path = "/"
##                current_stack = ["/"]
##                directories_size = add_path_to_directories(current_path, directories_size)

            elif line.strip() == "$ cd ..":
                current_path = "/".join(current_path.split("/")[:-1])
                current_stack.pop()

        if line[0].isdigit():
            file_size = int(line.split()[0])
            for directory in current_stack:
                directories_size[directory] += file_size

    final_list_task_1 = [el for el in directories_size.values() if el <= 100000]
    print("Task 1:")
    print(sum(final_list_task_1))

    MAX_USED_SIZE = 7e7-3e7
    current_root_size = directories_size["/"]
    space_to_free = current_root_size - MAX_USED_SIZE
    final_list_task_2 = sorted([el for el in directories_size.values() if el >= space_to_free])
    print("Task 2:")
    print(final_list_task_2[0])
solution()
