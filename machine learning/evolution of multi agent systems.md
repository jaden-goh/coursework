Algorithmic for small scale specific problems 
-> Reinforcement for large scale specific problems
--> LLM-Based for large scale general problems

### Algorithmic Previous Use Cases
- Security Games: Full of strategy, research proposed optimization under lack of information
- Pursuit-Evasion Game: Zero Sum imperfect information game, which complicates exponentially with scale and transfer -> We go to reinforcement learning

### Reinforcement Learning Use Cases
- Fraud Detection

- Recommendation Systems: User as environment, item as policy, focus on retention, optimize on return time and session length, DAU as key metric
- - delayed feedback and high training costs
- - to combat that, trained on reinforcing retention from preferences rather than rewards by predicting the preference and learn the reward model automatically

- Ride-hailing

- Financial Trading: Approached with low level RL with supervisor for different market conditions, high level RL to pick the low-level agents dynamically
- - Non Stationary markets, temporal distribution shifts

General limitations of RL based agents:
- Sample inefficient, tasks specific, long-horizon tasks, sparse reward

### LLM-Powered
- 
Limitations, misalignment with environment despite having rich prior knowledge, while RL agents are aligned ith environment but struggle to use prior knowledge
Use LLMs to for RL policy and optimize with PPO by interacting with embodied environments
