import numpy as np
import matplotlib.pyplot as plt
import argparse
import librosa
import soundfile as sf
import os.path


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Perform pitch estimation for given sensor data file.')

    parser.add_argument(dest='input', type=str, default=None, nargs='+')

    args = parser.parse_args()

    for in_file in args.input:
        audio, rate = sf.read(in_file)

        D = librosa.stft(audio)
        fig, ax = plt.subplots(1, 1, figsize=(10, 4))

        librosa.display.specshow(
            librosa.logamplitude(
                np.abs(D[:300, :])**2,
                ref_power=np.max
            ),
            y_axis='linear', x_axis='time',
            cmap='Greys'
        )

        plt.xticks([])
        plt.xlabel('')
        plt.yticks([])
        plt.ylabel('')

        plt.tight_layout(w_pad=0, h_pad=0)
        pre, ext = os.path.splitext(in_file)
        plt.savefig(pre + '.png', bbox_inches='tight', dpi=300, pad_inches=0)
