# NLP Examples with Hugging Face Transformers

This project is a collection of Python scripts that demonstrate various Natural Language Processing (NLP) tasks using the Hugging Face `transformers` library.

## Scripts

This project includes the following scripts:

*   **`classification.py`**: Demonstrates zero-shot classification for categorizing text without prior specific training for those categories.
*   **`how_tokenizer_works.py`**: Shows the inner workings of a tokenizer, including how text is converted into numerical representations (tokens and IDs) and back into text.
*   **`pipeline3.py`**: Illustrates text generation using a pre-trained model (distilgpt2) to create new text based on a prompt.
*   **`sentiment-analysis.py`**: Performs sentiment analysis to determine if a piece of text expresses a positive, negative, or neutral sentiment. It shows usage with both default and specified models.
*   **`training.py`**: Demonstrates how to load and preprocess the IMDB dataset, a common step before training a model for tasks like sentiment classification.

## Setup

To run these scripts, you'll need to install the necessary Python dependencies.

1.  **Ensure you have Python installed.** You can download it from [python.org](https://www.python.org/).
2.  **Clone the repository (if you haven't already).**
3.  **Install the dependencies using pip:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Scripts

Each Python script in this project is designed to be run individually. You can execute any script using the following command in your terminal:

```bash
python <script_name>.py
```

For example, to run the sentiment analysis script, you would use:

```bash
python sentiment-analysis.py
```
