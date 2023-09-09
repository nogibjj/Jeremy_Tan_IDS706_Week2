import pandas as pd
from pandas import DataFrame
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport


def describe_iris(summary):
    """uses .describe() to find descriptive stats,
    the summary argument requires any of the values in
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

    ex. "max", "mean", "min"... "freq"
    """
    iris_obj = load_iris()
    iris = DataFrame(
        iris_obj["data"],
        columns=iris_obj["feature_names"],
        index=pd.Index([i for i in range(iris_obj["data"].shape[0])]),
    ).join(
        DataFrame(
            iris_obj["target"],
            columns=pd.Index(["species"]),
            index=pd.Index([i for i in range(iris_obj["target"].shape[0])]),
        )
    )

    return iris.median(), iris.describe(include="all").loc[summary]


def general_describe(csv):
    """general describe function in csv"""
    general_df = pd.read_csv(csv)
    return general_df.describe()


def generate_viz_iris():
    """generates example visualziation for iris dataset"""
    iris_obj = load_iris()

    iris = DataFrame(
        iris_obj["data"],
        columns=iris_obj["feature_names"],
        index=pd.Index([i for i in range(iris_obj["data"].shape[0])]),
    )

    iris.hist(edgecolor="black", linewidth=1)
    plt.show()


def generate_vis_general_congress(csv):
    """generate example visualization of the congress dataset"""
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    # print(general_df.head())
    print(general_df.describe())
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["age"], bins=20, edgecolor="black")
    plt.title("Age Distribution of Congress Members")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()


def generate_summary_iris():
    """generates report for iris dataset"""
    iris_obj = load_iris()

    iris = DataFrame(
        iris_obj["data"],
        columns=iris_obj["feature_names"],
        index=pd.Index([i for i in range(iris_obj["data"].shape[0])]),
    )
    profile = ProfileReport(iris, title="Profiling Report")
    profile.to_file("iris.html")


def generate_summary(csv):
    """generates report of any dataset"""
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")
