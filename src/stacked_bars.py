import numpy as np
import matplotlib.pyplot as plt

import labels as lab

data_proficiency = {"A2": {}, "B1": {}, "B2": {}, "C1": {}, "C2": {}}

with open("../data/clean_data.tsv") as fin:
    categories = fin.readline().strip().split("\t")[1:]
    for line in fin:
        line = line.strip().split("\t")

        prof = line [0]
        data = list(zip(categories, [int(x) for x in line[1:]]))

        for cat, yes_no in data:
            if not cat in data_proficiency[prof]:
                data_proficiency[prof][cat] = [0, 0]
            data_proficiency[prof][cat][yes_no] += 1

# whether to have it in percentage or raw frequencies
normalize = True

for category in categories:

    labels = ["A2", "B1", "B2", "C1", "C2"]

    data_yes = [data_proficiency[lab][category][1] for lab in labels]
    data_no = [data_proficiency[lab][category][0] for lab in labels]

    if normalize:
        data_yes_p = [data_yes[i]*100/(data_yes[i]+data_no[i]) for i in range(len(data_yes))]
        data_no_p = [data_no[i]*100/(data_yes[i]+data_no[i]) for i in range(len(data_yes))]

        data_yes = data_yes_p
        data_no = data_no_p

    plt.figure(figsize=(9, 7))

    plt.ylabel('Number of responses')
    if normalize:
        plt.ylabel("Percentage of responses")

    plt.title(f'{lab._DICT[category]}')

    plt.bar(labels, data_yes, fill=False, hatch='///', label="YES")
    plt.bar(labels, data_no, fill=False, hatch='...', bottom=np.array(data_yes), label="No")

    # plt.legend(loc="lower left", bbox_to_anchor=(0.8, 1.0))
    plt.legend()

    plttitle = f"../plots/{category}.png"
    if normalize:
        plttitle = f"../plots/{category}_percentage.png"

    plt.savefig(plttitle)
