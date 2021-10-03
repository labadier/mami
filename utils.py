import pandas, numpy as np, os
from matplotlib import pyplot as plt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_data(path, labeled = True):

  if labeled == True:
    df = pandas.read_csv(os.path.join(path, 'trial.csv'), sep='\t', usecols=['file_name', 'misogynous', 'Text Transcription']).to_numpy()
  else: df = pandas.read_csv(os.path.join(path, 'trial.csv'), sep='\t', usecols=['file_name', 'Text Transcription']).to_numpy()
  
  labels = []
  text = []
  images = []

  for i in range(len(df[:,0])):
    pic = os.path.join(path, df[:,0][i])
    
    if os.path.exists(pic):
      images.append(pic)
      text.append(df[:,2][i])
      if labeled == True:
        labels.append(df[:,1][i])
  
  if labeled == True:
    return np.array(images), np.array(text), np.array(labels)
  return np.array(images), np.array(text)


def plot_training(history, model, measure='loss'):
    
    plotdev = 'dev_' + measure

    plt.plot(history[measure])
    plt.plot(history['dev_' + measure])
    plt.legend(['train', 'dev'], loc='upper left')
    plt.ylabel(measure)
    plt.xlabel('Epoch')
    if measure == 'loss':
        x = np.argmin(history['dev_loss'])
    else: x = np.argmax(history['dev_acc'])

    plt.plot(x,history['dev_' + measure][x], marker="o", color="red")

    if os.path.exists('./logs') == False:
        os.system('mkdir logs')

    plt.savefig(f'./logs/train_history_{model}.png')