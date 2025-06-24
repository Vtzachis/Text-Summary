import google.generativeai as genai
import gradio as gr
from getpass import getpass
api_key = getpass("Enter your API key: ")


genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_text(user_input):
    prompt = f"Summarize into bullet points using logical thinking about what is more crucial:\n\n{user_input}"
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=300)
        )
        return response.text or "No summary generated."
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("## ✨ Gemini Summarizer")
    input_text = gr.Textbox(lines=15, label="Paste your text")
    output_text = gr.Textbox(lines=15, label="Summary")
    btn = gr.Button("Summarize")
    btn.click(summarize_text, inputs=input_text, outputs=output_text)

demo.launch(share=True)


