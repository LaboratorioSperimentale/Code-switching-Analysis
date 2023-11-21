- [Intro](#intro)
- [Code](#code)
  - [Step1: `transform_data.py`](#step1-transform_datapy)
  - [Step2: `desc_statistics.py`](#step2-desc_statisticspy)
  - [Step3: Statistical inference](#step3-statistical-inference)
  - [Step4: Visualization](#step4-visualization)


# Intro

This repository contains code developed for the project [INSERT PROJECT NAME].
The study investigates [INSERT THEME] and was presented/submitted at []()

The project was developed by researchers [Antonella Luporini](https://www.unibo.it/sitoweb/antonella.luporini), ..., the statystical description and analysis was developed with the support of [Laboratorio Sperimentale](https://site.unibo.it/laboratorio-sperimentale/it).

# Code

This code is concerned with the analysis of a subset of questions discussed in the cited work.

Specifically, these questions investigate the opinions expressed by students about code-switching situations, both during English language and English linguistics lessons.

The original questionnaire was composed of 32 questions, we specifically examine 5 of these:

    a. What is your proficiency level in the English Language?
    b. What do you think about English language teachers' code-switching? More than one answer is possible
    c. In your opinion, when your English language teachers code-switch, does it help you pay more attention and feel more involved?
    d. What do you think about English Linguistics lecturers' code-switching? More than one answer is possible
    e. In your opinion, when your LECTURERS code-switch does it help you pay more attention and feel more involved?


For question (a), participants could select one of the 6 [CEFR levels](https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions) (A1 - Beginner to C2 - Proficient).

For questions (c) and (e), participants could choose either "Yes" or "No" as an answer.

For question (b) and (d), participants were asked to choose a subset of the following possibilities:
- They should never code-switch from English to Italian
- They should not code-switch in classes for advanced and proficient students (C1-C2)
- It can facilitate student understanding
- It DOES NOT facilitate student understanding
- It facilitates language learning
- It DOES NOT facilitate language learning
- It creates a positive atmosphere
- It DOES NOT create a positive atmosphere


The remainder of this file describes the scripts used to manipulate original data.
[ESTRAZIONE is available?]

## Step1: `transform_data.py`

The script turns responses collected for questions (b) and (d) into three binary variables (namely, one concerning student understanding, one concerning learning and the third one concerning class atmosphere).
It produces the files `data/clean_data.tsv` and `data/discarded_data.tsv` as output.
Each line in the files pertains to a specific participant:
    - participants that gave inconsistent answeres are filtered out
    - missing replies are indicated with a `-` symbol and stored in the `discarded_data.tsv` file
    - the `clean_data.tsv` file is the one containing all the participants that provided complete answers and is therefore the one we will be considering from this step onwards.


## Step2: `desc_statistics.py`

The script aggregates responses based on level and variable and prints them in tabular format on file `data/desc.tsv`

## Step3: Statistical inference

We tested the dataset following two different hypotheses:
1. Is the distribution of yes/no answers to the 8 posed questions significantly different depending on the proficiency level of the students?

To approach this question, we explored both binary logistic regression (`binary_logistic_regression.py`) and linear regression (`OLS.py`).

Results are provided in the files `data/binary_logit_models.txt` and `data/OLS_models.txt` respectively.


2. Is there a relation among the 8 considered variables at large?

In order to test this, we employed binary logistic regression (`binary_logit_regression_2.py`).
Results are provided in the files `data/binary_logit_models_2.txt`.

## Step4: Visualization

The two scripts `stacked_bars.py` and `matshow.py` provide visualization of descriptive statistics.


---

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
