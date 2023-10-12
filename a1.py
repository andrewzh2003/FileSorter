from pathlib import Path
# a1.py

def path_checker(master_list):
    location = master_list[0]
    p1 = Path('.') / location
    if p1.exists():
        return True
    else:
        return False
    pass

def r_to_e(master_list, locc):
    file = []
    dirr = []
    extension = '.' + master_list[3]
    locate = Path(locc)
    for obj in locate.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        if extension in str(i):
            print(i)
    for i in dirr:
        r_to_e(master_list, i)

def r_to_s(master_list, locc):
    file = []
    dirr = []
    locate = Path(locc)
    for obj in locate.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        if master_list[3] in str(i):
            print(i)
    for i in dirr:
        r_to_s(master_list, i)
    return locate

def r_to_f(locc):
    file = []
    dirr = []
    locate = Path(locc)
    for obj in locate.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        print(i)
    for i in dirr:
        r_to_f(i)
    return locate

def r(locc):
    file = []
    dirr = []
    locate = Path(locc)
    for obj in locate.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        print(i)
    for i in dirr:
        print(i)
        r(i)
    return locate

def feature1(master_list):
    if path_checker(master_list) == True:
        list1 = ['-r', '-f', '-s', '-e']
        length = len(master_list)
        locc = master_list[0]
        thetruthtables = False
        ## checks to see if first command is -r
        if length > 2 and master_list[1] == list1[2] or master_list[1] == list1[3]:
            if master_list[2] != list1[0] or master_list[2] != list1[1]:
                thetruthtables = True
            else:
                thetruthtables = False
        if length > 2 and master_list[1] != list1[2] or master_list[1] != list1[3] or master_list[1] != list1[1]:
            if master_list[1] != list1[0]:
                pass
            else:
                thetruthtables = True
        if length == 2:
            if master_list[1] in list1:
                thetruthtables = True
            else:
                print('ERROR')
        if thetruthtables == True:
            ## checks to see if the input is valid
            if master_list[1] in list1:
                ## tests for r
                if master_list[1] == list1[0]: 
                    if length == 2:
                        r(locc)
                    if length == 3:
                        if master_list[2] == list1[1]:
                            ## tests for f after the r
                            if master_list[2] == list1[1]:
                                r_to_f(locc) 
                        else:
                            print('ERROR')
                    if length == 4:
                        if master_list[2] == list1[2] or master_list[2] == list1[3]:
                            ## tests for s after the r
                            if master_list[2] == list1[2]: 
                                r_to_s(master_list, locc)
                            ## tests for e after the r
                            if master_list[2] == list1[3]:
                                r_to_e(master_list, locc)
                        else:
                            print('ERROR')
                ## tests for f
                if master_list[1] == list1[1]:
                    file = []
                    dirr = []
                    first = Path(master_list[0])
                    for obj in first.iterdir():
                        if obj.is_file():
                            file.append(obj)
                        if obj.is_dir():
                            dirr.append(obj)
                    for i in file:
                        print(i)
                ## tests for s
                if master_list[1] == list1[2]:
                    file = []
                    dirr = []
                    first = Path(master_list[0])
                    for obj in first.iterdir():
                        if obj.is_file():
                            file.append(obj)
                        if obj.is_dir():
                            dirr.append(obj)
                    for i in file:
                        if master_list[2] in str(i):
                            print(i)
                ## tests for e
                if master_list[1] == list1[3]: 
                    file = []
                    dirr = []
                    extension = '.' + master_list[2]
                    first = Path(master_list[0])
                    for obj in first.iterdir():
                        if obj.is_file():
                            file.append(obj)
                        if obj.is_dir():
                            dirr.append(obj)
                    for i in file:
                        if extension in str(i):
                            print(i)
    else:
        pass
    return 

