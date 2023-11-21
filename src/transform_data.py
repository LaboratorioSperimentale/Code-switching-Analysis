
def clean_data(input_datapath, output_datapath, discarded_datapath):

    # proficiency_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    columns = ["PROFICIENCY",
               "LANG_HELP", "LANG_UNDERSTAND", "LANG_LEARN", "LANG_ATM",
               "LING_HELP", "LING_UNDERSTAND", "LING_LEARN", "LING_ATM"]

    with open(output_datapath, "w", encoding="utf-8") as fout, \
       open(discarded_datapath, "w", encoding="utf-8") as fout_discarded:

        print("\t".join(columns), file=fout)
        print("\t".join(columns), file=fout_discarded)

        with open(input_datapath, "r", encoding="utf-8") as fin:
            fin.readline()

            for line in fin:
                line = line.strip().split("\t")

                proficiency, \
                think_language, help_language, \
                think_linguistics, help_linguistics = line

                proficiency = proficiency.split(" ")[0]

                if not help_language == "-":
                    help_language = 1 if help_language == "Yes" else 0

                if not help_linguistics == "-":
                    help_linguistics = 1 if help_linguistics == "Yes" else 0


                if think_language == "-":
                    lang_understanding_yes = "-"
                    lang_understanding_no = "-"

                    lang_learning_yes = "-"
                    lang_learning_no = "-"

                    lang_atmosphere_yes = "-"
                    lang_atmosphere_no = "-"

                else:

                    think_language = think_language.split(",")

                    lang_understanding_yes = 0
                    lang_understanding_no = 0

                    lang_learning_yes = 0
                    lang_learning_no = 0

                    lang_atmosphere_yes = 0
                    lang_atmosphere_no = 0

                    for element in think_language:
                        element = element.strip()
                        if element.startswith("They should never code"):
                            pass
                        elif element.startswith("They should not"):
                            pass
                        elif element.startswith("It can facilitate"):
                            lang_understanding_yes = 1
                        elif element.startswith("It DOES NOT facilitate stu"):
                            lang_understanding_no = 1
                        elif element.startswith("It facilitates"):
                            lang_learning_yes = 1
                        elif element.startswith("It DOES NOT facilitate lang"):
                            lang_learning_no = 1
                        elif element.startswith("It creates"):
                            lang_atmosphere_yes = 1
                        elif element.startswith("It DOES NOT create"):
                            lang_atmosphere_no = 1


                if think_linguistics == "-":
                    ling_understanding_yes = "-"
                    ling_understanding_no = "-"

                    ling_learning_yes = "-"
                    ling_learning_no = "-"

                    ling_atmosphere_yes = "-"
                    ling_atmosphere_no = "-"
                else:

                    think_linguistics = think_linguistics.split(",")

                    ling_understanding_yes = 0
                    ling_understanding_no = 0

                    ling_learning_yes = 0
                    ling_learning_no = 0

                    ling_atmosphere_yes = 0
                    ling_atmosphere_no = 0

                    for element in think_linguistics:
                        element = element.strip()
                        if element.startswith("They should never code"):
                            pass
                        elif element.startswith("They should not"):
                            pass
                        elif element.startswith("It can facilitate"):
                            ling_understanding_yes = 1
                        elif element.startswith("It DOES NOT facilitate stu"):
                            ling_understanding_no = 1
                        elif element.startswith("It facilitates"):
                            ling_learning_yes = 1
                        elif element.startswith("It DOES NOT facilitate lang"):
                            ling_learning_no = 1
                        elif element.startswith("It creates"):
                            ling_atmosphere_yes = 1
                        elif element.startswith("It DOES NOT create"):
                            ling_atmosphere_no = 1


                try:
                    assert((lang_learning_yes == "-" and lang_learning_no == "-") or \
                        (lang_learning_yes+lang_learning_no <= 1))

                    assert((lang_understanding_yes == "-" and lang_understanding_no == "-") or \
                        (lang_understanding_yes+lang_understanding_no <= 1))

                    assert((lang_atmosphere_yes == "-" and lang_atmosphere_no == "-") or \
                        (lang_atmosphere_yes+lang_atmosphere_no <= 1))

                    assert((ling_learning_yes == "-" and ling_learning_no == "-") or \
                        (ling_learning_yes+ling_learning_no <= 1))

                    assert((ling_understanding_yes == "-" and ling_understanding_no == "-") or \
                        (ling_understanding_yes+ling_understanding_no <= 1))

                    assert((ling_atmosphere_yes == "-" and ling_atmosphere_no == "-") or \
                        (ling_atmosphere_yes+ling_atmosphere_no <= 1))
                except AssertionError:
                    print("REMOVING LINE:", line)
                    pass


                toprint = [proficiency,
                           help_language, lang_learning_yes, lang_understanding_yes, lang_atmosphere_yes,
                           help_linguistics, ling_learning_yes, ling_understanding_yes, ling_atmosphere_yes]
                toprint = [str(x) for x in toprint]

                if "-" in toprint:
                    print("\t".join(toprint), file=fout_discarded)
                else:
                    print("\t".join(toprint), file=fout)

                # print(f"{proficiency}\t{help_language}\t{lang_learning_yes}\t{lang_understanding_yes}\t{lang_atmosphere_yes}\t{help_linguistics}\t{ling_learning_yes}\t{ling_understanding_yes}\t{ling_atmosphere_yes}",
                #       file=fout)


if __name__ == "__main__":

    _INPUT_DATAPATH = "../data/estrazione.tsv"
    _OUTPUT_DATAPATH = "../data/clean_data.tsv"
    _DISCARDED_DATAPATH = "../data/discarded_data.tsv"

    clean_data(_INPUT_DATAPATH, _OUTPUT_DATAPATH, _DISCARDED_DATAPATH)