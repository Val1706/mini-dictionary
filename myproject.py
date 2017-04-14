print("\n Welcome to your dictionary! :)")
import csv

while True:

    with open("file.csv", "r") as readFile:
        readFileReader = csv.reader(readFile)
        readFile = []
        for row in readFileReader:
            if len(row) != 0:
                readFile = readFile + [row]
    print("\n", "-" * 125)
    all_acts = ["1", "2", "3", "4", "0"]
    print("1) Search explanation by appellation")
    print("2) Add new definition")
    print("3) Show all appellations alphabetically")
    print("4) Show available definitions by first letter of appellation ")
    print("0) Exit")
    answer = input()

    if answer in all_acts:

        if answer == "2":
            word = input("\nAdd word: ")
            describ = input("Add definition: ")
            source = input("Add source: ")
            tuple_n = (describ, source)


            with open("file.csv", "a") as wrFile:
                wrFileWriter = csv.writer(wrFile)
                wrFileWriter.writerow([word.capitalize(),tuple_n])
                wrFile.close()
                print("\n New word added to dictionary")

            with open("file.csv", "r") as readFile:
                readFileReader = csv.reader(readFile)
                readFile = []
                for row in readFileReader:
                    if len(row) != 0:
                        readFile = readFile + [row]

        if answer == "1":
            dct_n = dict(readFile)
            search = input("Type word: ")
            search = search.capitalize()
            if search.capitalize() in dct_n:
                for keys in dct_n:
                    dct_n[keys] = dct_n[keys].split("', '")
                    dct_n[keys][0] = dct_n[keys][0].split("('")
                    dct_n[keys][1] = dct_n[keys][1].split("')")
                    print("\n", search, "-", dct_n[keys][0][1], "\n", dct_n[keys][1][0])
                    break
            else:
                print("\n No", search, "definition")
                continue



        if answer == "3":
            dct_n = dict(readFile)
            var_dict = dct_n.keys()
            var_dict = list(var_dict)
            var_dict.sort()
            for keys in var_dict:
                dct_n[keys] = dct_n[keys].split("', '")
                dct_n[keys][0] = dct_n[keys][0].split("('")
                dct_n[keys][1] = dct_n[keys][1].split("')")
                print("\n", keys, "-", dct_n[keys][0][1], "\n", dct_n[keys][1][0])

        if answer == "4":
            dct_n = dict(readFile)
            let_inp = input("Type first letter: ")
            for keys in dct_n.keys():
                if keys.startswith(let_inp.capitalize()):
                    dct_n[keys] = dct_n[keys].split("', '")
                    dct_n[keys][0] = dct_n[keys][0].split("('")
                    dct_n[keys][1] = dct_n[keys][1].split("')")
                    print("\n", keys, "-", dct_n[keys][0][1], "\n", dct_n[keys][1][0])

    if answer == "0":
            break
    if answer not in all_acts:
        print("Please choose the option below:")


