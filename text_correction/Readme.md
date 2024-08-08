# Spelling Correction using python:
### About
Did you know that you can correct spelling errors in text using Python? Python has a library called TextBlob that corrects spelling errors. Use pip to install the library
```bash
pip install -U textblob
```
Below, we pass a string to textblob that has spelling errors. You can see that the errors have been replaced with the correct spelling. Textblob will pick the most likely correct word for the misspelled word. But the traff off with this library is it performs poorly on homophones(Words with similar pronunciation). Check the below example:

The sun was shining **britely** in the sky. ---> The sun was shining **bristly** in the sky.

This is good for minor spelling mistakes, but 

### Practical Usage:
Use this script as a utility to automate spelling corrections across multiple text files. Simply iterate through your files, pass the content through TextBlob, and save the corrected text back to the original or a new file. This can be a time-saver when dealing with large volumes of text data.

Example: I can pass the same readme file through the script to check if there are any mistakes me instead of checking word-to-word.