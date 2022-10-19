# from LAI_label_studio import ComponentA, ComponentB
from LAI_label_studio.components.label_studio_server import LabelStudio
import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.data_annotator = LabelStudio()
        

    def run(self):
        self.data_annotator.run()
    
    # def configure_layout(self):
    #     # wait for work to complete so that manual refresh is not required
    #     tab_1 = {'name': 'Data report', 'content': self.data_annotator}

app = L.LightningApp(LitApp())
