import os

from lightning_sdk.deployment import Deployment

deployment = Deployment(
   name="sentiment-analyzer-othertrialll", 
   teamspace=os.getenv("TEAMSPACE"),
   user=os.getenv("LIGHTNING_USER_ID")
   
)


dockerhub_username = os.getenv("DOCKERHUB_USERNAME", "").strip()
image_name = os.getenv("IMAGE_NAME", "").strip()
sha = os.getenv("GITHUB_SHA_SHORT", "").strip()

deployment.start(
    image=f"{dockerhub_username}/{image_name}:{sha}",
    ports=[8000],
)