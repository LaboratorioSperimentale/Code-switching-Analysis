import collections


def print_tabular(input_datapath, output_path):

    data = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))

    with open(input_datapath, "r", encoding="utf-8") as fin:

        fin.readline()

        for line in fin:

            line = line.strip().split("\t")

            for i in range(1, len(line)):
                line[i] = int(line[i])

            PROFICIENCY, \
            LANG_HELP, LANG_UNDERSTAND, LANG_LEARN, LANG_ATM, \
            LING_HELP, LING_UNDERSTAND, LING_LEARN, LING_ATM = line

            data[PROFICIENCY]["LANG_HELP"][LANG_HELP]+=1
            data[PROFICIENCY]["LANG_UNDERSTAND"][LANG_UNDERSTAND]+=1
            data[PROFICIENCY]["LANG_LEARN"][LANG_LEARN]+=1
            data[PROFICIENCY]["LANG_ATM"][LANG_ATM]+=1

            data[PROFICIENCY]["LING_HELP"][LING_HELP]+=1
            data[PROFICIENCY]["LING_UNDERSTAND"][LING_UNDERSTAND]+=1
            data[PROFICIENCY]["LING_LEARN"][LING_LEARN]+=1
            data[PROFICIENCY]["LING_ATM"][LING_ATM]+=1


    for level in data:
        for el_name, el_data in data[level].items():
            data[level][el_name] = "\t".join(str(x) for x in el_data)


    with open(output_path, "w", encoding="utf-8") as fout:
        print("\tLANG_HELP\t\tLANG_UNDERSTAND\t\tLANG_LEARN\t\t" \
              "LANG_ATM\t\tLING_HELP\t\tLING_UNDERSTAND\t\tLING_LEARN\t\tLING_ATM",
              file=fout)

        for level in data:
            print(f"{level}\t{data[level]['LANG_HELP']}\t{data[level]['LANG_UNDERSTAND']}\t"\
                  f"{data[level]['LANG_LEARN']}\t{data[level]['LANG_ATM']}\t"\
                  f"{data[level]['LING_HELP']}\t{data[level]['LING_UNDERSTAND']}\t"\
                  f"{data[level]['LING_LEARN']}\t{data[level]['LING_ATM']}",
                  file=fout)


if __name__ == "__main__":

    _INPUT_DATAPATH = "../data/clean_data.tsv"
    _OUTPUT_PATH = "../data/desc.tsv"

    print_tabular(_INPUT_DATAPATH, _OUTPUT_PATH)