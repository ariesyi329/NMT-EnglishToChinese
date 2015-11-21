import numpy
import os

from nmt import train

def main(job_id, params):
    print params
    validerr = train(saveto=params['model'][0],
                                        reload_=params['reload'][0],
                                        dim_word=params['dim_word'][0],
                                        dim=params['dim'][0],
                                        n_words=params['n-words'][0],
                                        n_words_src=params['n-words'][0],
                                        decay_c=params['decay-c'][0],
                                        clip_c=params['clip-c'][0],
                                        lrate=params['learning-rate'][0],
                                        optimizer=params['optimizer'][0], 
                                        maxlen=50,
                                        batch_size=32,
                                        valid_batch_size=32,
					datasets=['../../../data/zh/no_seg/ted.zh.no_seg.train', 
					          '../../../data/en/ted.en.train'],
					valid_datasets=['../../../data/zh/no_seg/ted.zh.no_seg.dev', 
					                '../../../data/en/ted.en.dev'],
					dictionaries=['../../../data/zh/no_seg/ted.zh.no_seg.train.pkl', 
					              '../../../data/en/ted.en.train.pkl'],
                                        validFreq=5000,
                                        dispFreq=10,
                                        saveFreq=5000,
                                        sampleFreq=1000,
                                        use_dropout=params['use-dropout'][0])
    return validerr

if __name__ == '__main__':
    main(0, {
        'model': ['../../experiments/attention_nmt_zh-en_seg/model.npz'],
        'dim_word': [512],
        'dim': [1024],
        'n-words': [30000], 
        'optimizer': ['adadelta'],
        'decay-c': [0.], 
        'clip-c': [1.], 
        'use-dropout': [False],
        'learning-rate': [0.0001],
        'reload': [False]})


