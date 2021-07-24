# GPT3_Slack_Integration
A way to make requests to OpenAI GPT-3 using your Slack client for the prompts.  Firor the Slack bit, I decided to go with Slack Bolt since it is so easy to work with.  I've also gone ahead and enabled Socket Mode for Slack because it is easier than needing to expose a HTTP endpoint.

## What you'll need

### A Slack App/Bot

I have gone ahead and added an example Slack App manifest in `slack_app_manifest.yml` ,but mostly you eill need the following:

- app_mentions:read
- chat:write

### OpenAPI GPT-3 API Key

This one is a little more tricky since these API Keys are a little harder to come by (I just got mine after waiting for some time).  Once you have your key, you can use the [Playground](https://beta.openai.com/playground/) for testing out your prompts and then export.  I started with using `davinci` at first, and it is definitely the most powerful, but I got a lot of good results with `curie` as well and it is 1/10th the cost (You will likely have some free credits but you can burn through those pretty quick).

#### Prompt limits

One thing that I was running into a lot was hitting the prompt limits.  I still need to do some testing with this, but I was thinkiing of splitting up the prompts across multiple requests/files and then choosing the one that comes back with the best result.



