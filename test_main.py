"""
Test goes here

"""

from main import describe_iris, general_describe

example_csv = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"


def test_describe_iris_and_general_describe():
    """Function calling describe_iris and tests different parts of the dataset"""

    # print(describe_iris("std"))

    assert describe_iris("mean").loc["sepal length (cm)"] == 5.843333333333334
    assert describe_iris("max").loc["species"] == 2.0
    assert describe_iris("std").loc["petal width (cm)"] == 0.7622376689603465

    # only works for the example_csv link
    assert general_describe(example_csv).loc["mean", "Year"] == 2017.0
    assert general_describe(example_csv).loc["count", "Year"] == 41715.0


if __name__ == "__main__":
    test_describe_iris_and_general_describe()
