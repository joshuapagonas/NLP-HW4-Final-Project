# NLP-HW4-Final-Project User Guide:

How it was Built:
Web scrapping the STM32 Part Website, creating a GUI within tkinter, and combining it within the Gradio framework to host it on Hugging Face.

Model Loading:
I loaded a Gemini Model to have the user prompt ask to compare the different parts within the GUI application. Once compared, it displays the results of the different parts.

Data Preparation:
Through web scrapping the STM32 Part Website, I was able to gather 100 different part urls that have their specifications all scrapped.Once scrapped, the part data was stored within different part text files that were read through to have their data compared with one another through storing them within a GUI to compare. 

Limitations and Constraints:
Only used about 10 different parts to compare with due to time constraints.

Run Locally:
Within the "NLP HW4 Final Project Demo" directory, run this command: python demo.py

You should be able to have a live share link from there to test out the application yourself.
