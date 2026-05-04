# ReAct

[toc]

### Abstract

**Reasoning traces** help the model induce, track, and update action plans as well as handle exceptions, while **actions** allow it to interface with and gather additional information from external sources such as knowledge bases or environments.

**ReAct**, a prompt-based paradigm that **synergizes reasoning and acting** in LLMs. LLMs can generate both reasoning traces and task-specific actions in an interleaved manner.

### ReAct : Synergizing REasoning + ACTing

Consider a general setup of an agent interacting with an environment for task solving.

At time step $t$, the agent receives an observation $o_t \in O$ from the environment and takes an action $a_t \in A$ according to a policy
$$
\pi(a_t \mid c_t)
$$

where the context is

$$
c_t = (o_1, a_1, \cdots, o_{t-1}, a_{t-1}, o_t)
$$

The difficulty is that the mapping from context to action, $c_t \mapsto a_t$, can be highly implicit and may require extensive computation. ReAct addresses this by augmenting the agent’s action space

$$
\hat{A} = A \cup L
$$

where $A$ is the original task-specific **action space** and $L$ is the space of language. A language action $\hat{a}_t \in L$ is called a **thought** or **reasoning trace**. Unlike a normal action, a thought does not affect the external environment and produces no observation feedback. Instead, it composes useful information by reasoning over the current context and updates the context

$$
c_{t+1} = (c_t, \hat{a}_t)
$$

This updated context then supports future reasoning or acting.

```python
context = [initial_observation_or_task_input]
done = False

while not done:

    react_step = LLM.generate(context)

    if react_step.type == "thought":
        context.append(react_step)

    elif react_step.type == "action":
        context.append(react_step)

        if react_step.name == "Finish":
            answer = react_step.input
            done = True
            break

        observation = environment.step(react_step)
        context.append(observation)

return answer
```

```text
Question / Task: {input}

Thought 1: {reasoning about what to do}
Action 1: {tool_or_environment_action}
Observation 1: {feedback from environment}

Thought 2: {reasoning based on observation}
Action 2: {next action}
Observation 2: {feedback}

...

Thought N: {final reasoning}
Action N: Finish[{answer}]
```

For the tasks where reasoning is of primary importance, like knowledge-intensive reasoning tasks, we alternate the generation of thoughts and actions so that the task-solving trajectory consists of multiple **thought-action-observation steps**.

In contrast, for decision making tasks that potentially involve a large number of actions, thoughts only need to appear sparsely in the most relevant positions of a trajectory, so we let the language model decide the asynchronous occurrence of thoughts and actions for itself.

Since decision making and reasoning capabilities are integrated into a large language model, ReAct enjoys several unique features

+ Intuitive and easy to design.
+ General and flexible.
+ Performant and robust.
+ Human aligned and controllable.

### Knowledge-Intensive Reasoning Tasks

For multi-hop question answering and fact verification, ReAct is used in a **question-only setup**. The model receives only the question or claim as input and must rely on either its internal knowledge or information retrieved from an external environment.

Multi-hop question answering example

```
Question: Which magazine was started first, Arthur’s Magazine or First for Women?

Thought 1: I need to search Arthur’s Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur’s Magazine]
Observation 1: Arthur’s Magazine was an American literary periodical published in Philadelphia in the 19th century.

Thought 2: Arthur’s Magazine was started in 1844. I need to search First for Women next.
Action 2: Search[First for Women]
Observation 2: First for Women is a woman’s magazine ... The magazine was started in 1989.

Thought 3: 1844 < 1989, so Arthur’s Magazine was started first.
Action 3: Finish[Arthur’s Magazine]
```

Fact verification example

```
Claim: Stranger Things is set in Bloomington, Indiana.

Action 1: Search[Stranger Things]
Observation 1: Stranger Things is set primarily in the fictional town of Hawkins, Indiana.

Action 2: Finish[REFUTES]
```

### Decision Making Tasks

For decision making tasks, ReAct is designed to support long-horizon acting in environments with sparse rewards. The model must maintain high-level goals, track subgoals, and decide what to do next based on observations.

```
Act 1: Think [First, I need to find a peppershaker.
It is more likely to appear in cabinets, countertops, ...]

Act 2: Go to cabinet 1
Obs 2: On the cabinet 1, you see a vase 2.

...

Act 6: Go to countertop 3
Obs 6: On the countertop 3, you see an apple 1, a bread 1,
       a peppershaker 1, and a vase 3.

Act 7: Take peppershaker 1 from countertop 3
Obs 7: You pick up the peppershaker 1 from the countertop 3.

Act 8: Think [Now I find a peppershaker 1.
Next, I need to put it in/on drawer 1.]

Act 9: Go to drawer 1
Obs 9: Drawer 1 is closed.

Act 10: Open drawer 1
Obs 10: You open drawer 1.

Act 11: Put peppershaker 1 in/on drawer 1
Obs 11: You put peppershaker 1 in/on the drawer 1.
```

