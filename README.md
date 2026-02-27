# ClearerVoice Studio

Speech separation and enhancement using MossFormer2.

## Setup

```bash
git clone https://github.com/hoanganh0106/Mossformer2.git
cd ClearerVoice-Studio-main
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Download Model Checkpoints

Model weights are not included in this repository due to file size.

Download the model from Google Drive: [model.ckpt-61-221600.pt](https://drive.google.com/file/d/1NfZyzGUQX7g8TMXvO0J6XCmBe098Eu1q/view?usp=sharing)

After downloading, place the file at:

```
ClearerVoice-Studio-main/clearvoice/checkpoints/MossFormer2_SS_16K/model.ckpt-61-221600.pt
```

Original source: [ClearerVoice-Studio on GitHub](https://github.com/modelscope/ClearerVoice-Studio)

## Usage

###Tách giọng nói từ file audio có sẵn

```bash
cd ClearerVoice-Studio-main/clearvoice
# Dùng file mặc định (samples/mix.wav)
python separate_3spk.py

# Hoặc chỉ định file input và thư mục output
python separate_3spk.py <input_file.wav> <output_dir>
# Ví dụ:
python separate_3spk.py samples/mix.wav samples/output
```

Kết quả sẽ được lưu vào thư mục output dưới dạng các file `output_s1.wav`, `output_s2.wav`, `output_s3.wav` tương ứng với 3 nguồn âm được tách.
