from ollama import chat
import json
import inspect

def has_parameters(func):
    sig = inspect.signature(func)  # 获取函数签名
    return len(sig.parameters) > 0


class FCModel:
    def __init__(self, tools, func_map, fc_model_path='qwen3:0.6b'):
        self._func_map = func_map
        self._model_path = fc_model_path
        self._tools = tools
        self.messages = [
            {
                "role": "system",
                "content": "你是一个工具助手，严格执行用户定义的tools，严格返回用户在tools设定的函数名和设定的tools参数;",
            }
        ]

    # 获取聊天流的函数
    def get_chat_stream(self, text, messages):
        messages.append({"role": "user", "content": text})
        stream = chat(
            model=self._model_path,
            messages=messages,
            tools=self._tools
        )
        return stream

    # 处理函数调用的主逻辑
    def generate(self, text):
        response = self.get_chat_stream(text, self.messages)
        # print("response:", response)
        msg = response.message

        if msg.tool_calls and msg.tool_calls is not None:
            tc = msg.tool_calls[0]           # 取第一个 ToolCall
            fn = tc.function                  # Function 对象
            fn_name = fn.name                 # 函数名
            fn_args = fn.arguments or {}      # 参数字典

            function_to_call = self._func_map.get(fn_name)
            if function_to_call:
                if has_parameters(function_to_call):
                    result = function_to_call(**fn_args)
                else:
                    result = function_to_call()
                print('Function output:', result)
            else:
                print('Function not found:', fn_name)
            return True
        else:
            return False
