import pandas as pd
from pandas import DataFrame
from sklearn.datasets import load_iris


# sklearn.datasetsincludes common example datasets
def describe_iris(summary):
    iris_obj = load_iris()
    iris = DataFrame(
        iris_obj.data,
        columns=iris_obj.feature_names,
        index=pd.Index([i for i in range(iris_obj.data.shape[0])]),
    ).join(
        DataFrame(
            iris_obj.target,
            columns=pd.Index(["species"]),
            index=pd.Index([i for i in range(iris_obj.target.shape[0])]),
        )
    )

    return iris.describe(include="all").loc[summary]
