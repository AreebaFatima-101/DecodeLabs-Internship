# ============================================================
# Project 2 : Data Classification Using AI
# DecodeLabs Artificial Intelligence Internship
# Author : Areeba Fatima
# ============================================================

# -----------------------------
# Import Required Libraries
# -----------------------------

import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# -----------------------------
# Display Project Header
# -----------------------------

print("=" * 65)
print("              DATA CLASSIFICATION USING AI")
print("=" * 65)
print("DecodeLabs Artificial Intelligence Internship")
print("Project 2")
print("=" * 65)


# -----------------------------
# Load Dataset
# -----------------------------

print("\nLoading Iris Dataset...")

iris = load_iris()

print("Dataset Loaded Successfully!\n")


# -----------------------------
# Convert into DataFrame
# -----------------------------

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

data["Species"] = iris.target


# -----------------------------
# Display Dataset Information
# -----------------------------

print("=" * 65)
print("FIRST FIVE RECORDS")
print("=" * 65)

print(data.head())


print("\n" + "=" * 65)
print("DATASET INFORMATION")
print("=" * 65)

print(data.info())


print("\n" + "=" * 65)
print("STATISTICAL SUMMARY")
print("=" * 65)

print(data.describe())


print("\n" + "=" * 65)
print("DATASET SHAPE")
print("=" * 65)

print("Rows    :", data.shape[0])
print("Columns :", data.shape[1])


print("\n" + "=" * 65)
print("FEATURE NAMES")
print("=" * 65)

for feature in iris.feature_names:
    print("-", feature)


print("\n" + "=" * 65)
print("TARGET CLASSES")
print("=" * 65)

for index, name in enumerate(iris.target_names):
    print(index, ":", name)


print("\n" + "=" * 65)
print("CHECKING FOR MISSING VALUES")
print("=" * 65)

print(data.isnull().sum())


# -----------------------------
# Prepare Features and Labels
# -----------------------------

print("\nPreparing Features and Target...\n")

X = data.iloc[:, :-1]

y = data["Species"]

print("Features Prepared Successfully.")
print("Target Prepared Successfully.")


print("\nFeature Matrix Shape :", X.shape)
print("Target Vector Shape  :", y.shape)