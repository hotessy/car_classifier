# openCV HOG Trainer

Example linux program on how to train your custom HOG detecting vector for use with openCV hog.setSVMDetector(_descriptor)

## Information

For the paper regarding Histograms of Oriented Gradients (HOG), see http://lear.inrialpes.fr/pubs/2005/DT05/.
You can populate the positive samples dir with files from the INRIA person detection dataset, see http://pascal.inrialpes.fr/data/human/.
This program uses SVMlight as machine learning algorithm (see http://svmlight.joachims.org/), but is not restricted to it.
Tested in Ubuntu Linux 64bit 12.04 "Precise Pangolin" with openCV 2.3.1, SVMlight 6.02, g++ 4.6.3 and standard HOG settings, training images of size 64x128px.

What this program basically does:
* Read positive and negative training sample image files from specified directories
* Calculate their HOG features and keep track of their classes (pos, neg)
* Save the feature map (vector of vectors/matrix) to file system
* Read in and pass the features and their classes to a machine learning algorithm, e.g. SVMlight
* Train the machine learning algorithm using the specified parameters
* Use the calculated support vectors and SVM model to calculate a single detecting descriptor vector
* Dry-run the newly trained custom HOG descriptor against training set and against camera images, if available

## Usage

Build by issuing:
    ./complile.sh   


## Run by issuing:
    ./trainhog

## Warning words

* At least one of the functions (opendir) doing file system operations is unix/linux-only, for using the program in other operating systems a alternative API functions have to be used.
* Be aware that the program may consume a considerable amount of main memory, hard disk memory and time, dependent on the amount of training samples.
* Also be aware that (esp. for 32bit systems), there are limitations for the maximum file size which may take effect when writing the features file.
