from app.classes.container import Container
from app.classes.person import Person
from app.functions.randomizers import random_weight
from app.shared_constants import LOSE, PERSON_LIM, SRC_FOLDER
from librosa import load


WEIGHT_INTERVAL = (90, 130)
AUDIO_PATH = f'{SRC_FOLDER}/assets/audio/playlist.mp3'
WAVEFORMS, _ = load(AUDIO_PATH, sr=None)

mini_world: list[Container] = []
waveform_increment = (len(WAVEFORMS) - 1) // PERSON_LIM
waveform_idx = -1

for i in range(1, (PERSON_LIM + 1)):
    fst_weight = random_weight(WEIGHT_INTERVAL)
    person = Person(i, LOSE, fst_weight)

    waveform_split = WAVEFORMS[(waveform_idx + 1):(waveform_idx + waveform_increment)]
    waveform_idx += waveform_increment

    container = Container(person, waveform_split)
    container.toggle_thread()

    mini_world.append(container)
