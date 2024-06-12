__all__ = [
    "INT_TO_FLOAT_MAPPER",
    "FLOAT_TO_INT_MAPPER",
]

__INT_TO_FLOAT_MAPPER = \
{
    "divest/mistral-7b-bnb-4bit" : (
        "divest/mistral-7b",
        "mistralai/Mistral-7B-v0.1",
    ),
    "divest/llama-2-7b-bnb-4bit" : (
        "divest/llama-2-7b",
        "meta-llama/Llama-2-7b-hf",
    ),
    "divest/llama-2-13b-bnb-4bit" : (
        "divest/llama-2-13b",
        "meta-llama/Llama-2-13b-hf",
    ),
    "divest/codellama-34b-bnb-4bit" : (
        "codellama/CodeLlama-34b-hf",
    ),
    "divest/zephyr-sft-bnb-4bit" : (
        "divest/zephyr-sft",
        "HuggingFaceH4/mistral-7b-sft-beta",
    ),
    "divest/tinyllama-bnb-4bit" : (
        "divest/tinyllama",
        "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
    ),
    "divest/tinyllama-chat-bnb-4bit" : (
        "divest/tinyllama-chat",
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    ),
    "divest/mistral-7b-instruct-v0.1-bnb-4bit" : (
        "mistralai/Mistral-7B-Instruct-v0.1",
    ),
    "divest/mistral-7b-instruct-v0.2-bnb-4bit" : (
        "mistralai/Mistral-7B-Instruct-v0.2",
    ),
    "divest/llama-2-7b-chat-bnb-4bit" : (
        "divest/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "divest/llama-2-7b-chat-bnb-4bit" : (
        "divest/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "divest/codellama-7b-bnb-4bit" : (
        "divest/codellama-7b",
        "codellama/CodeLlama-7b-hf",
    ),
    "divest/codellama-13b-bnb-4bit" : (
        "codellama/CodeLlama-13b-hf",
    ),
    "divest/yi-6b-bnb-4bit" : (
        "divest/yi-6b",
        "01-ai/Yi-6B",
    ),
    "divest/solar-10.7b-bnb-4bit" : (
        "upstage/SOLAR-10.7B-v1.0",
    ),
    "divest/gemma-7b-bnb-4bit" : (
        "divest/gemma-7b",
        "google/gemma-7b",
    ),
    "divest/gemma-2b-bnb-4bit" : (
        "divest/gemma-2b",
        "google/gemma-2b",
    ),
    "divest/gemma-7b-it-bnb-4bit" : (
        "divest/gemma-7b-it",
        "google/gemma-7b-it",
    ),
    "divest/gemma-2b-bnb-4bit" : (
        "divest/gemma-2b-it",
        "google/gemma-2b-it",
    ),
    "divest/mistral-7b-v0.2-bnb-4bit" : (
        "divest/mistral-7b-v0.2",
        "alpindale/Mistral-7B-v0.2-hf",
    ),
    "divest/gemma-1.1-2b-it-bnb-4bit" : (
        "divest/gemma-1.1-2b-it",
        "google/gemma-1.1-2b-it",
    ),
    "divest/gemma-1.1-7b-it-bnb-4bit" : (
        "divest/gemma-1.1-7b-it",
        "google/gemma-1.1-7b-it",
    ),
    "divest/Starling-LM-7B-beta-bnb-4bit" : (
        "divest/Starling-LM-7B-beta",
        "Nexusflow/Starling-LM-7B-beta",
    ),
    "divest/Hermes-2-Pro-Mistral-7B-bnb-4bit" : (
        "divest/Hermes-2-Pro-Mistral-7B",
        "NousResearch/Hermes-2-Pro-Mistral-7B",
    ),
    "divest/OpenHermes-2.5-Mistral-7B-bnb-4bit" : (
        "divest/OpenHermes-2.5-Mistral-7B",
        "teknium/OpenHermes-2.5-Mistral-7B",
    ),
    "divest/codegemma-2b-bnb-4bit" : (
        "divest/codegemma-2b",
        "google/codegemma-2b",
    ),
    "divest/codegemma-7b-bnb-4bit" : (
        "divest/codegemma-7b",
        "google/codegemma-7b",
    ),
    "divest/codegemma-7b-it-bnb-4bit" : (
        "divest/codegemma-7b-it",
        "google/codegemma-7b-it",
    ),
    "divest/llama-3-8b-bnb-4bit" : (
        "divest/llama-3-8b",
        "meta-llama/Meta-Llama-3-8B",
    ),
    "divest/llama-3-8b-Instruct-bnb-4bit" : (
        "divest/llama-3-8b-Instruct",
        "meta-llama/Meta-Llama-3-8B-Instruct",
    ),
    "divest/llama-3-70b-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B",
    ),
    "divest/llama-3-70b-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B-Instruct",
    ),
    "divest/Phi-3-mini-4k-instruct-bnb-4bit" : (
        "divest/Phi-3-mini-4k-instruct",
        "microsoft/Phi-3-mini-4k-instruct",
    ),
    "divest/mistral-7b-v0.3-bnb-4bit" : (
        "divest/mistral-7b-v0.3",
        "mistralai/Mistral-7B-v0.3",
    ),
    "divest/mistral-7b-instruct-v0.3-bnb-4bit" : (
        "divest/mistral-7b-instruct-v0.3",
        "mistralai/Mistral-7B-Instruct-v0.3",
    ),
    "divest/Phi-3-medium-4k-instruct-bnb-4bit" : (
        "divest/Phi-3-medium-4k-instruct",
        "microsoft/Phi-3-medium-4k-instruct",
    ),
    "divest/Qwen2-0.5B-bnb-4bit" : (
        "divest/Qwen2-0.5B",
        "Qwen/Qwen2-0.5B",
    ),
    "divest/Qwen2-0.5B-Instruct-bnb-4bit" : (
        "divest/Qwen2-0.5B-Instruct",
        "Qwen/Qwen2-0.5B-Instruct",
    ),
    "divest/Qwen2-1.5B-bnb-4bit" : (
        "divest/Qwen2-1.5B",
        "Qwen/Qwen2-1.5B",
    ),
    "divest/Qwen2-1.5B-Instruct-bnb-4bit" : (
        "divest/Qwen2-1.5B-Instruct",
        "Qwen/Qwen2-1.5B-Instruct",
    ),
    "divest/Qwen2-7B-bnb-4bit" : (
        "divest/Qwen2-7B",
        "Qwen/Qwen2-7B",
    ),
    "divest/Qwen2-7B-Instruct-bnb-4bit" : (
        "divest/Qwen2-7B-Instruct",
        "Qwen/Qwen2-7B-Instruct",
    ),
    "divest/Qwen2-70B-bnb-4bit" : (
        "Qwen/Qwen2-70B",
    ),
    "divest/Qwen2-70B-Instruct-bnb-4bit" : (
        "Qwen/Qwen2-70B-Instruct",
    ),
}

INT_TO_FLOAT_MAPPER = {}
FLOAT_TO_INT_MAPPER = {}

for key, values in __INT_TO_FLOAT_MAPPER.items():
    INT_TO_FLOAT_MAPPER[key] = values[0]

    for value in values:
        FLOAT_TO_INT_MAPPER[value] = key
    pass
pass