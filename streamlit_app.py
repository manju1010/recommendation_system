import streamlit as st
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from database.schema import initialize_db

# Initialize DB
initialize_db()

# Set up agents
customer_agent = CustomerAgent()
product_agent = ProductAgent()
recommender_agent = RecommenderAgent(customer_agent, product_agent)

# Streamlit UI
st.title("🛍️ Multi-Agent Product Recommender")

user_id = st.number_input("Enter your User ID", min_value=1, step=1)

if st.button("Recommend Products"):
    recommendations = recommender_agent.get_recommendations(user_id)

    if recommendations:
        st.subheader("🎯 Recommended for You:")
        for pid in recommendations:
            product = product_agent.get_product_info(pid)
            if product:
                st.markdown(f"**{product['name']}** ({product['category']}) - ${product['price']}")
    else:
        st.warning("No recommendations found. Try a different user ID.")
