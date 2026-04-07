The Problem with Default Responses
By default, when you ask Claude to generate JSON, you might get something like this:

```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
```

This rule captures EC2 instance state changes when instances start running.

The JSON is correct, but it's wrapped in markdown formatting and includes explanatory text. For a web app where users need to copy the raw JSON, this creates friction in the user experience.

## The Solution: Assistant Message Prefilling + Stop Sequences

You can combine assistant message prefilling with stop sequences to get exactly the content you want. Here's how it works:

````
messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
````

This technique works by:

The user message tells Claude what to generate
The prefilled assistant message makes Claude think it already started a markdown code block
Claude continues by writing just the JSON content
When Claude tries to close the code block with ```, the stop sequence immediately ends generation

![alt text](image-3.png)
