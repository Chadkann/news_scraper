from langchain_ollama import OllamaLLM

model = OllamaLLM(model='llama3.1')


def llama_summary(text):
    result = model.invoke(input=f'Write a summary for this article, skip printing any greeting: {text}')
    return result

