"""
Test goes here

"""

from main import describe_iris


def test_describe_iris():
    """Function calling describe_iris"""

    # print(describe_iris("mean"))
    # print(describe_iris("mean").keys())
    assert describe_iris("mean").loc["sepal length (cm)"] == 5.843333


if __name__ == "__main__":
    test_describe_iris()
