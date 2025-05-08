import webbrowser

################################## 
def open_browser():
    url = "https://www.baidu.com"
    webbrowser.open(url)
    return f"已打开浏览器，访问 {url}"

def turn_off_light():
    return "灯已关闭"

def turn_on_light(brightness:int):
    return f"灯已调亮{brightness}"

def turn_left(angle:int):
    return f"左转{angle}度"
##################################

##################################
tools = [
    {
        "type": "function",
        "function": {
            "name": "turn_on_light",
            "description": "开灯或者turn on light，调高多少亮度",
            "arguments": {
                "angle": {
                    "type": "int",
                    "description": "调高的亮度"
                }
            }
        },
    },
    {
        "type": "function",
        "function": {
            "name": "turn_off_light",
            "description": "关灯或者turn off light",
        }
    },
    {
        "type": "function",
        "function": {
            "name": "turn_left",
            "description": "左转一定角度",
            "arguments": {
                "angle":{
                    "type": "float",
                    "description": '旋转的角度值',
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "open_browser",
            "description": "打开浏览器",
        }
    }
]
##################################

func_map = {
    "turn_off_light": turn_off_light,
    "turn_on_light": turn_on_light,
    "turn_left": turn_left,
    "open_browser": open_browser
}