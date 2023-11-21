import pandas as pd
import statsmodels.formula.api as smf


prof_categories = ["A1", "A2", "B1", "B2", "C1", "C2"]

data = pd.read_csv("../data/clean_data.tsv", sep="\t")


data["PROFICIENCY"] = data["PROFICIENCY"].astype("category")

variables = ["LANG_HELP", "LANG_UNDERSTAND", "LANG_LEARN", "LANG_ATM",
             "LING_HELP", "LING_UNDERSTAND", "LING_LEARN", "LING_ATM"]


with open("../data/binary_logit_models_2.txt", "w") as fout:
    for dep_variable in variables:
        for dep_variable_2 in variables:
            if not dep_variable == dep_variable_2:
                print(f"#### {dep_variable} ~ {dep_variable_2} ####\n", file=fout)
                model = smf.logit(formula = f"{dep_variable} ~ {dep_variable_2}", data = data).fit()
                print(model.summary(), file=fout)
                print("\n\n", file=fout)