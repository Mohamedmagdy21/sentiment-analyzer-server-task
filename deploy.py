import os

from lightning_sdk.deployment import Deployment

deployment = Deployment(
   name="sentiment-analyzer", 
   teamspace=os.getenv("TEAMSPACE"),
   user=os.getenv("LIGHTNING_USERNAME")
)

print(os.getenv("TEAMSPACE"))
print(os.getenv("IMAGE_NAME"))
print(os.getenv("DOCKERHUB_USERNAME"))
print(os.getenv("GITHUB_SHA_SHORT"))

# Create the initial release 
deployment.start(
   image=f"{os.getenv('DOCKERHUB_USERNAME')}/{os.getenv('IMAGE_NAME')}:{os.getenv('GITHUB_SHA')}", # Ollama Docker image
   ports=[8000],
)