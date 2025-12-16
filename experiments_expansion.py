from modules.expansion import FooocusExpansion

expansion = FooocusExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
def lock_realistic_lighting(prompt):
    lighting = (
        "soft window lighting, "
        "natural light falloff, "
        "cinematic shadows, "
        "realistic facial depth"
    )

    if lighting not in prompt:
        prompt = f"{prompt}, {lighting}"

    return prompt
