# Mental-Wellness-TinyTroupe
A chat assistant using TinyTroupe agentic framework

## Table of Contents

* [Introduction](#introduction)
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Interacting with the Streamlit App](#interacting-with-the-streamlit-app)
* [Project Structure](#project-structure)
* [Using the Library](#using-the-library)
* [TinyPerson](#tinyperson)
* [TinyWorld](#tinyworld)
* [Configuring the Library](#configuring-the-library)


## Introduction

Mental-Wellness-TinyTroupe is a chat assistant built using the TinyTroupe agentic framework. It is designed to provide a conversational interface for users to interact with a simulated environment, with the goal of promoting mental wellness and stress relief.

## Getting Started

To get started with Mental-Wellness-TinyTroupe, follow these steps:

1. Clone the repository: `git clone https://github.com/sharath-sms/Mental-Wellness-TinyTroupe.git`
2. Navigate to the `Mental-Wellness-TinyTroupe` directory: `cd Mental-Wellness-TinyTroupe`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Open the `streamlit_chat_app.py` file in a code editor of your choice.
5. Locate the `api_key` variable in the file. This is where you can add your OpenAI API key manually.
6. Run the Streamlit app: `streamlit run streamlit_chat_app.py`

## Interacting with the Streamlit App

The Streamlit app provides a conversational interface for users to interact with a simulated environment. Here are the ways to interact with the app:

* **Enter your name**: Enter your name in the "Hi! Please enter your name" field to start the conversation.
* **Choose a conversation type**: Choose whether you want to chat with a virtual therapist or seek advice from a group of virtual agents.
* **Enter your message**: Enter your message in the chat box and click "Send" to send it to the virtual therapist or agents.
* **View responses**: View the responses from the virtual therapist or agents in the chat box.
* **Select expert agents**: If you choose to seek advice from a group of virtual agents, you can select whether you want to include expert agents who specialize in traditional methods or alternative methods.
* **View advice**: View the advice from the virtual agents in the chat box.


## Project Structure

The project is structured as follows:

* `/tinytroupe`: contains the TinyTroupe library
* `/mental-wellness-tinytroupe`: contains the chat assistant code
* `/examples`: contains example usage of the chat assistant
* `/data`: contains data used by the chat assistant
* `/docs`: contains documentation for the project

## Using the Library

To use the TinyTroupe library, you will need to create a `TinyWorld` object and add `TinyPerson` objects to it. You can then use the `listen_and_act` method to simulate conversations between the agents.

## TinyPerson

A `TinyPerson` object represents an agent in the simulated environment. It has a `name` attribute and a `listen_and_act` method that takes a prompt and returns a response.

## TinyWorld

A `TinyWorld` object represents the simulated environment. It has a `name` attribute and a `get_agent_by_name` method that returns a `TinyPerson` object by name.

## Configuring the Library

To configure the library, you will need to set the following environment variables:

* `AZURE_OPENAI_API_KEY`: your Azure OpenAI API key
* `OPENAI_API_KEY`: your OpenAI API key
* `TINYTRUPE_CONFIG`: the path to the `config.ini` file

You can also configure the library by editing the `config.ini` file directly.

