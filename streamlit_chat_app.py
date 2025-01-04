####
# Copyright (c) 2024 Sharath M S
####


import os
import streamlit as st 
from st_bg_image import set_background

st.set_page_config(
    page_title="Mental Wellness Assistant",
    layout="centered",
    menu_items={
        "Get help": "https://github.com/sharath-sms/Mental-Wellness-TinyTroupe/issues",
        "Report a Bug": "https://github.com/sharath-sms/Mental-Wellness-TinyTroupe/issues",
        "About": """Agentic Mental Wellness Assistant 

https://github.com/sharath-sms/Mental-Wellness-TinyTroupe

Copyright (c) 2024 Sharath M S

""",
    },
)


set_background('./assets/st_bg_img.png')
st.title("Mental Wellness Assistant")

with st.expander("Disclaimer"):
    st.info(" This is not a clinical advice! Users are urged to consult a qualified healthcare professional for personalized advice.",
        icon="⚠️")


####### API Key
api_key = st.sidebar.text_input("OpenAPI Key", type="password")
if not api_key:
    st.info("Please add your OpenAI API key (in the sidebar) to continue.", icon="🗝️")
else:
    os.environ["OPENAI_API_KEY"] = api_key  # Set the API key as an environment variable
#################


def main():
    if api_key:
        import tinytroupe
        from tiny_people import create_therapist
        from tiny_world import create_tiny_world, get_tinyworld_intro_response, run_tinyworld_with_prompt, consolidate_tinyworld_ideas

        col1, col2, col3 = st.columns(3)

        with col1:
            user_name = st.text_input("Hi! Please enter your name")

        with col2:
            user_age = st.number_input("What is your age?", min_value=0, max_value=100)

        with col3:
            user_nationality = st.text_input("What is your nationality")

    
        help_option = st.radio(f"Hello {user_name}! How do you want to proceed?", ["Chat with a virtual therapist", "Seek advice from a group of virtual agents"],
                               captions=["You can interact with a virtual therapist agent", "You can interact with a group of virtual agents, who also brainstorm within themselsves in a virtual world to help you."])

        if help_option == "Chat with a virtual therapist" and user_name and user_age and user_nationality:
            therapist_agent = create_therapist(nationality=user_nationality)

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if user_input := st.chat_input(f"Hi {user_name}! Chat here ..."):
                st.chat_message("user").markdown(user_input)
                st.session_state.messages.append({"role": "user", "content": user_input})

                therapist_responses = therapist_agent.listen_and_act(user_input, return_actions=True)
                response_content = [action['action']["content"] for action in therapist_responses if action['action']['type'] == 'TALK'][-1]

                with st.chat_message("assistant"):
                    st.markdown(response_content)

                st.session_state.messages.append({"role": "assistant", "content": response_content})

        elif help_option == "Seek advice from a group of virtual agents" and user_name and user_age and user_nationality:
            traditional_methods = st.radio("Do you want to include expert agents who specialize in traditional methods?", ("Yes", "No"),
                                           captions=["This would include Psychologist, Ayurvedic Expert, Tai Chi Expert, and Psychiatrist as agents", "This would only include Psychologist, Psychiatrist as agents"])
            use_traditional_methods = traditional_methods == "Yes"

            world = create_tiny_world(use_traditional_methods=use_traditional_methods)
            world = get_tinyworld_intro_response(world)

            if "tinyworld_messages" not in st.session_state:
                st.session_state.tinyworld_messages = []

            for message in st.session_state.tinyworld_messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if user_prompt := st.chat_input(f"Hi {user_name}! Chat here ... Be as descriptive as possible"):
                st.chat_message("user").markdown(user_prompt)
                st.session_state.tinyworld_messages.append({"role": "user", "content": user_prompt})

                world, responses = run_tinyworld_with_prompt(world, user_prompt=user_prompt)
                agent_responses = consolidate_tinyworld_ideas(world=world)

                for agent in world.agents:
                    agent_name = agent.name
                    response = agent_responses[agent_name]
                    response_content = [action['action']["content"] for action in response if action['action']['type'] == 'TALK'][-1]

                    with st.chat_message(agent_name):
                        st.markdown(f"### {agent_name}'s Response")
                        st.markdown(response_content)

                    st.session_state.tinyworld_messages.append({"role": agent_name, "content": response_content})

    else:
        st.info("Hello! Waiting for your inputs")



if __name__ == "__main__":
    main()