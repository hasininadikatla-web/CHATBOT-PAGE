
import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 MY AI CHATBOT")
st.caption("Powered by Ollama + Streamlit")

# Create message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
prompt = st.chat_input("Type your message...")

if prompt:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(answer)
