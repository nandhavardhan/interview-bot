from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Small, CPU-friendly Q&A model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model     = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_answer(context: str, question: str, mode: str) -> str:
    instr = (
        "Please answer concisely in 1–2 paragraphs."
        if mode == "brief"
        else "Please provide a structured, multi-paragraph answer."
    )
    prompt = f"{instr}\nContext:\n{context}\nQuestion: {question}"
    out = generator(prompt, max_length=512, do_sample=False)
    return out[0].get("generated_text", "")
