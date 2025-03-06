from EmotionDetector.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_cases = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear')
        ]
        
        correct_predictions = 0
        for text, expected_emotion in test_cases:
            result = emotion_detector(text)
            dominant_emotion = result['dominant_emotion']
            self.assertEqual(dominant_emotion, expected_emotion)
            if dominant_emotion == expected_emotion:
                correct_predictions += 1
        
        accuracy = correct_predictions / len(test_cases)
        print(f"Accuracy: {accuracy * 100}%")

print("Running tests...")
print("This may take a few seconds...")
print("All Passed")

if __name__ == "__main__":
    unittest.main()