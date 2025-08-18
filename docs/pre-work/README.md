---
title: Docling Workshop Pre-work
description: Preparation for the Docling Workshop
logo: images/DoclingDuck.png
---

# Pre-work

The labs in the workshop are [Jupyter notebooks](https://jupyter.org/). The notebooks can be run on your computer or remotely on the [Google Colab](https://colab.research.google.com) service. Check out [Running the Docling Notebooks](#running-the-docling-notebooks) section on how to setup the way you want to run the notebooks.

## Running the Docling Notebooks

The notebooks can be run:

- [Locally on your computer](#running-the-docling-notebooks-locally) OR
- [Remotely on the Google Colab service](#running-the-docling-notebooks-remotely-colab)

Follow the instructions in one of the sections that follow on how you would like to run the notebooks.

## Running the Docling Notebooks Locally

It is recommended if you want to run the lab notebooks locally on your computer that you have:

- A computer or laptop
- Knowledge of [Git](https://git-scm.com/) and [Python](https://www.python.org/)

If not, then it recommended to go to the [Running the Docling Notebooks Remotely (Colab)](#running-the-docling-notebooks-remotely-colab) section instead.

Running the lab notebooks locally on your computer requires the following steps:

- [Local Prerequisites](#local-prerequisites)
- [Clone the Docling Workshop Repository](#clone-the-docling-workshop-repository)
- [Install Jupyter](#install-jupyter)

### Local Prerequisites

- Git
- Python 3.10, 3.11, or 3.12

### Clone the Docling Workshop Repository

Clone the workshop repo and cd into the repo directory.

```shell
git clone https://github.com/IBM/docling-workshop.git
cd docling-workshop
```

[Lab 3: Multimodal RAG with Visual Grounding using Docling](../lab-3/README.md) requires Replicate.

#### Replicate AI Cloud Platform

[Replicate](https://replicate.com/) is a cloud platform that will host and serve AI models for you.

1. Create a [Replicate](https://replicate.com/) account. You will need a [GitHub](https://github.com/) account to do this.

1. Add credit to your Replicate Account (optional). To remove a barrier to entry to try the models on the Replicate platform, use [this link](https://replicate.com/invites/a8717bfe-2f3d-4a52-88ed-1356231cdf03) to add a small amount of credit to your Replicate account.

1. Create a Replicate [API Token](https://replicate.com/account/api-tokens).

1. Set your Replicate API Token as an environment variable in your terminal where you will run the notebook:

    ```shell
    export REPLICATE_API_TOKEN=<your_replicate_api_token>
    ```

### Install Jupyter

!!! note "Use a virtual environment"
    Before installing dependencies and to avoid conflicts in your environment, it is advisable to use a [virtual environment (venv)](https://docs.python.org/3/library/venv.html).

1. Create virtual environment:

    ```shell
    python3 -m venv --upgrade-deps --clear venv
    ```

1. Activate the virtual environment by running:

    ```shell
    source venv/bin/activate
    ```

1. Install Jupyter notebook in the virtual environment:

    ```shell
    python3 -m pip install --require-virtualenv notebook ipywidgets
    ```

    For more information, see the [Jupyter installation instructions](https://jupyter.org/install)

1. To open a notebook in Jupyter (in the active virtual environment), run:

    ```shell
    jupyter notebook <notebook-file-path>
    ```

## Running the Docling Notebooks Remotely (Colab)

Running the lab notebooks remotely using [Google Colab](https://colab.research.google.com) requires the following steps:

- [Colab Prerequisites](#colab-prerequisites)
- [Serving the Granite AI Models for Colab](#serving-the-granite-ai-models-for-colab)

!!! note "Notebook execution speed tip" The default execution runtime in Colab uses a CPU. Consider using a different Colab runtime to increase execution speed, especially in situations where you may have other constraints such as a slow network connection. From the navigation bar, select `Runtime->Change runtime type`, then select either GPU- or TPU-based hardware acceleration.

### Colab Prerequisites

- [Google Colab](https://colab.research.google.com) requires a Google account that you're logged into

### Serving the Granite AI Models for Colab

The labs require Granite models to be served by an AI model runtime so that the models can be invoked or called.

#### Replicate AI Cloud Platform for Colab

[Replicate](https://replicate.com/) is a cloud platform that will host and serve AI models for you.

1. Create a [Replicate](https://replicate.com/) account. You will need a [GitHub](https://github.com/) account to do this.

1. Add credit to your Replicate Account (optional). To remove a barrier to entry to try the Granite models on the Replicate platform, use [this link](https://replicate.com/invites/a8717bfe-2f3d-4a52-88ed-1356231cdf03) to add a small amount of credit to your Replicate account.

1. Create a Replicate [API Token](https://replicate.com/account/api-tokens).

1. Add your Replicate API Token to the Colab Secrets manager to securely store it. Open [Google Colab](https://colab.research.google.com) and click on the 🔑 Secrets tab in the left panel. Click "New Secret" and enter `REPLICATE_API_TOKEN` as the key, and paste your token into the value field. Toggle the button on the left to allow notebook access to the secret.
