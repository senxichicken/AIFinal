'''自創，因為剛好專題需要GPT，所以直接使用API，但因為上傳程式碼中沒有key，請直接參考輸出影像'''

import openai

apikey = file.read().rstrip()

openai.api_key = apikey



completion = openai.ChatCompletion.create(
    model = "gpt-4o",
    messages = [
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "請說明5/16出生的人是什麼星座，並且通常被認為有那些人格特徵?"}
    ]
)
print(completion['choices'][0]['message']['content'])