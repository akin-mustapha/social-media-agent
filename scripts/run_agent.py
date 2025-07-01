import sys
import os

# This is a common pattern to make the `src` directory available to the script
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the necessary components from our structured project
from src.agent.core.agent import create_social_media_agent
from src.agent.utils.image_generation import generate_image
from src.agent.adapters.x_adapter import post_to_x

def main():
    """
    Main function to assemble and run the agent.
    """
    print("--- Assembling Social Media Agent ---")

    # Define the list of tools the agent will have access to
    available_tools = [generate_image, post_to_x]

    # Create the agent instance
    social_agent = create_social_media_agent(tools=available_tools)

    # Check if a user prompt was provided via command line
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        # Default prompt for testing if none is provided
        user_input = "Generate a tweet about fight sleep when coding. Make it funny and engaging. Accompany it with anime image style. Make sure to indicate post was made by an AI."

    print(f"\n--- Running Agent with Input ---\n'{user_input}'\n")

    try:
        # Run the agent
        result = social_agent.invoke({"input": user_input})
        print("\n--- Agent Final Output ---")
        print(result.get("output"))
    except Exception as e:
        print(f"An error occurred while running the agent: {e}")

if __name__ == "__main__":
    main()