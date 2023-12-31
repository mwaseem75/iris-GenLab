from dataclasses import dataclass, field
from dataclasses_json import LetterCase, dataclass_json, config

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PostClass:
    title: str
    selftext : str   
    
   