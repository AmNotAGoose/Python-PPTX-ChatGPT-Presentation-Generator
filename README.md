# PPTX Presentation Generator
## Overview

A tool to generate PowerPoint presentations using text generation based on a single prompt.

## Features
- Supports OpenAI and Cohere endpoints
- Specify a number of slides

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/AmNotAGoose/PPTX-Presentation-Generator
   cd PPTX-Presentation-Generator
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to run

To launch the user interface:
```bash
python ui.py
```

## API keys

Depending on which platform you pick, you will need to input an API key. You can find this at:
- OpenAI: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
- Cohere (free): [https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)

## Known issues

- The GUI may freeze when "Submit" is clicked. It will unfreeze once it is finished.

## Troubleshooting

- Make sure you have pressed "Save API Key" before pressing "Submit" 
