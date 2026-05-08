# SsTeX - Screenshot to LaTeX tool
# Copyright (C) 2026 mmichaellangelo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This file provides a class used for configuring SsTeX.  
It provides methods to load, save, and modify the system's configuration.
"""

import os
import json
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field, PrivateAttr, ConfigDict
from threading import Lock

class SsTeXConfig(BaseModel):
    """ SsTex Program Configuration """
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    config_filepath: Path = Field(default_factory=lambda: SsTeXConfig.get_default_path(), exclude=True)
    api_key: Optional[str] = None
    notify_err: bool = True
    notify_success: bool = True
    _lock: Lock = PrivateAttr(default_factory=lambda: Lock())

    @staticmethod
    def get_default_path():
        """ Get the path to the program's config file """
        # Points to C:\Users\Username\AppData\Roaming\YourAppName
        app_data = os.getenv('APPDATA')
        config_dir = Path(app_data) / 'SsTeX'
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / 'config.json'

    @classmethod
    def load(cls) -> SsTeXConfig:
        """ 
        Factory method for getting SsTeX config
        from the configuration file. 
        Returns a fresh SsTeXConfig instance if 
        config file doesn't exist or can't be read.
        """
        path = cls.get_default_path()
        if path.exists():
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
                    return cls.model_validate(data)
            except:
                return cls()
        
        return cls()

    def save(self):
        """ Saves current configuration to file. """
        with self._lock:
            with open(self.config_filepath, 'w') as f:
                json.dump(self.model_dump(mode='json'), f, indent=4)
