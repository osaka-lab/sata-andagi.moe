from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional, Union, List, Dict

import toml
import random
import subprocess
from pathlib import Path
from .osaka import Osaka
from .constant import GIT_PATH

class Azumanga:
    """A class for interfacing with the Azumanga TOML Files."""
    def __init__(self) -> None:
        self._repo_path = Path(GIT_PATH)

        self.__update_repo()
        self.osakas, self.categories = self.__phrase_osakas()
    
    def get_random(self, categorie: str = None) -> Osaka:
        if categorie is not None:
            if categorie in self.categories:
                return random.choice(self.categories[categorie])
        
        return random.choice(self.osakas)
    
    def get(self, id: str) -> Optional[Osaka]:
        for osaka in self.osakas:
            if osaka.id == id:
                return osaka
        
        return None
            
    def __update_repo(self):
        print(
            f"Pulling azumanga repo '{self._repo_path}'..."
        )

        process = subprocess.Popen(
            ["git", "pull"], 
            text = True, 
            stdout = subprocess.PIPE, 
            cwd = self._repo_path
        )

        process.wait()
        output, _ = process.communicate()

        if not process.returncode == 0:
            print("Git Error")

        print(f"Git Output: {output}")

    def __phrase_osakas(self) -> Union[List[Osaka], Dict[str, Osaka]]:
        osakas = []
        categories = {}

        for toml_file in self._repo_path.glob("**/*.toml"):
            _toml = toml.loads(
                toml_file.read_text()
            ).get("metadata", {})           

            category = _toml.get("category")
            
            osaka = Osaka(
                id = _toml.get("id"),
                title = _toml.get("title"),
                url = _toml.get("url"),
                category = category,
                source = _toml.get("source")
            )

            osakas.append(osaka)

            if isinstance(category, list):
                for cate in category:
                    if cate not in categories:
                        categories[cate] = []
            
                    categories[cate].append(osaka)
            else:
                if category not in categories:
                    categories[category] = []
        
                categories[category].append(osaka)
        
        return osakas, categories