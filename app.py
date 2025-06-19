import streamlit as st
from multi_tool_agent.agent import product_strategy_agent  # adjust if needed

st.set_page_config(page_title="AI Product Strategy Assistant")

st.title("🤖 Product Strategy Launch Assistant")
st.markdown("Enter your product idea to generate market insights, PRDs, and marketing content.")

product_name = st.text_input("Product Name")
product_description = st.text_area("Product Description", height=150)
target_user = st.text_input("Target User (optional)")
initial_features = st.text_area("Initial Features (comma-separated, optional)")

if st.button("Generate Strategy"):
    with st.spinner("Running multi-agent system..."):
        response = product_strategy_agent.run({
            "product_name": product_name,
            "product_description": product_description,
            "target_user": target_user,
            "initial_features": [f.strip() for f in initial_features.split(",") if f.strip()]
        })
        st.success("🎉 horay Strategy Generated!")
        st.json(response)
