"""
Tách 3 nguồn âm thanh
Cách dùng: python separate_3spk.py <input_file> [output_dir]
"""
from clearvoice import ClearVoice
import os
import sys

# Đường dẫn mặc định
input_file = sys.argv[1] if len(sys.argv) > 1 else "samples/1.wav"
output_dir = sys.argv[2] if len(sys.argv) > 2 else "samples/output"

os.makedirs(output_dir, exist_ok=True)

print(f"Input: {input_file}")
print(f"Output: {output_dir}")

# Tách 3 nguồn âm
myClearVoice = ClearVoice(task='speech_separation', model_names=['MossFormer2_SS_16K'])
output_wav = myClearVoice(input_path=input_file, online_write=False)
myClearVoice.write(output_wav, output_path=os.path.join(output_dir, "output.wav"))

print("\n✓ Hoàn thành!")
for f in os.listdir(output_dir):
    print(f"  • {output_dir}/{f}")
