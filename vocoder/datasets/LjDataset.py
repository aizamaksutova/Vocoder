import time
from tqdm.auto import tqdm
import torchaudio
import os
from pathlib import Path
import torch
import random
from vocoder.melspec import MelSpectrogramConfig, MelSpectrogram


class LjDataset:
    def __init__(self, data_path, wav_max_len=None, limit=None, **kwargs):
        data_path = Path(data_path)
        self.paths = []

        for wav_path in data_path.iterdir():
            self.paths.append(wav_path)

        if limit is not None:
            self.paths = self.paths[:limit]

        mel_spec_config = MelSpectrogramConfig()
        self.mel_spec_transform = MelSpectrogram(mel_spec_config)
        self.wav_max_len = wav_max_len

    def __getitem__(self, index):
        wav_gt, _ = torchaudio.load(self.paths[index])
        if self.wav_max_len is not None:
            start_pos = random.randint(0, wav_gt.shape[-1] - self.wav_max_len)
            wav_gt = wav_gt[..., start_pos: start_pos + self.wav_max_len]
        mel_gt = self.mel_spec_transform(wav_gt.detach()).squeeze(0)
        return {
            "wav_gt": wav_gt,
            "mel_gt": mel_gt
        }

    def __len__(self):
        return len(self.paths)