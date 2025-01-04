import streamlit as st

import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.extraction import ResultsExtractor
from tinytroupe.examples import *

from tiny_people import (
    create_psychiatrist,
    create_ayurvedic_specialist,
    create_psychologist,
    create_taichi_specialist,
)


@st.cache_resource
def create_tiny_world(use_traditional_methods: bool = True) -> TinyWorld:
    """Create a tiny world with all the agents."""
    if use_traditional_methods:
        agents = [
            create_psychologist(),
            create_ayurvedic_specialist(),
            create_taichi_specialist(),
            create_psychiatrist(),
        ]
    else:
        agents = [create_psychiatrist(), create_psychologist()]

    world = TinyWorld("Mental Wellness and Mindfulness Group", agents)

    return world


def get_tinyworld_intro_response(tiny_world: TinyWorld) -> TinyWorld:
    """
    Get the intro response from the tiny world.
    
    This function sends a message to the tiny world, which is then broadcasted to all agents.
    It also returns the world with the intro response.
    """
    intro_message = (
        "Hello everyone! All of you are stalwarts and experts in your respective fields. "
        "You all know each other and are very close professionally. "
        "Your main task is to brainstorm and discuss about the user and the problems the user faces, "
        "and finally come up with a solution and/or an action plan. "
        "Your main aim is to increase Mindfulness and improve Mental Wellbeing. "
        "Also, 'Psychiatrist' would act as the main interface and would manage all conversation flow between each and everyone. "
        "'Psychiatrist' would also act as only direct interface with user."
    )
    tiny_world.broadcast(intro_message)

    return tiny_world


def run_tinyworld_with_prompt(tiny_world: TinyWorld, user_prompt: str):
    """
    Run the tiny world with a prompt.

    This function sends a message to the tiny world, which is then broadcasted to all agents.
    It also returns the world with the response.
    """
    tiny_world.broadcast(user_prompt)

    tinyworld_responses = tiny_world.run(1, return_actions=True)

    return tiny_world, tinyworld_responses

def consolidate_tinyworld_ideas(world: TinyWorld) -> dict:
    """Consolidate the latest ideas from each agent in the world."""
    agent_prompt = (
        "Divide your response into 2 parts/sections. \
        In the first part/section-  consolidate the latest ideas from you and  also your perspective of the latest conversation in the group and explain to the user \
        Let the user know who suggested the idea and why. \
        In the second part/section- give concrete points and suggestions to the user\
        Have a clear seperation for the above two sections. \
        Summarize the the ideas to the user that the group came up with, explaining each idea as an item of a list. \
        Note that you should only focus on the latest conversation in the group based on latest input. \
        Provide a lot of details on each idea, and complement anything missing. \
        Always format your responses in Markdown format "
    )
    agent_responses = {}
    for agent in world.agents:
        agent_name = agent.name
        rapporteur = world.get_agent_by_name(agent_name)
        rapporteur_response = rapporteur.listen_and_act(agent_prompt, return_actions=True)
        agent_responses[agent_name] = rapporteur_response
    return agent_responses


def extract_results_from_tinyworld(world: TinyWorld, rapporteur: TinyPerson) -> dict:
    """
    Extracts the results from the tiny world.

    Args:
        world (TinyWorld): The tiny world to extract results from.
        rapporteur (TinyPerson): The rapporteur agent in the world.

    Returns:
        dict: A dictionary with the extracted results.
    """
    extractor = ResultsExtractor()

    extraction_objective = (
        "Consolidates the ideas that the group came up with, explaining each idea as an item of a list. "
        "Add all relevant details, including key benefits and drawbacks, if any. "
        "Finally format everything neatly into a Markdown format"
    )
    situation = "A focus group to promote Mindfulness and improve Mental Wellbeing"

    results = extractor.extract_results_from_agent(
        rapporteur, extraction_objective, situation
    )

    return results
