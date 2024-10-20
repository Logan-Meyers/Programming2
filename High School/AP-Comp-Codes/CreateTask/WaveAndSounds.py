import numpy as np
import math
import wavio
from matplotlib import pyplot as plt


MAX_FREQS = {
    "C": 4186,
    "C#": 4435,
    "D": 4699,
    "Eb": 4978,
    "E": 5274,
    "F": 5588,
    "F#": 5920,
    "G": 6272,
    "G#": 6645,
    "A": 7040,
    "Bb": 7459,
    "B": 7902
}
MAX_OCTAVE = 8

def write_file(file_name: str, data_array, sample_rate: int=44100, sample_width: int=2):
    """
    Takes in a file name and list of data, and writes it out to a .wav file for listening or sharing (or decoding)

        Parameters
            file_name (str): a string, holding the name for the file to be written (e.x. "example.wav")
            data_array (np.array): a 1D or 2D np array holding all the data to be written
            sample_rate (int): how many samples per second are there? Default: 44,100
            sample_width (int): size, 1-4, of wav file data. Default: 2 (16 bits)
    """

    wavio.write(file_name, data_array, sample_rate, sampwidth=sample_width)

def sine(hz: float, sample_rate: int, max_time: float, decay: float=0, is_np_array: bool=True):
    """Takes in some parameters and generates an array containing values over time that make up the sound wave
    
        Parameters:
            hz (float): SINGLE frequency of the wave
            sample_rate (int): amount of samples per second the output file will have
            max_time (float): max length of time the note can sound for
            decay (float): how much to scale sound wave by over time
            is_np_array (bool): whether or not to convert to a numpy array
    """

    # function to calculate value at given time
    def calc_val(curr_time):
        t = curr_time * hz # get time scaled by frequency
        t *= (2 * math.pi)/sample_rate  # scale to sample rate

        curr_val = math.sin(t)  # sine value at time
        curr_val *= 1-(decay * curr_time/sample_rate)  # apply decay

        return curr_val  # return value
    
    # define a list to hold values of wave
    wave_values = []

    # calculate and append values for wave for its entire duration
    for time in range(int(max_time * sample_rate)):
        wave_values.append(calc_val(time))
    
    # convert to numpy array if needed and return array
    if is_np_array:
        return np.array(wave_values)
    else:
        return wave_values

def makeSines(hz: float | list[float], sample_rate: int, max_time: float, decay: float=0, is_np_array: bool=True):
    """Takes in some parameters and generates an array containing values over time that make up the sound wave(s)
    
        Parameters:
            hz (float or list): single or multiple frequency(s) of the wave(s)
            sample_rate (int): amount of samples per second the output file will have
            max_time (float): max length of time the note can sound for
            decay (float): how much to scale sound wave by over time
            is_np_array (bool): whether or not to convert to a numpy array
    """

    # if a list of frequencies are given, make multiple and join them together
    if isinstance(hz, list):
        # define an empty list
        entireWave = []
        # go through each frequency
        for frequency in hz:
            # make a sine wave for that frequency
            newWave = sine(frequency, sample_rate, max_time, decay, is_np_array)
            # if the entire list is empty, make entire wave list equal to new list
            if len(entireWave) == 0:
                entireWave = newWave
            # else add the wave's sample together (each list has the same length from time, so no possibility of an IndexError)
            else:
                for sample in range(len(newWave)):
                    entireWave[sample] += newWave[sample]
    # else if a single float is given, make one wave
    elif isinstance(hz, float):
        entireWave = sine(hz, sample_rate, max_time, decay, is_np_array)
    
    # return
    if is_np_array:
        return np.array(entireWave)
    else:
        return entireWave

def rest(sample_rate: int, max_time: float, is_np_array: bool=True):
    wave_values = []

    for _ in range(int(sample_rate * max_time)):
        wave_values.append(0)
    
    # convert to numpy array if needed and return array
    if is_np_array:
        return np.array(wave_values)
    else:
        return wave_values

def scale_to_1(np_array):
    """
    Takes in a numpy array and scales each value down to a max rangeof -1 to 1
    
        Parameters
            np_array: the numpy array to scale
    """

    # define max and min values
    max_val = 0
    min_val = 0

    # for each value in the numpy array, adjust max and min values as needed
    for val in np_array:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    
    # define a new array of the original, but scaled down to 1
    scaled_array = np_array / max(max_val, -min_val)
            
    # return said array
    return scaled_array

def cap_at_1(np_array):
    """
    Takes in a numpy array and caps each value at either -1 or 1
    
        Parameters
            np_array: the numpy array to cap
    """

    # define a new array containing capped values
    capped_array = []

    # for each value in the array, cap at -1 to 1
    for val in np_array:
        if val > 1:
            val = 1
        if val < -1:
            val = -1
        
        # add to array
        capped_array.append(val)
    
    # return a 1D numpy version of that array
    return np.array(capped_array)

def write_song(notes: list[list[str]]):
    for notesCol in notes:
        print(notesCol)

def noteToFrequency(note: str, octave: int, roundAmnt: int=2):
    maxNoteFreq = MAX_FREQS[note]  # get max frequency for note
    noteFreq = maxNoteFreq / (2 ** (MAX_OCTAVE - octave))  # 'scale' down
    noteFreq = round(noteFreq, roundAmnt)  # round
    return noteFreq
