import sys

def bf_interpreter(script,step=0):
    output = []
    _script = script + "E" #add char that tell finish script

    LFF = 0 #Loop Fold Flag
    LFL = 0 #Loop Fold Location

    sc = 0 #script counter
    memory = [0 for x in range(32)]
    p = 0

    while _script[sc] != "E":
        if _script[sc] == "+":
            memory[p] += 1

        elif _script[sc] == "-":
            memory[p] -= 1

        elif _script[sc] == ">":
            p += 1
            if p > 32:
                print "error out of memory!"
                break

        elif _script[sc] == "<":
            p -= 1
            if p < 0:
                print "error out of memory!"
                break

        elif _script[sc] == "[":
            LFF += 1
            LFL = sc

        elif _script[sc] == "]":
            if memory[p] != 0:
                sc = LFL
            else:
                LFF -= 1

        elif _script[sc] == ".":
            if step == 1:
                print chr(memory[p])

            output.append(chr(memory[p]))

        elif _script[sc] == ",":
            memory[p] = input()

        sc += 1

        if step != 1:
            pass
        else:
            print memory
            print script
            print " "*(sc-1)+"^"
            raw_input()

    print "".join(output)

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        bfIO = open(file_name)
        script = bfIO.read()
        script = script.replace("\n","")
        if len(sys.argv) == 3:
            step = int(sys.argv[2])
            bf_interpreter(script,step)
        else:
            bf_interpreter(script)
    except IOError:
        print "file not found!"
