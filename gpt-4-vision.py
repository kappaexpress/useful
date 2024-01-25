from openai import OpenAI
import base64
import key


client = OpenAI(api_key=key.api_key2)


# ローカルの画像を読み込み、base64エンコードする関数
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


encoded_image = encode_image("test_11.jpg")


response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "これは日本語の本の目次ページの画像である。ページ数と題目がセットになっている部分を抜き出してCSVのフォーマットで出力せよ"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ],
    max_tokens=1000,
)

print(response.choices[0])
