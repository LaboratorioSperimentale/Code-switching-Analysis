import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from textwrap import wrap

import labels as lab


data = pd.read_csv("../data/clean_data.tsv", sep="\t")

with open("../data/clean_data.tsv") as fin:
    categories = fin.readline().strip().split("\t")[1:]

# whether to have it in percentage or raw frequencies
normalize = True

for cat1 in categories:
    for cat2 in categories:
        if cat1 < cat2:

            if normalize:
                confusion_matrix = pd.crosstab(data[cat1], data[cat2],
                                               rownames=['\n'.join(wrap(lab._DICT[cat1], 50))],
                                               colnames=['\n'.join(wrap(lab._DICT[cat2], 50))],
                                               normalize=True)
            else:
                confusion_matrix = pd.crosstab(data[cat1], data[cat2],
                                               rownames=['\n'.join(wrap(lab._DICT[cat1], 50))],
                                               colnames=['\n'.join(wrap(lab._DICT[cat2], 50))])

            confusion_matrix.sort_index(level=0, ascending=True, inplace=True)

            plt.figure(figsize=(7, 7), layout="tight")
            sns.set(font_scale=1.4)
            if normalize:
                sns.heatmap(confusion_matrix, annot=True, square=True, cmap="Blues",
                            cbar=False, fmt=".2f", annot_kws={"size": 20})
            else:
                sns.heatmap(confusion_matrix, annot=True, square=True, cmap="Blues",
                            cbar=False, fmt="d", annot_kws={"size": 20})

            plt.xlim(0, 2)
            plt.ylim(0, 2)

            plttitle = f"../plots/CM.{cat1}.{cat2}.png"
            if normalize:
                plttitle = f"../plots/CM.{cat1}.{cat2}.percentage.png"

            plt.savefig(plttitle)
            plt.clf()