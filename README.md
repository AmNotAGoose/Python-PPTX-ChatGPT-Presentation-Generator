# PPTX Presentation Generator
## Overview

A tool to generate PowerPoint presentations using text generation based on a single prompt.


![image](https://github.com/user-attachments/assets/330a4995-c8eb-480f-91ba-0f164a53efff)
![image](https://github.com/user-attachments/assets/9159798b-c190-46be-9b9d-ab84f1afcf4d)
See a full example in `/examples` !

## Features
- Supports OpenAI and Cohere endpoints
- Specify a number of slides

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/AmNotAGoose/PPTX-Presentation-Generator
   cd PPTX-Presentation-Generator
   ```

2. Install the required packages (use an elevated shell for Windows / sudo for Linux):
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
