import torch

print(f"Current device index: {torch.cuda.current_device()}")
print(f"Is it CUDA? {torch.cuda.is_available()}")
print(f"Cuda device address: {torch.cuda.device(0)}")
print(f"Cuda device count: {torch.cuda.device_count()}")
print(f"Cuda device name: {torch.cuda.get_device_name(0)}")

