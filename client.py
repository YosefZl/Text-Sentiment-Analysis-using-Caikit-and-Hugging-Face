# Standard
import os
# Third Party
import grpc
# Local
from caikit.runtime.service_factory import ServicePackageFactory
from text_sentiment.data_model import TextInput
inference_service = ServicePackageFactory().get_service_package(
   ServicePackageFactory.ServiceType.INFERENCE,
)
port = 8085
# Setup the client
channel = grpc.insecure_channel(f"localhost:{port}")
client_stub = inference_service.stub_class(channel)
# Run inference for two sample prompts
for text in ["I am not feeling well today!", "Today is a nice sunny day", "My dog is really cute", "ItzTimmy love playing Apex Legend"]:
   input_text_proto = TextInput(text=text).to_proto()
   request = inference_service.messages.HuggingFaceSentimentTaskRequest(
      text_input=input_text_proto
   )
   response = client_stub.HuggingFaceSentimentTaskPredict(
      request, metadata=[("mm-model-id", "text_sentiment")]
   )
   print("Text:", text)
   print("RESPONSE:", response)