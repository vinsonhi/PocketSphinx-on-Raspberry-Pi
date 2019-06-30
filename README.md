# PocketSphinx-on-Raspberry-Pi
  build a a intellectual desk lamp of offline speech recognition system
  
  With the great transterability, developers can build smart desk lamp, or smart lock, or smart electric switch and so on rapidly.Besieds, instead of connecting to the network and installing the APP, user just need to input voice commands. With using smart desk lamp as a demo, the major work and contribution of this thesis includes:
1.	  Based on the Raspberry Pi, build a smart desk lamp which is equipped with the speech recognition system. With installing the open source speech recognition framework Pocketsphinx, the system will give feedback and operate the given script files in one or two seconds. Moreover, to be friendly to user as more as possible, the voice command allow user to mix some natural language like ‘please’,’hey’,’um’ and so on. 
2.	  Propose a language model trainning method based on the 2-gram and 3-gram model, and use voice signals from different distance to train the acoustic model, which greatly improves the recognition accuracy of Pocketsphinx on the Raspberry Pi. It can achieve a recognition rate of nearly 90% within 2m, and the probability of 99.9% will not be triggered by the chat, which meets the requirement of smart home.

before running the task, you need to insert the following command
  
  export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
  
  export LD_LIBRARY_PATH=/usr/local/lib

running command:
  
  pocketsphinx_continuous -lm /home/pi/pocketsphinx-0.7/model/lm/en_US/9935.lm -dict /home/pi/pocketsphinx-0.7/model/lm/en_US/9935.dic -hmm /home/pi/pocketsphinx-0.7/model/hmm/en_US/cmu-adapt/  >> test.txt
