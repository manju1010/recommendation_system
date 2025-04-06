from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from database.schema import initialize_db

initialize_db()

customer_agent = CustomerAgent()
product_agent = ProductAgent()
recommender_agent = RecommenderAgent(customer_agent, product_agent)

user_id = 1
print(f"Recommendations for User {user_id}:")
recommendations = recommender_agent.get_recommendations(user_id)

for pid in recommendations:
    info = product_agent.get_product_info(pid)
    print(f"- {info['name']} ({info['category']})")
