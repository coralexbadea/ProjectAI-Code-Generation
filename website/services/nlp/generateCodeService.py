from pickle import load
from numpy.lib.function_base import delete
from .models.generate_code_model import LoadModel
import gc 

class GenerateCodeService():
   def __init__(self) -> None:
      pass

   def generateCode(self, src):
      loadModel = LoadModel()
      loadModel.createModel()
      result = loadModel.eng_to_python(src)
      del loadModel
      gc.collect()
      return result

