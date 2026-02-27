# ClearerVoice Studio

Speech separation and enhancement using MossFormer2.

## Setup

```bash
git clone <your-repo-url>
cd ClearerVoice-Studio-main
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Download Model Checkpoints

Model weights are not included in this repository due to file size.

Download manually from the original release and place them at:

```
ClearerVoice-Studio-main/clearvoice/checkpoints/MossFormer2_SS_16K/model.ckpt-61-221600.pt
```

Original source: [ClearerVoice-Studio on GitHub](https://github.com/modelscope/ClearerVoice-Studio)

## Usage

```bash
cd ClearerVoice-Studio-main
python clearvoice/separate_3spk.py
```
