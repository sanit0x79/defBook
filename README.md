```
       __     ________              __  
  ____/ /__  / __/ __ )____  ____  / /__
 / __  / _ \/ /_/ __  / __ \/ __ \/ //_/
/ /_/ /  __/ __/ /_/ / /_/ / /_/ / ,<   
\__,_/\___/_/ /_____/\____/\____/_/|_|  

```

DefBook is a simple notebook application that uses OpenAI's GPT-4o-mini API to fetch concise definitions for any word you type. This tool is designed mainly for readers that want to expand their knowledge of words. DefBook allows you to save and load notebooks with stored definitions, ensuring your work is preserved and easily accessible for future reference.

## Features

- **Automatic Definitions**: Type in words, and DefBook will fetch a one-sentence definition for each using GPT-4o-mini, eliminating the need for manual lookup.
- **Notebook Saving and Loading**: Save your notebook, including words, definitions, and cached entries, to a file. Reload notebooks seamlessly with definitions preserved.
- **Efficient Caching**: Previously defined words are cached, reducing repeated API calls and speeding up your workflow.

## Requirements

- Python 3.6 or higher
- OpenAI API Key
- Virtual environment (recommended)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sanit0x79/defbook.git
   cd defbook

2. Create and activate the Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: .\venv\Scripts\activate
3. Install the required packages
   ```bash
   pip install -r requirements.txt
4. Add your OpenAI key to your env
   ```bash
   export OPENAI_API_KEY='yourkeyhere' # On Windows: set OEPNAI_API_KEY=yourkeyhere

## Pricing
### Cost Breakdown
- **Input Token Cost**: €0.150 per 1 million tokens
- **Output Token Cost**: €0.600 per 1 million tokens
- **Average Input Tokens**: ~10 tokens (prompt to define a word)
- **Average Output Tokens**: Maximum of 40 tokens per definition

### Estimated Cost per Definition
Based on the above, each definition retrieval costs approximately:

- **Input Cost**: $\(10 \, \text{tokens} \times \frac{0.150}{1,000,000} = €0.0000015\)$
- **Output Cost**: $\(40 \, \text{tokens} \times \frac{0.600}{1,000,000} = €0.000024\)$

**Total Cost per Definition**: €0.0000255

### Definitions per €5
With these rates, you can retrieve approximately **196,078 definitions** for €5, assuming an input of 10 tokens per word and a maximum of 40 output tokens per definition.

> **Note**: This is an estimate, and the actual cost may vary slightly depending on the length of each prompt and response.

## Support
If you encounter any issues or have any questions, please feel free to open an issue on GitHub or contact me at admin@logic-leap.net.

Enjoy using defBook!
