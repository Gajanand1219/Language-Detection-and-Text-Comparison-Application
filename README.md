# Language Detection and Text Comparison Application Api
**This Flask application allows users to detect the language of input text and compare two pieces of text for similarity.**
**This is a Flask web application that provides two primary functionalities: detecting the language of input text and comparing two pieces of text for similarity.**


https://github.com/user-attachments/assets/f553d73f-4241-4329-a341-cd46711d72ae



## Features

- **Language Detection**: Identifies the language of user-provided text using the `langdetect` library. Displays the detected languages along with their probabilities.
- **Text Comparison**: Compares two texts to determine if they are identical (case insensitive) and calculates the percentage of similarity based on matching characters.
- **User-Friendly Interface**: Intuitive HTML forms for user input, accompanied by clear results presentation.
- **Visual Feedback**: Animated progress bar displaying the accuracy percentage during text comparison.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **langdetect**: A language detection library for Python.
- **HTML/CSS**: For structuring and styling the web application.

## Usage
- Navigate to the "Text Detection" page to detect the language of a text input.
- Use the "Text Compare" page to compare two texts and see the similarity percentage.

1. **Language Detection**
   - Purpose: This functionality detects the language of the input text and provides a probability score for each detected language.
   - Main Components:
     - **Flask Routes**: The `/` route serves the language detection page, and the `/detect` route processes the submitted text.
     - **Language Detection Logic**: It uses the `langdetect` library to analyze the input text. The `detect_langs` function identifies the languages and their associated probabilities.
     - **Language Mapping**: A dictionary (`LANGUAGE_MAP`) maps language codes to full language names, which is used to display user-friendly results.
     - **Result Display**: After processing the input, the detected languages and their probabilities are displayed on the page.

2. **Text Comparison**
   - Purpose: This functionality compares two pieces of text to determine if they are identical and calculates the percentage accuracy of their similarity.
   - Main Components:
     - **Flask Routes**: The `/text` route serves the text comparison page and processes the submitted texts.
     - **Comparison Logic**: The `calculate_accuracy` function compares the two texts character by character to calculate the accuracy percentage based on matching characters.
     - **Result Display**: If the texts are identical (case insensitive), a message is shown; otherwise, it indicates the texts are different. The calculated accuracy percentage is also displayed.

3. **HTML Templates**
   - Structure: There are two main HTML templates (`lang.html` for language detection and `compare.html` for text comparison) that include:
     - **Navigation Bar**: Links to switch between the language detection and text comparison functionalities.
     - **Forms**: Each functionality has a form where users can input text. The language detection form has a button that triggers a loading animation while processing.
     - **Progress Bar Animation**: In the text comparison section, a progress bar visually represents the accuracy percentage, animating from 0% to the calculated accuracy value.

4. **CSS Styles**
   - Styling: The CSS styles define the layout, colors, and appearance of various elements, enhancing the user interface with a cohesive and appealing design.

5. **Code Overview**
   - This code is designed to enhance the user interface of a web application by displaying a loading animation and a progress bar that visually represents the accuracy of a process, such as language detection or text comparison.
     #
## Summary

Overall, your application provides users with a straightforward way to detect languages and compare texts. The combination of Flask for backend processing, `langdetect` for language analysis, and well-structured HTML/CSS for frontend display creates an effective tool for language-related tasks.

If you have any specific questions or need help with features, let me know!
