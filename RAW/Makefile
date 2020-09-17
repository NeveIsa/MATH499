

all: clean tranch1 tranch2 tranch3


tranch1:
	wget http://sampy.ml:499/persons-posture-tranch1.zip
	unzip persons-posture-tranch1.zip
	mv home/tyler/git/darknet/data/persons/yolo/v4/ tranch1
	wget http://sampy.ml:499/tranch1_labels.csv

tranch2:
	wget http://sampy.ml:499/persons-posture-tranch2.zip
	unzip persons-posture-tranch2.zip
	wget http://sampy.ml:499/tranch2_labels.csv

tranch3:
	wget http://sampy.ml:499/persons-posture-tranch3.zip
	unzip persons-posture-tranch3.zip
	wget http://sampy.ml:499/tranch3_labels.csv


clean:
      	rm -rf home
