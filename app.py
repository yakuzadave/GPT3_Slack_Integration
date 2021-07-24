import os
from dotenv import load_dotenv, dotenv_values
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


config = dotenv_values('.env')
api_key = config.get('OPEN_API_KEY')
SLACK_BOT_TOKEN =config.get('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = config.get('SLACK_APP_TOKEN')
SLACK_SIGNING_SECRET = config.get('SLACK_SIGNING_SECRET')
openai.api_key = api_key


def gpt3(prompt_content):
    start_sequence = "\nA:"
    restart_sequence = "\nQ:"

    #Default setting
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_content + start_sequence,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
        stop=["\n"]
    )

    # Curie Engine
    # response = openai.Completion.create(
    #     engine="curie",
    #     prompt=prompt_content + start_sequence,
    #     temperature=0.5,
    #     max_tokens=100,
    #     top_p=1,
    #     frequency_penalty=0.2,
    #     presence_penalty=0,
    #     stop=["\n"]
    # )

    response_text = response['choices'][0]['text']
    print(response_text)
    new_prompt_text = prompt_content + start_sequence + response_text
    obj = {
        "new_prompt_text": new_prompt_text,
        "response_text": response_text
    }
    return obj


def gpt_req(req):
    with open('./prompt1.txt', 'r') as f:
        lines = f.readlines()
        lines = "".join(lines)
    res = gpt3(f"{lines}\nQ: {req}")
    answer = res['response_text']
    return answer


slack_app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)



@slack_app.event("app_mention")
def handle_app_mention_events(body, logger, client,say):
    logger.info(body)
    print(body)
    logger.info(body)
    print(body)
    event = body['event']
    event_text = event['text']
    
    # Enter your bot id here to slice it from the text.
    mention = "<@U000000000000>"
    if (event_text.find(mention) != -1):
        # So basic while the bot is 
        say("Sure, I can try to come up with something for you.")
        question = event_text[15:]
        print(question)
        res = gpt_req(question)
        print(res)
        say("I have something for you.  I am still learning, so feel free to check the results and make any modifications that you need.")
        say(res)




if __name__ == '__main__':
    handler = SocketModeHandler(slack_app, SLACK_APP_TOKEN)
    handler.start()
    port = int(os.environ.get('PORT', 5000))
    slack_app.start(port=int(os.environ.get("PORT", 3000)))
