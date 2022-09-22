# Assignment One - Voice commands for start and stop actions.

## Goal -

For this assignment we were asked to make a Artificial Intelligence Model that can hear the voice commands and filters the required command.

## How did we Achieve this ?

   We achieved this my making a Model that uses the data from several 'Generic Indian English telecom and broadcasts '. This dataset was under the Apache 2.0 Licence and hence Open Source to use. This algorithm also uses rescoring algorithm in it to get a greater accuracy.

![Image.png](https://res.craft.do/user/full/b39bc00a-f6ef-8bc0-9003-92e051599ad2/doc/99159D6D-BD45-49DE-BB35-DFC02987B611/8C73D027-B64D-4F5A-9DFC-EA5F0A5D74BC_2/8LDkjOrvaHFIxvVnS8hnsgz6xI77shwGeUgxXQMN1bcz/Image.png)

   This algorithm is built using 3 data sources which are -

   - Dictionary
   - Acoustic Model
   - Language Model

   The concern that the model should work even when the computer goes offline which is why I made it offline. And also with offline engine we had the option to make either small or large model so I made both. Small model typically is around 36Mb in size and requires about 100Mb of memory in runtime. Big models are for the high-accuracy transcription on the server. Big models require around 1 Gb in memory since they apply advanced AI algorithms. Ideally you run them on some high-end servers like i7 or latest AMD Ryzen. You are free to utilise whichever model you like and are fine with using. The code also provides flexibility for the models to be updated in the future and can also be used with other models given they are in the similar format.

## This is the basic view of the algorithms architecture.

![Image.png](https://res.craft.do/user/full/b39bc00a-f6ef-8bc0-9003-92e051599ad2/doc/99159D6D-BD45-49DE-BB35-DFC02987B611/BC8441BC-2B0D-4273-9DC6-14F90AEA7375_2/zbsTd5rvWxjzD4Pgakx1Kwy3FwBLwj8xaE3So67Qh0Az/output-onlinepngtools.png)

Large Model Download Link - [https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip](https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip)

Small Model Download Link - [https://alphacephei.com/vosk/models/vosk-model-small-en-in-0.4.zip](https://alphacephei.com/vosk/models/vosk-model-small-en-in-0.4.zip)

Code Link - [https://github.com/AnandSinhaProjects/TATA_Final_Voice.git](https://github.com/AnandSinhaProjects/TATA_Final_Voice.git)

