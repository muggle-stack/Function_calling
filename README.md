## LLM Model Function Calling

The content of this project is to call the function calling function of qwen3 through the ollama API. There are 4 built-in functions, "open browser", "light up {parameter}", "turn off light" and "turn left {angle}". The actual operation is "open browser", and the other three functions only return print function (you can develop or add functions to realize the internal functions of the functions yourself)

## Install dependencies

```bash
pip install ollama webbrowser
```

## Usage

Clone code

```bash
git clone https://github.com/muggle-stack/Function_calling.git
cd Function_calling
python main.py
```

You can call a function by inputting operations related to the function, such as "open the browser". After the big model recognizes the semantics, it will open the browser. If no related functions are detected, the big model will communicate with you normally.