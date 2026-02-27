"""
Tạo file test: Mix 3 giọng nói + noise
"""
import numpy as np
import soundfile as sf
import librosa
import os
import random

# Paths
base_path = r"d:\Dự án\ClearerVoice-Studio-main\LibriMix\Data_Raw"
test_clean = os.path.join(base_path, "LibriSpeech", "test-clean")
noise_path = os.path.join(base_path, "wham_noise", "tt")
output_path = r"d:\Dự án\ClearerVoice-Studio-main\ClearerVoice-Studio-main\clearvoice\samples"

# Lấy 3 speaker khác nhau từ test-clean
speakers = [d for d in os.listdir(test_clean) if os.path.isdir(os.path.join(test_clean, d))]
random.shuffle(speakers)
selected_speakers = speakers[:3]

print("="*60)
print("TẠO FILE TEST: 3 GIỌNG + NOISE")
print("="*60)

# Lấy 1 file audio từ mỗi speaker
audio_files = []
for spk in selected_speakers:
    spk_path = os.path.join(test_clean, spk)
    # Tìm file flac trong tất cả subfolders
    found = False
    for root, dirs, files in os.walk(spk_path):
        for f in files:
            if f.endswith('.flac'):
                audio_files.append(os.path.join(root, f))
                found = True
                break
        if found:
            break

print(f"\n3 Speakers được chọn: {selected_speakers}")
print(f"Số file tìm được: {len(audio_files)}")

# Lấy 1 file noise
noise_files = [f for f in os.listdir(noise_path) if f.endswith('.wav')]
noise_file = os.path.join(noise_path, random.choice(noise_files))
print(f"Noise file: {os.path.basename(noise_file)}")

# Đọc audio
target_sr = 16000
audios = []

for i, f in enumerate(audio_files):
    audio, sr = librosa.load(f, sr=target_sr)
    audios.append(audio)
    print(f"  Speaker {i+1}: {os.path.basename(f)} ({len(audio)/target_sr:.2f}s)")

# Đọc noise
noise, sr = librosa.load(noise_file, sr=target_sr)
print(f"  Noise: ({len(noise)/target_sr:.2f}s)")

# Cắt về cùng độ dài
min_len = min(len(a) for a in audios)
min_len = min(min_len, len(noise))
min_len = min(min_len, 5 * target_sr)  # Max 5 giây

audios = [a[:min_len] for a in audios]
noise = noise[:min_len]

# Normalize
audios = [a / (np.abs(a).max() + 1e-8) for a in audios]
noise = noise / (np.abs(noise).max() + 1e-8)

# Mix với các SNR khác nhau
snr_speech = [0, -2, -4]  # dB cho mỗi speaker
snr_noise = -10  # dB cho noise

mixture = np.zeros(min_len)
for i, a in enumerate(audios):
    scale = 10 ** (snr_speech[i] / 20)
    mixture += a * scale

# Thêm noise
noise_scale = 10 ** (snr_noise / 20)
mixture += noise * noise_scale

# Normalize output
mixture = mixture / (np.abs(mixture).max() + 1e-8) * 0.9

# Lưu file
output_file = os.path.join(output_path, "test_3spk_noisy.wav")
sf.write(output_file, mixture, target_sr)

print(f"\n✓ Đã tạo: {output_file}")
print(f"  Độ dài: {len(mixture)/target_sr:.2f}s")
print(f"  Sample rate: {target_sr} Hz")

# Lưu ground truth cho đánh giá
gt_path = os.path.join(output_path, "ground_truth")
os.makedirs(gt_path, exist_ok=True)

for i, a in enumerate(audios):
    gt_file = os.path.join(gt_path, f"speaker_{i+1}.wav")
    sf.write(gt_file, a, target_sr)
    print(f"  Ground truth: {gt_file}")

print("\n" + "="*60)
print("Bây giờ test model:")
print(f"  python separate_3spk.py samples/test_3spk_noisy.wav samples/test_output")
print("="*60)
