class RecommenderAgent:
    def __init__(self, customer_agent, product_agent):
        self.customer_agent = customer_agent
        self.product_agent = product_agent

    def get_recommendations(self, user_id):
        user_profile = self.customer_agent.get_profile(user_id)
        history = user_profile.get("history", [])
        # Dummy logic: recommend 2 other product IDs
        recommendations = [pid + 1 for pid in history if pid + 1 <= 200]
        return recommendations
