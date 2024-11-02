base_url = 'https://api.rhymes.ai/v1'
api_key = ''  # Replace with your actual API key

from openai import OpenAI

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)


# ==================================================================================================
# test based
# response = client.chat.completions.create(
#     model="aria",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "How can I make toothpaste?"
#                 }
#             ]
#         }
#     ],
#     stop=["<|im_end|>"],
#     stream=False,
#     temperature=0.6,
#     max_tokens=1024,
#     top_p=1
# )

# print(response.choices[0].message.content)


# ==================================================================================================
# image based
import base64

def image_to_base64(image_path):
    """
    Converts an image to a base64-encoded string.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64-encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        return base64_string
    except FileNotFoundError:
        return "Image file not found. Please check the path."
    except Exception as e:
        return f"An error occurred: {str(e)}"

base64_image_1 = image_to_base64('img/im1.jpg')
base64_image_2 = image_to_base64('img/im2.jpg')

response = client.chat.completions.create(
    model="aria",  # Model name updated
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_1}"
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_2}"
                    }
                },
                {
                    "type": "text",
                    "text": "<image><image>\nWhat's in the image?"  # Added <image> symbols for each image
                }
            ]
        }
    ],
    stream=False,
    temperature=0.6,
    max_tokens=1024,
    top_p=1,
    stop=["<|im_end|>"]
)

print(response.choices[0].message.content)