import pandas as pd
from pandas import DataFrame
from sklearn.datasets import load_iris


def describe_iris(summary):
    """uses .describe() to find descriptive stats"""
    iris_obj = load_iris()
    iris = DataFrame(
        iris_obj["data"],
        columns=iris_obj["feature_names"],
        index=pd.Index([i for i in range(iris_obj["data"].shape[0])]),
    ).join(
        DataFrame(
            iris_obj.target,
            columns=pd.Index(["species"]),
            index=pd.Index([i for i in range(iris_obj["target"].shape[0])]),
        )
    )

    return iris.describe(include="all").loc[summary]
