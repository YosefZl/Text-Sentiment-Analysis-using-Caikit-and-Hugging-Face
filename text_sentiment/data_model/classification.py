# Standard
from typing import List
# Local
from caikit.core import DataObjectBase
from caikit.core.data_model import dataobject
@dataobject(package="text_sentiment.data_model")
class ClassInfo(DataObjectBase):
   """A single classification prediction."""
   class_name: str  
   confidence: float  
@dataobject(package="text_sentiment.data_model")
class ClassificationPrediction(DataObjectBase):
   """The result of a classification prediction."""
   classes: List[ClassInfo]
@dataobject(package="text_sentiment.data_model")
class TextInput(DataObjectBase):
   """A sample `domain primitive` input type for this library.
   The analog to a `Raw Document` for the `Natural Language Processing` domain."""
   text: str