import os
import subprocess
from lightning.app import LightningWork

class LabelStudio(LightningWork):
    def __init__(self, ls_host: str='0.0.0.0', ls_port: int=8888):
        super().__init__()
        # self.ls_host = ls_host
        # self.ls_port = ls_port


    def start_server(self):
        server_start_command = ["label-studio", "start", f"--host={self.host}", f"--port={self.port}"]
        try:
            subprocess.run(server_start_command)
        except Exception as e:
            print(e)

    def run(self):
        self.start_server()