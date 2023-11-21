import pandas as pd
import statsmodels.formula.api as smf


prof_categories = ["A1", "A2", "B1", "B2", "C1", "C2"]

data = pd.read_csv("../data/clean_data.tsv", sep="\t")


data["PROFICIENCY"] = data["PROFICIENCY"].astype("category")

variables = ["LANG_HELP", "LANG_UNDERSTAND", "LANG_LEARN", "LANG_ATM",
             "LING_HELP", "LING_UNDERSTAND", "LING_LEARN", "LING_ATM"]


with open("../data/binary_logit_models.txt", "w") as fout:
    for dep_variable in variables:
        print(f"#### {dep_variable} ~ PROFICIENCY ####\n", file=fout)
        model = smf.logit(formula = f"{dep_variable} ~ PROFICIENCY", data = data).fit()
        print(model.summary(), file=fout)
        print("\n\n\n", file=fout)