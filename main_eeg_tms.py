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
from visualization import plot_results, plot_mean_topomaps


# EEG class for epochs and power estimation
class Eeg:
    def __init__(self, path_to_files, path_to_folder):
        powers, epochs = [], []
        files_eeg = [f for f in sorted(os.listdir(path_to_files))]
        files_events = []
        for ind, path in enumerate(files_eeg):
            raw = self._read_raw_with_annotations(path_to_files + '/{0}'.format(path))
            ch_names = raw.ch_names
            events = create_events(raw)
            epoch = self._create_epochs(raw, events)
            epochs.append(epoch)
            power = Power(epoch)
            powers.append(power)
        self.ch_names = ch_names
        self.powers = powers
        self.epochs = epochs
        self.path_for_save = path_to_folder
        del powers, epochs, raw, events, ch_names

    @staticmethod
    def _read_raw_with_annotations(path):
        raw = mne.io.read_raw_eeglab(path, preload=True)
        return raw

    @staticmethod
    def _create_epochs(raw, events):
        epoch = mne.Epochs(raw, events=events, event_id=useful_notations.event_dict, tmin=-0.05, tmax=0.05,
                           baseline=(None, 0), preload=True)
        return epoch

    def classification(self):
        result = Results(self.powers, self.path_for_save)
        return result

    def save_powers(self, path_to_folder):
        pass

    def plot(self, path_to):
        pass


# class fo making plots for results of classification
class Results:
    def __init__(self, powers, path):
        self.perceptron = predict_perceptron(powers)
        self.svm = predict_svm(powers)
        self.path_for_save = path

    def plot(self, save=False):
        plot_results([self.perceptron, self.svm], save)


# class fo key accessing the Powers
class Power:
    def __init__(self, epochs):
        bands = useful_notations.bands
        events_list = useful_notations.event_list_ext
        for _, k in enumerate(events_list):
            psds, freqs = psd_multitaper(epochs[k])
            psds /= np.sum(psds, axis=-1, keepdims=True)
            x = []
            for fmin, fmax in bands.values():
                psds_band = psds[:, :, (freqs >= fmin) & (freqs < fmax)].mean(axis=-1)
                x.append(psds_band.reshape(len(psds), -1))
            np.concatenate(x, axis=1)
            self.__dict__[k] = x

    # create key accessing
    def __getitem__(self, key):
        return self.key
