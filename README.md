# Real-Time Emotion and Interest Detection

This repository contains a Python script for real-time face detection, emotion analysis, and interest determination using OpenCV and DeepFace. The script captures video from a webcam, detects faces, analyzes their emotions, and displays whether the person is interested based on their emotional state and confidence level.

## Requirements

To run the script, you need to install the following libraries:

- OpenCV
- DeepFace
- NumPy

You can install these dependencies using pip:

```bash
pip install opencv-python deepface numpy
```

## Script Overview

The script captures video frames from the default webcam, detects faces using the Haar Cascade classifier, and analyzes the emotions of the detected faces using the DeepFace library. It also determines if the person is interested based on the dominant emotion and its confidence level.

### Emotion Colors

The script uses a predefined set of colors to highlight different emotions:

- Angry: Red
- Disgust: Yellow
- Fear: Blue
- Happy: Green
- Sad: Cyan
- Surprise: Magenta
- Neutral: White

### Interest Analysis

The script considers a person interested if their dominant emotion is 'happy', 'surprise', or 'neutral' with a confidence level above 70%. Otherwise, it considers the person not interested.

### How to Run

1. Clone the repository:

```bash
git clone https://github.com/codewithdark-git/InterestAnalyzer.git
cd InterestAnalyzer
```

2. Run the script:

```bash
python emotion_detection.py
```

3. Press 'q' to exit the video feed.

## Files

- `emotion_detection.py`: The main script for emotion detection and interest analysis.
- `README.md`: This documentation file.

## Usage

This project can be used for various applications, such as:

- Real-time emotion monitoring
- Enhancing user experience by adapting to emotions
- Interest detection in video calls or presentations

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [DeepFace](https://github.com/serengil/deepface)
- [NumPy](https://numpy.org/)

---

## Project Background

This project was inspired by a memorable classroom experience. In a lively database class with a strict but perceptive teacher, it was common to witness a mix of strict discipline and spontaneous humor. 

One day, the teacher remarked on their ability to read our emotions from our expressions and behaviors. This sparked an idea: what if we could create a system that uses machine learning to read students' faces and assess their interest levels in real-time? Such a system could help identify who is engaged and who isn't, making it a valuable tool for educators.

This project aims to bridge technology and education, enhancing the learning experience by providing real-time feedback on student engagement. This tool can help teachers tailor their methods to better suit the needs of their students, creating a more responsive and effective learning environment.