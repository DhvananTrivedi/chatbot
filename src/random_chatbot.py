import random
import gradio as gr

## Backend
def random_response(message, history):
    return random.choice(["Yes", "No"])

## Frontend
demo = gr.ChatInterface(random_response, type="messages", autofocus=False)

if __name__ == "__main__":
    demo.launch()
