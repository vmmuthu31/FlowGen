import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys


def generate_actor_wireframe(actor_components: dict, title: str = "Actor-Based Interfaces: Wireframe"):
    """
    Generate an actor-based wireframe prototype.

    Parameters:
    - actor_components: Dictionary with actors as keys and their components as list values.
    - title: Title of the wireframe plot.

    Returns:
    - A visual representation of the actor-based wireframe.
    """

    fig, ax = plt.subplots(figsize=(15, 10))

    # Draw the main application window
    app_box = patches.Rectangle(
        (0.05, 0.1), 0.9, 0.8, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(app_box)

    num_actors = len(actor_components)
    x_positions = [((i+1) / (num_actors + 1)) for i in range(num_actors)]

    # Draw components for each actor
    for actor, x in zip(actor_components.keys(), x_positions):
        y_start = 0.7
        ax.text(x, 0.85, actor, horizontalalignment='center',
                verticalalignment='center', fontsize=10, weight='bold')
        for comp in actor_components[actor]:
            box = patches.Rectangle((x - 0.09, y_start), 0.18, 0.08, fill=True,
                                    edgecolor='black', facecolor='lightgray', linewidth=1)
            ax.add_patch(box)
            ax.text(x, y_start + 0.04, comp, horizontalalignment='center',
                    verticalalignment='center', fontsize=9)
            y_start -= 0.1

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title(title, size=16)

    plt.tight_layout()
    plt.show()


# Test the module with the previous data
# actor_data = {
#     "Farmers": ["Dashboard", "NFT Management", "Crop Management", "AI Recommendations", "Learning Platform", "Loan Application", "WhatsApp Bot"],
#     "Consumers": ["Product Trace", "Feedback", "Purchase History"],
#     "DAO Members": ["Approve Loans", "Manage Supply Chain", "Support"],
#     "Intermediaries": ["Supply Chain Status", "Inventory", "Transactions", "NFT Verification"],
#     "Admins": ["User Management", "Dispute Resolution", "System Monitoring", "NFT Oversight"]
# }

# generate_actor_wireframe(
#     actor_data, "Updated Actor-Based Interfaces with NFT: Prototype Wireframe")


# if __name__ == "__main__":
#     if len(sys.argv) <= 2 and len(sys.argv) > 0:
#         generate_actor_wireframe(sys.argv[1], sys.argv[2])
#     else:
#         print("No arguments provided.")
