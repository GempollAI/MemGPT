# MemGPT - Gempoll

## Setup

1. Setup api keys by creating `./functions/api.json`
    ```
    {
      "url": "your_api_url",
      "key": "your_api_key"
    }
    ```
2. Setup Persona: `memgpt add persona --name sam_cn -f ./persona/sam_cn.txt `
3. Setup Human: `memgpt add human --name alice_the_pm_cn -f ./human/alice_the_pm_cn.txt`
4. Setup Agents: `sh setup_custom_agent.sh`

