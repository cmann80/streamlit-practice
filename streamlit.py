
# code from blog.stremlit.io/ai-talks-chatgpt-assistant-via_streamlit

# library for user interface elements
from openai import InvalidRequestError
import streamlit as st

# library for streamlit messages
from streamlit_chat import message

# library for openAI interface
from langchain.chat_models import ChatOpenAI

# library for something to do with type?
from typing import List

# libraries for text to speech
from io import BytesIO
from gtts import gTTS, gTTSError

# library for Streamlit option menu
from streamlit_option_menu import option_menu

# helper function to clear the chat
def clear_chat() -> None:
    st.session_state.generated = []
    st.session_state.past = []
    st.session_state.messages = []
    st.session_state.user_text = ""
 
# helper function to show text input
def show_text_input() -> None:
    st.text_area(label=st.session_state.chat_placeholder, value = st.session_state.user_text, key = "user_text")
    
# helper function to render buttons
def show_chat_buttons() -> None:
    b0, b1, b2 = st.columns(3)
    with b0, b1, b2:
        b0.button(label=st.session_state.locale_chat_run_btn)
        b1.button(label=st.session_state.locale.chat_clear_btm, on_click=clear_chat)
        b2.download_button(
            label = st.session_state.locale.chat_save_btn,
            data = "\\n".join([str(d) for d in st.session_state.messages[1:]]),
            file_name="ai-talks-chat.json",
            mime="application/json",
        )

# function to take two inputs, ai_model and messages, and send to API
def create_gpt_completion(ai_model: str, messages: List[dict]) -> dict:
    completion = ChatOpenAI(temperature=0)._create_chat_result(
        model = ai_model,
        messages = messages,
    )
    return completion

# function to display the conversation
def show_chat(ai_content: str, user_text: str) -> None:
    if ai_content not in st.session_state.generated:
        # stores the AI content
        st.session_state.past.append(user_text)
        st.session_state.generated.append(ai_content)
    if  st.session_state.generated:
            for i in range(len(st.session_state.generated)):
                message(st.session_state.past[i], is_user= True, key = str(i) + "_user", avatar_style="micah")
                message("", key=str(i))
                st.markdown(st.session_state.generated[i])
                
# function that controls the flow of the AI response
def show_gpt_conversation() -> None:
    try:
        completion = create_gpt_completion(st.session_state_model, st.session_state_messages)
        ai_content = completion.get("choices")[0].get("message").get("content")
        st.sesson_state.messages.append({"role": "assistant", "content": ai_content})
        if ai_content:
            show_chat(ai_content, st.session_state.user_text)
            st.divider()
            show_audio_player(ai_content)
    except InvalidRequestError as err:
        if err.code == "context_length_exceeded":
            st.session_state.messages.pop(1)
            if len(st.session_state.messages) == 1:
                st.session_state.user_text = ""
            show_conversation()
        else:
            st.error(err)
    # Here I left out the OpenAI error, need to replace it with something but what?
    except(UnboundLocalError) as err:
        st.error(err)

# function to update the message list
def show_conversation() -> None:
    if st.session_state.messages:
        st.session_state.messages.append({"role": "user", "content": st.session_state.user_text})
    else: 
        ai_role = f"{st.session_state.locale.ai_role_prefix} {st.session_state.role}. {st.session_state.locale.ai_role_postfix}" #NOQA: E501
        st.session_state.messages = [
            {"role": "system", "content": ai_role},
            {"role": "user", "content": st.session_state.user_text}
        ]
    show_gpt_conversation()
    
# function for text to speech
def show_audio_player(ai_content: str) -> None:
    sound_file = BytesIO()
    try:
        tts = gTTS(text=ai_content, lang=st.session_state.locale.lang_code)
        tts.write_to_fp(sound_file)
        st.write(st.session_state.locale.stt_placeholder)
        st.audio(sound_file)
    except gTTSError as err:
        st.error(err)


# streamlit main application

# general settings
PAGE_TITLE: str = "AI Talks with Langchain"
PAGE_ICON: str = "🤖"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# left out language options for now

# storing content
#left language out here too
if "generated" not in st.session_state:
    st.session_state.generated = []
if "past" not in st.session_state:
    st.session_state.past =[]
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_text" not in st.session_state:
    st.session_state.user_text = ""
    
# main function
def main() -> None:
    
    if st.session_state.user_text:
       show_conversation()
       st.session_state.user_text = ""
    show_text_input()
    show_chat_buttons()
    
    
            
    