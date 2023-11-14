import pandas as pd


# with open("data/source_data_correct.tsv", "w") as fout:
#     with open("data/source_data_reduced.tsv") as fin:
#         for lineno, line in enumerate(fin):
#             line = line.strip().split("\t")
#             if len(line) == 6:
#                 print("\t".join([line[0], line[3]]), file=fout)
#             else:
#                 print(lineno, len(line))

from pandas.api.types import CategoricalDtype


prof_categories = ["A1Beginner", 
                    "A2 Elementary English",
                    "B1Intermediate",
                    "B2 Upper-Intemediate",
                    "C1 Advanced English",
                    "C2 Proficiency English"]

cat_type_proficiency = CategoricalDtype(categories=prof_categories, ordered=True)
cat_type_help = CategoricalDtype(categories=["No", "Yes"], ordered=True)

data = pd.read_csv("data/source_data_manual.tsv", sep="\t")

data["proficiency_level"] = data["proficiency_level"].astype(cat_type_proficiency)
data["help_language"] = data["help_language"].astype(cat_type_help)
# data["help_linguistics"] = data["help_linguistics"].astype(cat_type_help)

print(data.dtypes)

# data = pd.get_dummies(data, columns=['proficiency_level', 'help_language'], drop_first=True)
# data = pd.get_dummies(data, columns=['proficiency_level'], drop_first=True)

print(data.dtypes)

from statsmodels.miscmodels.ordinal_model import OrderedModel

mod_prob = OrderedModel(data['help_language'],
                        data["proficiency_level"],
                        distr='logit')



# data[["proficiency_level_A2 Elementary English", "proficiency_level_B1Intermediate", "proficiency_level_B2 Upper-Intemediate", "proficiency_level_C1 Advanced English", "proficiency_level_C2 Proficiency English"]],

res_prob = mod_prob.fit(method='bfgs')
res_prob.summary()