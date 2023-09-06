"""
Test goes here

"""

from main import describe_iris


def test_describe_iris():
    """Function calling describe_iris and tests different parts of the dataset"""

    # print(describe_iris("std"))

    assert describe_iris("mean").loc["sepal length (cm)"] == 5.843333333333334
    assert describe_iris("max").loc["species"] == 2.0
    assert describe_iris("std").loc["petal width (cm)"] == 0.7622376689603465


if __name__ == "__main__":
    test_describe_iris()
