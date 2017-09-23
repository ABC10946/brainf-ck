import sys

def bf_interpreter(script,mode=0):
    #mode 0 is default mode,1 is step mode,2 is output immediately
    output = []
    _script = script + "E" #add char that tell finish script

    LFF = 0 #Loop Fold Flag
    LFL_stack = [] #Loop Fold Location stack
    sc = 0 #script counter
    memory = [0 for x in range(32)]
    p = 0
    count = 0
    error_flag = 0

    while _script[sc] != "E":
        count += 1
        if _script[sc] == "+":
            memory[p] += 1

        elif _script[sc] == "-":
            if memory[p] != 0:
                memory[p] -= 1

        elif _script[sc] == ">":
            p += 1
            if p > 31:
                print("error out of memory!")
                error_flag = 1
                break

        elif _script[sc] == "<":
            p -= 1
            if p < 0:
                print("error out of memory!")
                error_flag = 1
                break

        elif _script[sc] == "[":
            LFF += 1
            LFL_stack.append(sc)

        elif _script[sc] == "]":
            if memory[p] != 0:
                sc = LFL_stack[-1]
            else:
                LFF -= 1
                LFL_stack.pop(-1)

        elif _script[sc] == ".":
            if mode == 1 or mode == 2:
                print("output:",chr(memory[p]))


            output.append(chr(memory[p]))

        elif _script[sc] == ",":
            try:
                memory[p] = input("input:")
            except EOFError:
                print("")
                break
            except KeyboardInterrupt:
                print("")
                break

        else:
            print("error \""+script[sc]+"\" command is undefined.")
            error_flag = 1
            break

        sc += 1

        if mode == 0: #default mode
            pass
        elif mode == 2: #output immediately
            pass
        elif mode == 1: #step mode
            print("counter:",count)
            print("memory")
            print(memory)
            if p == 0: #memory cursor
                print(" ^")
            elif p == memory[len(memory)-1]:
                s_memory = map(str,memory)
                print(" "*(len(", ".join(s_memory))-1)+"^")
            else:
                s_memory = map(str,memory[0:p+1])
                print(" "*(len(", ".join(s_memory)))+"^")

            #script cursor
            print("script")
            print(script)
            print(" "*(sc-1)+"^")
            try:
                input("Enter to next step")
            except EOFError:
                print("")
                break
            except KeyboardInterrupt:
                print("")
                break

        else:
            print("error mode is undefined.")
            error_flag = 1
            break

    if error_flag == 0:
        print("".join(output))

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            file_name = sys.argv[1]
            bfIO = open(file_name)
            script = bfIO.read()
            script = script.replace("\n","")
            if len(sys.argv) == 3:
                mode = int(sys.argv[2])
                bf_interpreter(script,mode)
            else:
                bf_interpreter(script)

        except IOError:
            print("file not found!")
    else:
        print("error file undefined!")
