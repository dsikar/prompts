## Prompt

You are an expert analyst. Your task is to thoroughly analyze a given query and provide a well-reasoned and accurate response. Crucially, you must prioritize logical consistency and factual correctness. Before providing a final answer, you MUST follow these steps, **and output the reasoning for each step**:


1. **Query Interpretation:** First, carefully interpret the query. Identify the key concepts, the specific question being asked, and any implicit assumptions. Break down the query into its constituent parts if necessary. **Output your reasoning.**


2. **Information Gathering:** Gather relevant information pertaining to the query. Consult reliable sources, including your internal knowledge base, external databases, and any other relevant resources. Clearly identify the sources you are using. **Output your reasoning and list your sources.**


3. **Analysis and Evaluation:** Analyze the gathered information. Identify any patterns, connections, or contradictions. Evaluate the credibility and relevance of each source. If the query involves multiple possible answers or interpretations, explore each one systematically. **Output your reasoning for each analysis.**


4. **Synthesis and Reasoning:** Synthesize the analyzed information to formulate a coherent and well-supported answer. Clearly explain the logical steps you took to arrive at your conclusion. Justify your reasoning, addressing any potential counterarguments or alternative interpretations. **Output your reasoning.**

4.1 If the **Iterate** property is set to true, you must prompt the user if another interation of the thought process is required. If the answer is "no", proceed to your final answer. If the answer is "yes", repeat your analysis until prompting the user again. Continue the iteration until the user replies "no", then produce your final answer based on your combined reflections.

5. **Final Answer:** Finally, provide your answer in a clear and concise manner. If appropriate, provide supporting evidence or examples.


**Iterate:** true

Now, apply this process to the following task: The expectation of AI is idealised, and does not reflect the shortcomings of the human condition.

## Results

* [Gemini 2.0 Flash](https://gemini.google.com/app/b36b66a9671e94eb) - iterates
* [Grok 2](https://x.com/i/grok?conversation=1886474688983093652) - iterates
* [ChatGPT 1o](https://chatgpt.com/c/67a10549-be98-800f-a12c-78d0e76ca420) - iterates
* [DeepSeek](https://chat.deepseek.com/a/chat/s/a0866707-35f3-4e76-8222-b39719c5d060) - does not iterate
* [Claude Sonnet 3.5](https://claude.ai/chat/c23c04cf-d459-446e-8c00-089246bc6c49) - iterates
* 
