import re

def generate_questions(text, long_q_count, short_q_count, model=None, tokenizer=None):
    if model is None or tokenizer is None:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

    total_requested = long_q_count + short_q_count
    generated_qs = []
    
    # --- SMART CHUNKING (Fixes the single paragraph issue) ---
    # Agar \n\n nahi mila, toh text ko har 800 characters ke blocks me todenge
    chunk_size = 800
    paragraphs = []
    
    for i in range(0, len(text), chunk_size):
        block = text[i:i+chunk_size].strip()
        if len(block) > 100:  # Sirf unhi blocks ko lein jo meaningful hain
            paragraphs.append(block)
            
    if not paragraphs:
        paragraphs = [text]

    # --- QUESTION GENERATION LOOP ---
    for para in paragraphs:
        if len(generated_qs) >= total_requested:
            break
            
        # AI ko prompt me explicitly bolenge ki unique questions banaye
        prompt = (
            f"Context: {para}\n\n"
            f"Task: Generate a unique, clear question based on the context above."
        )
        
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        
        outputs = model.generate(
            **inputs, 
            max_length=64, 
            do_sample=True,         # Sampling enabled for variety
            temperature=0.8,        # Creativity badhane ke liye thoda badhaya
            top_k=50,
            top_p=0.95
        )
        
        q_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        
        # Clean up and validation
        if q_text and len(q_text) > 10 and not q_text.isdigit():
            if not q_text.endswith("?"):
                q_text += "?"
                
            # Formatting clean up (agar AI ne 'Question:', 'Q1:' jaisa kuch generate kiya ho)
            q_text = re.sub(r'^(question|q\d+:|query):\s*', '', q_text, flags=re.IGNORECASE)
            
            if q_text not in generated_qs:
                generated_qs.append(q_text)

    # --- FALLBACK MECHANISM (Agar abhi bhi count kam reh jaye) ---
    # Agar text content kam pad gaya aur requested 10 questions poore nahi huye
    backup_questions = [
        "What are the primary features of Python discussed in this section?",
        "Explain the fundamental concepts introduced in this chapter.",
        "What are the standard expressions and operations used here?",
        "Describe the practical applications of the topics covered above.",
        "What are the common syntax rules to keep in mind for this topic?",
        "Give a detailed overview of the core components explained in the text."
    ]
    
    backup_idx = 0
    while len(generated_qs) < total_requested and backup_idx < len(backup_questions):
        if backup_questions[backup_idx] not in generated_qs:
            generated_qs.append(backup_questions[backup_idx])
        backup_idx += 1

    return generated_qs[:total_requested]