# lib import
import math
import os
import re
import mne
import pandas as pd
from mne.time_frequency import psd_multitaper
import numpy as np
import useful_notations
from spikes_events import create_events
from classification import predict_perceptron, predict_svm

class EegPower:
    def __init__(self, path_to_files):
        powers, epochs = [], []
        files = [f for f in sorted(os.listdir(path_to_files))]
        for ind, path in enumerate(files):
            raw = self._read_raw_with_annotations(path_to_files + '/{0}'.format(path))
            del raw
            events = create_events(raw)
            epoch = self._create_epochs(raw, events)
            del events
            epochs.append(epoch)
            power = self._create_evoked(epoch)
            powers.append(power)
        self.powers = powers
        self.epochs = epochs
        del powers, epochs

    @staticmethod
    def _read_raw_with_annotations(path):
        raw = mne.io.read_raw_eeglab(path, preload=True)
        return raw
    @staticmethod
    def _create_epochs(raw, events):
        epoch = mne.Epochs(raw, events = events, event_id = useful_notations.event_dict , tmin=-0.05, tmax=0.05,
                           baseline=(None, 0), preload=True)
        return epoch
    @staticmethod
    def _create_evoked(epochs):
            bands = useful_notations.bands
            psds, freqs  = psd_multitaper(epochs)
            psds /= np.sum(psds, axis=-1, keepdims=True)
            X = []
            for fmin, fmax in bands.values():
                psds_band = psds[:, :, (freqs >= fmin) & (freqs < fmax)].mean(axis=-1)
                X.append(psds_band.reshape(len(psds), -1))
            return np.concatenate(X, axis=1)
    def classification(self):
        result = Results(self.powers)
        return result
    def save_powers(self, path_to_folder):


class Results:
      def __init__(self, powers):
           self.perceptron = predict_perceptron(powers)
           self.svm = predict_svm(powers)


