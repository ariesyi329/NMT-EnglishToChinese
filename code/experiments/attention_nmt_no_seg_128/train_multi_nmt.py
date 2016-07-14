import numpy
import os

from code.model.attention_nmt.multi_nmt import train

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
					datasets=['/home/yl3068/NMT/NMT-EnglishToChinese/data/zh/no_seg/zh.train.no_seg.tok',
					'/home/yl3068/NMT/NMT-EnglishToChinese/data/en/train.en.tok'],
					valid_datasets=['/home/yl3068/NMT/NMT-EnglishToChinese/data/zh/no_seg/zh.dev.no_seg.tok',
				        '/home/yl3068/NMT/NMT-EnglishToChinese/data/en/dev.en.tok'],
					dictionaries=['/home/yl3068/NMT/NMT-EnglishToChinese/data/zh/no_seg/zh.train.no_seg.tok.pkl',
					'/home/yl3068/NMT/NMT-EnglishToChinese/data/en/train.en.tok.pkl'],
                                        validFreq=5000,
                                        dispFreq=10,
                                        saveFreq=5000,
                                        sampleFreq=1000,
                                        use_dropout=params['use-dropout'][0])
    return validerr

if __name__ == '__main__':
    main(0, {
        'model': ['/home/yl3068/NMT/NMT-EnglishToChinese/code/experiments/attention_nmt_no_seg_128/model_multi.npz'],
        'dim_word': [128],
        'dim': [128],
        'n-words': [30000],
        'optimizer': ['adadelta'],
        'decay-c': [0.],
        'clip-c': [1.],
        'use-dropout': [False],
        'learning-rate': [0.0001],
        'reload': [False]})