def C(master_list): ## creates file
    ## os. path. join(save_path, file_name)
    ## master_list == location command name
    list1 = ['-n']
    ## check that lsit of 1 is location 2 is -n and location 3 is a file name with no '.'
    if master_list[1] in list1:
        corrected_file = master_list[2] + ".dsu"
        full_name = master_list[0] + "\\" + corrected_file
        p1 = Path(".") / full_name
        if not p1.exists():
            p1.touch()
            print(full_name)
        else:
            print("ERROR")
    else:
        print("ERROR")
    return

def D(master_list): ## Deleting
    if len(master_list) > 3:
        second = master_list[2:len(master_list)] ## the file directory
        reversed_second = second[len(second):None:-1] ## reversing the directory
        location = reversed_second.index('.') ## taking the index of the first . after reversing to find extension
        extension = reversed_second[0:location] ## isolating the extention
        p1 = Path(".") / second
    
        if extension == "usd":
            if p1.exists():
                p1.unlink()
                print(f'{second} DELETED')
        else:
            print('ERROR')
    else:
        print("ERROR")
    return

def R(master_list):## reading the things
    if len(master_list) > 3:
        tester = True
        second = master_list[2:len(master_list)]
        reversed_second = second[len(second):None:-1]
        location = reversed_second.index('.')
        extension = reversed_second[0:location]
        p1 = Path(".") / second

        if extension == "usd":
            if p1.exists(): # check to see if file exists
                f = p1.open('r')
                single = f.read()
                f.close()
                if single == '':
                    tester = False
                    print("EMPTY")
                if tester:
                    f = p1.open('r')
                    for i in f.readlines():
                        print(i[:-1])
                    f.close()
        else:
            print("ERROR")
    else:
        print("ERROR")
    return

def run():
    initial_input = input()
    function_being_called  = initial_input[0:1]
    list1 = ['l', 'L', 'C', 'D', 'R', 'Q']
    list2 = ['l', 'L']
    list3 = ['c', 'C']
    thetruthtables = True

    if function_being_called not in list1:
        print('ERROR')
    if function_being_called.upper() in list1:
        if ' -' in initial_input:
            if function_being_called in list2:
                index_of_dash = initial_input.index(' -')
                length_of_input = len(initial_input)
                different_options = initial_input[index_of_dash:length_of_input].split()
                location = initial_input[2:index_of_dash].strip()
                master_list = [location] + different_options
            if function_being_called in list3: ### ho do dis
                index_of_dash = initial_input.index(' -')
            
                length_of_input = len(initial_input)
                
                option1 = initial_input[2:index_of_dash]
               
                second_part = initial_input[index_of_dash: length_of_input]
              
                counter = second_part.count(' -')
               
                if counter == 1:
                    first_part = initial_input[index_of_dash + 1:index_of_dash + 3]
                   
                    second_ = initial_input[(index_of_dash + 4):length_of_input]
                    
                    master_list1 = [option1] + [first_part] + [second_]
                else:
                    print('ERROR')
            if function_being_called == "Q" or function_being_called == "q":
                thetruthtables = False
                return
            elif function_being_called == "L" or function_being_called == 'l':
                feature1(master_list)
            elif function_being_called == 'C' or function_being_called == "c":
                C(master_list1)
            if function_being_called not in list1:
                print('ERROR')
        else:
            if function_being_called == 'D' or function_being_called == "d":
                D(initial_input)
            elif function_being_called == 'R' or function_being_called == "r":
                R(initial_input)
            elif function_being_called == 'L':
                file = []
                dirr = []
                places = initial_input[2:len(initial_input)]
                first = Path('.') / places
                for obj in first.iterdir():
                    if obj.is_file():
                        file.append(obj)
                    if obj.is_dir():
                        dirr.append(obj)
                for i in file:
                    print(i)
                for i in dirr:
                    print(i)
            elif function_being_called == "Q" or function_being_called == "q":
                thetruthtables = False
            else:
                print('ERROR')

    

    if thetruthtables:
        run()

if __name__ == "__main__":
    run()
