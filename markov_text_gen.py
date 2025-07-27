import random

def build_markov_chain(text, n=1):
    """Builds a Markov chain of order n"""
    words = text.split()
    chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i+n])  # current state
        next_word = words[i+n]     # next word
        if key not in chain:
            chain[key] = []
        chain[key].append(next_word)

    return chain

def generate_text(chain, n=1, max_words=50):
    """Generates text using the Markov chain"""
    start = random.choice(list(chain.keys()))
    output = list(start)

    for _ in range(max_words - n):
        state = tuple(output[-n:])
        next_words = chain.get(state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        output.append(next_word)

    return ' '.join(output)

# --- MAIN EXECUTION ---

# Load your input text (you can replace this with any text file)
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Step 1: Build the chain
n = 2  # change to 1 for basic, 2 for better grammar
markov_chain = build_markov_chain(data, n=n)

# Step 2: Generate new text
generated = generate_text(markov_chain, n=n, max_words=60)

# Step 3: Show result
print("🔹 Generated Text 🔹\n")
print(generated)
