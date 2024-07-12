# AI Agentic Framework

AI Agentic framework - I would proudly call this a "great minds think alike" concept. As I was prototyping this concept, at a parallel point of the same time fabric, Prof. Wang, L had publised a paper[1] on this line. AI Agentic framework would consider a Planner node and one or more worker nodes. 

## The Planner node:
- Orchestrates interactions with user / system
- Breaks down the task in hand into contained individual steps
- Collates results and workder nodes

## The Worker node(s):
- Is initiated for each step outlined by planner node
- Always works in a "function-calling" pattern
- Invokes Tools or external API as needed / defined
- Doesn't get too creative (unless needed) and responds to the point
  


### Citation
[1] https://arxiv.org/abs/2305.04091?ref=blog.langchain.dev 
