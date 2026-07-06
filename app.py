import streamlit as st

from agent import select_agent

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#2E86DE;
}

.agent-box{
    background:#f5f5f5;
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
}

.user-box{
    background:#DCF8C6;
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
}

.bot-box{
    background:#F2F2F2;
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.title("🚀 CareerPilot AI")

    st.write("Multi-Agent Career Guidance System")

    st.divider()

    st.markdown("""
### Available Agents

✅ Career Advisor

✅ Skills Advisor

✅ Resume Expert

✅ Interview Coach

✅ Roadmap Planner
""")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# -------------------------------------------------
# Title
# -------------------------------------------------

st.markdown(
    '<p class="main-title">CareerPilot AI</p>',
    unsafe_allow_html=True
)

st.write(
    "Ask anything about careers, resumes, interviews, skills, or learning roadmaps."
)

# -------------------------------------------------
# Chat History
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
<div class="user-box">

**🧑 You**

{message["content"]}

</div>
""",
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            f"""
<div class="bot-box">

**🤖 {message["agent"]}**

{message["content"]}

</div>
""",
            unsafe_allow_html=True,
        )

# -------------------------------------------------
# Input
# -------------------------------------------------

query = st.chat_input("Ask your question...")

# -------------------------------------------------
# Response
# -------------------------------------------------

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    agent = select_agent(query)

    agent_name = agent.name.replace("_", " ").title()

    # ============================================
    # Replace this section with your ADK runner.
    # ============================================

    try:
        response = agent.run(query)

        # If your runner returns an object instead of
        # plain text, replace the next line with the
        # appropriate field.
        answer = str(response)

    except Exception as e:

        answer = f"""
Agent selected: {agent_name}

Your routing is working.

Next, connect the Google ADK Runner here.

Error:
{e}
"""

    st.session_state.messages.append(
        {
            "role": "assistant",
            "agent": agent_name,
            "content": answer
        }
    )

    st.rerun()