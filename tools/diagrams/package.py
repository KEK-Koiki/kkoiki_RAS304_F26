"""Package the published diagram exports without modifying the website pages."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[2]
folder=root/'docs/01-Block-Diagram'
with zipfile.ZipFile(folder/'encoder-block-diagram-source.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for name in ['encoder-block-diagram.svg','encoder-block-diagram.png','encoder-detailed-block-diagram.svg','encoder-detailed-block-diagram.png']:
        archive.write(folder/name,name)
print('Updated diagram source ZIP.')
