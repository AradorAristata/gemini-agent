# Gemini Agent

A project for building and managing AI agents powered by Google's Gemini model.

FOR THE LOVE OF ALL THAT IS HOLY, THIS IS JUST A TEST TOOL. DO NOT USE IT WITHOUT TAKING A LOT OF CARE TO ISOLATE
WHAT IT CAN TOUCH. I PASS IN THE WORKING DIRECTORY AS THE CALCULATOR APP BUT BE SURE YOU UNDERSTAND WHAT IS
HAPPENING BEFORE YOU RUN IT.

## Overview

This project provides a framework for creating intelligent agents that leverage the Gemini API to perform various tasks, including code generation, analysis, and automation.

## Features

- Integration with Google's Gemini API
- Agent architecture for task execution
- Extensible design for custom workflows
- Error handling and logging

## Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API key

### Installation

```bash
git clone <repository-url>
cd gemini-agent
pip install -r requirements.txt
```

### Configuration

Set your Gemini API key:

```bash
export GEMINI_API_KEY=<your-api-key>
```

or Create a .env file and paste the key in there.

NB NB NB NB NB NB!!!
DO NOT UPLOAD YOUR .env FILE TO A PUBLIC REPO. ADD IT TO GITIGNORE IMMEDIATELY!!!

### Usage

```python
from gemini_agent import Agent

agent = Agent()
response = agent.run("Your task here")
print(response)
```

## Contributing

Contributions welcome. Please submit a pull request or open an issue.

## License

MIT