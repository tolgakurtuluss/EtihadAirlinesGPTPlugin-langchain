# Chat with Etihad Airlines GPT Plugin

This repository contains code for a LangChain framework-based chat agent that perform flight searches on Etihad Airlines GPT-Plugin based on user queries. The GPT Plugin is designed to find flights that are operated by Etihad Airlines.

Detailed info about this plugin;

1. [Etihad Airways to offer flight bookings through Astra Tech's Botim app](https://www.thenationalnews.com/business/aviation/2023/05/03/etihad-airways-to-offer-flight-bookings-through-astra-techs-botim-app/)
2. [Now, you can book Etihad flight tickets on Botim](https://gulfnews.com/business/aviation/now-you-can-book-etihad-flight-tickets-on-botim-1.95515901)
3. ["Etihad Airways signs deal to allow bookings using AI within chat app BOTIM"](https://www.reuters.com/business/aerospace-defense/etihad-airways-signs-deal-allow-bookings-using-ai-within-chat-app-botim-2023-05-03/)

## Installation

1. Clone this repository to your local machine.
2. Install the required packages by running the following command:
```bash
pip install langchain openai
```
3. Set up the OpenAI API key:
Locate the section that sets up the environment variable for the OpenAI API key. Replace 'sk-PLACEYOURAPI' with your actual OpenAI API key.

4. Run the Python script:

```bash
python main.py
```

## Usage
Enter a flight search query to Etihad Airlines GPT Plugin. In this case this prompt used as below.

```
agent_chain.run("Search flights from IST to AUH on 1st of august 2023")
```

The result of this chain after searching flights is given below.

The chat agent will process the query and provide you with relevant flight search results.
![](https://github.com/tolgakurtuluss/EtihadAirlinesGPTPlugin-langchain/blob/556dea9fce7425804e2d323d850030b5c2a4362b/chainresult.PNG)

## Final Observation

```
Observation: Found 5 flight plans for your one-way economy class trip from IST to AUH, Prices start at 1015.0 AED

Here are some recommended flight plans:

Plan 1: the full price is 1015.0 AED. Depart on August 1 at 6:15AM, arrive on August 1 at 11:45AM, with 0 stops, taking `4h 30m`. Detail link is https://gpt-etihad.botim.me/w/offer?q=8badcbf5ba004384afc7abd8b338783b

Plan 2: the full price is 3225.0 AED. Depart on August 1 at 1:30PM, arrive on August 1 at 11:05PM, with 1 stops, taking `8h 35m`. Detail link is https://gpt-etihad.botim.me/w/offer?q=9eab5fed533d4bada152358ab216279f

Plan 3: the full price is 4125.0 AED. Depart on August 1 at 7:20PM, arrive on August 2 at 12:45AM, with 0 stops, taking `4h 25m`. Detail link is https://gpt-etihad.botim.me/w/offer?q=f02a98ea71134de9821352cde1e298cf

To see more search results go to https://gpt-etihad.botim.me/w/search?q=841f72e33aa54e23bb707f457b492f80
```

## References

Etihad Airlines GPT Plugin link is gathered from [GPTStore website](https://gptstore.ai/chat/gpt-etihad-botim-me) where this GPTPlugin can be used unverified/unauthenticated.
