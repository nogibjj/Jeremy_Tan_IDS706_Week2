"""
Test goes here

"""

from main import (
    describe_iris,
    general_describe,
    generate_viz_iris,
    generate_vis_general_congress,
    generate_summary,
    generate_summary_iris,
)
import pandas as pd

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


def test_describe_iris_and_general_describe():
    """Function calling describe_iris and general_describe which tests different parts of the dataset"""

    # for the first assert statement I am calling the mean but the function is returning the medians for all the columns
    # so returns tuple of (median of all columns, .decribe() function)
    assert describe_iris("mean")[0].loc["sepal length (cm)"] == 5.8
    assert describe_iris("mean")[1].loc["petal width (cm)"] == 1.1993333333333336
    assert describe_iris("std")[1].loc["petal width (cm)"] == 0.7622376689603465

    # only works for the example_csv link
    # since the congress dataset has columns that don't contain numeric data, I can't just return .median()
    # so I need to read it here to check
    congress = pd.read_csv(example_csv)
    median_age = congress["age"].median()
    assert median_age == 53.0
    assert general_describe(example_csv).loc["mean", "age"] == 53.31373222430909
    assert general_describe(example_csv).loc["std", "age"] == 10.678469157541091


def test_viz_iris_and_general():
    """Function calling generate_viz_iris() and generate_vis_general_congress"""
    generate_viz_iris()
    generate_vis_general_congress(example_csv)


def test_generate_summary_report():
    """Function calling generate_summary() and generate_summary_iris()"""
    generate_summary(example_csv)
    generate_summary_iris()


if __name__ == "__main__":
    test_describe_iris_and_general_describe()
    # test_viz_iris_and_general()
    # test_generate_summary_report()
