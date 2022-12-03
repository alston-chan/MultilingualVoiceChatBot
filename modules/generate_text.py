def generate_text(model, tokenizer, instruction, knowledge, query, top_p, min_length, max_length):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = [query]
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"

    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, min_length=int(
        min_length), max_length=int(max_length), top_p=top_p, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(query)
    print(output)
    return output
