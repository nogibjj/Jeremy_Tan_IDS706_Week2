# IDS706-python-template [![CI](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week2/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week2/actions/workflows/ci.yml)
This repo contains work for mini-project 2. It sets up an environment on codespaces and uses Github Actions to run a Makefile for the following: `make install`, `make test`, `make format`, `make lint`. It loads the iris dataset and runs a simple function to generate descriptive statistics on the dataset. I've also included a general describe function that uses a csv link as an argument. 

Some important stuff included are:

* `Makefile`

* `Dockerfile`

* A base set of libraries for devops and web

* `githubactions` 

## Purpose of project
The purpose of this project is to extend from the previous project (making a python template) and generate descriptive statistics on datasets using Pandas. I made two functions in main.py: "describe_iris(summary)" and "general_describe(csv)". The former function provides descriptive statistics on only the iris dataset while the latter dataset provides descriptive statistics on any csv file a user passes in. I test both functions in test_main with "test_describe_iris_and_general_describe()" 

## Preparation
1. open codespaces 
2. wait for container to be built with requiremnts.txt installed

## Check format and test errors
1. Format code `make format`
2. Lint code `make lint`

<img width="1353" alt="Screenshot 2023-09-07 at 7 14 03 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week2/assets/36715338/13e9d5b3-aa92-47df-a6cc-cf5af68ece28">

3. Test code `make test`

<img width="751" alt="Screenshot 2023-09-07 at 7 14 10 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week2/assets/36715338/8343c2f7-b005-4103-a468-9f917b91eeba">

