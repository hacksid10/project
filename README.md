# Local Agent

This workspace now contains a minimal agent scaffold for a local assistant.

## What it does

The agent accepts a user request, recognizes a few built-in actions, and responds in a simple chat loop.

## Example agent

```python
class Agent:
    def __init__(self, name: str = "LocalAgent"):
        self.name = name

    def respond(self, prompt: str) -> str:
        prompt = prompt.strip().lower()

        if not prompt:
            return "I’m ready. Ask me anything."
        if prompt in {"hi", "hello", "hey"}:
            return f"Hello! I’m {self.name}. How can I help?"
        if prompt.startswith("echo "):
            return prompt[5:]
        if prompt == "status":
            return "Agent is online and ready."
        return "I can help with simple commands like hello, status, and echo."


if __name__ == "__main__":
    agent = Agent()
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Agent: Goodbye!")
            break
        print(f"Agent: {agent.respond(user_input)}")
```

## Run it

1. Copy the script into a Python file such as `agent.py`.
2. Run:

```bash
python agent.py
```

The agent supports a few simple commands:
- `hello`
- `status`
- `echo <message>`
- `exit`

This gives you an immediately usable local agent foundation that can be extended with tool calls, memory, or API integrations later.


This file has been initialized for the local agent project.
using this for the project creation

## Sewing services demo website
A static demo site was added in `sewing-services-demo/`.

### Run locally
Open `sewing-services-demo/index.html` in your browser.
