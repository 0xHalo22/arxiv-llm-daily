# arxiv LLM daily — 2026-11-03

the 30 most recent papers from cs.CL and cs.AI.

### [Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations](http://arxiv.org/abs/2611.03647v1)
_Jason Jingzhou Liu, Tony Tao, Deepak Pathak, Ruslan Salakhutdinov_ • 2026-11-02

Sensorized human demonstrations offer scalable data for mobile manipulation, but embodiment differences complicate policy learning. We present Pixel-UMI, a pipeline for learning environment-aware whole-body policies from human data. We first introduce Environment-Aware Retargeting (EAR), which combines reconstructed...

### [Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation](http://arxiv.org/abs/2611.03648v1)
_Tony Tao, Jason Jingzhou Liu, Ruslan Salakhutdinov, Deepak Pathak_ • 2026-11-02

General-purpose mobile manipulation requires a combination of capable robot hardware, scalable demonstration collection, expressive whole-body control, and effective policy learning. Yet these components are often developed independently, creating mismatches that limit the capabilities of the complete system. We pre...

### [From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles](http://arxiv.org/abs/2611.03641v1)
_Paulius Skaisgiris, Thomas Pammer, Veronika Semmelrock, Mykyta Ielanskyi, Maximilian Heisinger, +1 more_ • 2026-11-02

Chain-of-Thought (CoT) generation has substantially improved the performance of Large Language Models (LLMs) on complex reasoning tasks, including code generation, data analysis, and exam-style question answering. Despite these advances, purely neural LLMs continue to struggle with elementary logical reasoning probl...

### [WebHarbor: Docking Real Websites for Evolving GUI Agent Environments](http://arxiv.org/abs/2611.03634v1)
_Zhaoyang Wang, Qianhui Wu, Boyu Gou, Demi Wang, Jiacheng Zhang, +52 more_ • 2026-11-02

GUI web agents require realistic and interactive environments that remain stable during both evaluation and training. Live website evaluation suffers from changing content, access restrictions, and limited coverage of authenticated workflows, while existing synthetic environments for training often lack functional d...

### [D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models](http://arxiv.org/abs/2611.03622v1)
_Marius Memmel, Shawn Yin, Urvi Rutia, Angad Wadhwa, Eldon Li, +7 more_ • 2026-11-02

Vision-Language Models (VLMs) hold promise for zero-shot video task-progress estimation in robot learning, yet existing frameworks frequently suffer from confirmation bias, hallucinating progress in failed executions due to implicit success assumptions or relative temporal ranking designs. Naive prompting of frontie...

### [Strategist: Evolving Reasoning with Agents](http://arxiv.org/abs/2611.03618v1)
_Taiming Lu, Qi Xu, Zhigang Hua, Zhuang Liu_ • 2026-11-02

A model is only half of an AI agent system. The other half is the inference strategy: the reasoning procedure that turns model calls into a response. Today that second half is written by hand, and the experience of building one strategy never carries to the next. We introduce Strategist, a meta-agent that evolves in...

### [Tracing the Scientific Discovery Capacity of LLMs to Their Training Data](http://arxiv.org/abs/2611.03617v1)
_Arda Uzunoglu, Mahler Revsine, Michael Schatz, Benjamin Van Durme, Mehrdad Farajtabar, +2 more_ • 2026-11-02

Large language models (LLMs) show growing promise for scientific discovery, yet basic questions remain about what enables reliable discovery. How can we trace the scientific discovery capacity of LLMs to their training data? We study this question as one of missing probability mass and develop a theoretical account...

### [ufakzeka-kulak: Building and Evaluating a 31.6M-Parameter Turkish Speech Recognizer from Scratch](http://arxiv.org/abs/2611.03605v1)
_Sait Furkan Teke_ • 2026-11-02

ufakzeka-kulak is an open Turkish speech-to-text model of 31.6M parameters, a FastConformer encoder with a token-and-duration transducer (TDT) and a CTC head, trained from scratch and released under Apache-2.0. It writes cased, punctuated Turkish with numbers as words. Its 4,977 training hours come from sources whos...

### [DiabAgent: Toward Agentic Physiological Control](http://arxiv.org/abs/2611.03601v1)
_Chengxi Li, Shaoxuan Li, Deyao Hong, Qingle Liu, Yi Huang, +11 more_ • 2026-11-02

As pretraining scales, medical language models have advanced rapidly in clinical question answering. Their ability to achieve effective physiological control through sustained intervention still lacks systematic quantitative evaluation. Type 1 diabetes provides a concrete setting: impaired insulin secretion creates...

### [Four Bridges: Measuring Deception Propensity in a Multi-Agent Game](http://arxiv.org/abs/2611.03600v1)
_Raphael Casey, Michael Simeone, Alberto Tosato, Florian Ernst, Kemal El Moujahid, +2 more_ • 2026-11-02

AI agents are increasingly deployed in settings where they interact and coordinate with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure the model to deceive. We study deception that emerges in multi-agent interaction without any instruction to deceive. We introduce...

### [Spacetime Emergence in the Memory of a Learning Agent](http://arxiv.org/abs/2611.03596v1)
_Philip A. LeMaitre, T. Rick Perche_ • 2026-11-02

We show that the causal structure of spacetime can emerge within the memory of a learning agent performing a quantum information task. We train a model-based reinforcement-learning agent to maximize the quantum mutual information between localized quantum probes interacting with a quantum field in Minkowski spacetim...

### [Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models](http://arxiv.org/abs/2611.03592v1)
_Thomas Decker, Volker Tresp_ • 2026-11-02

Time series foundation models (TSFMs) are increasingly used for probabilistic forecasting across diverse domains, yet the reliability of their uncertainty estimates remains poorly understood. In this work, we study uncertainty calibration in probabilistic TSFMs from a broader methodological and empirical perspective...

### [FedReady: Bounded Agents for Federation Formation](http://arxiv.org/abs/2611.03586v1)
_Ziyue Xu, Holger R. Roth, Chester Chen, Peter Cnudde_ • 2026-11-02

Federated learning (FL) runtimes standardize aggregation and deployment, but each new study still requires federation formation: selecting task-eligible sites and preparing their local data and task code for federated training or analysis. This preparation recurs when the target changes, while raw records and site-p...

### [Sonar-MoE: In-Backward Expert Updates for Memory-Efficient Mixture-of-Experts Training](http://arxiv.org/abs/2611.03577v1)
_Avni Mittal, Avinash Anand, Ashutosh Kumar, Dikshant Kukreja, Kritarth Prasad, +5 more_ • 2026-11-02

Most parameters of a Mixture-of-Experts (MoE) model belong to its experts, and standard training keeps every expert gradient in GPU memory until the optimizer step. This memory grows with the number and size of the experts, so it rises as MoE models scale. We introduce Sonar-MoE, which updates each expert tensor dur...

### [NitiBench+: A Temporal Thai Legal Question Answering Benchmark Across 17 Domains](http://arxiv.org/abs/2611.03576v1)
_Pawitsapak Akarajaradwong, Sarana Nutanong, Chompakorn Chaksangchaichot_ • 2026-11-02

Law changes over time. A court decides a case under the law in force on that day, and legal QA benchmarks grade answers against today's law. We checked 156,650 decisions of four Thai courts. Up to 67% of them cite law that has since been amended or repealed. We introduce NitiBench+, the sequel of our NitiBench, a Th...

### [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](http://arxiv.org/abs/2611.03575v1)
_Wei-Lin Chen, Zhepei Wei, Xinyu Zhu, Yu-Min Tseng, Tzu-Han Lin, +1 more_ • 2026-11-02

Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated files, weakening access controls, or...

### [PlantVLM-Edge: Quantized Vision-Language Models for On-Device Crop Health Diagnosis](http://arxiv.org/abs/2611.03557v1)
_Gaurab Wagle, Bishal Adhikari, Jiajia Li, Xiaolei Huang, Dong Chen_ • 2026-11-02

Timely and accurate crop health diagnosis is essential for sustainable agricultural production, yet accurate diagnosis often requires expert knowledge that is not readily available. Recent vision-language models (VLMs) have demonstrated remarkable capabilities in visual understanding, reasoning, and natural-language...

### [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](http://arxiv.org/abs/2611.03555v1)
_Farooq Shaikh, Biagio Montaruli_ • 2026-11-02

The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model compliance with poisoned instructions...

### [Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL](http://arxiv.org/abs/2611.03551v1)
_Marianne Menglin Liu, Rongguang Wang, Zheng Wang, Yewen Wang, Leonid Boytsov, +3 more_ • 2026-11-02

LLM coding agents can increasingly automate model post-training, but whether they can act as forward-deployed engineer (FDE) agents, discovering customer requirements and turning them into deployment decisions, remains unclear. We study this on a real enterprise text-to-SQL engagement: a simulated customer, grounded...

### [An Agentic Framework for Automated Power System Studies and Grid Connection Assessment](http://arxiv.org/abs/2611.03534v1)
_MaoXun Huang, Kshitij Kapoor, Eli Louise_ • 2026-11-02

Connecting new generation and demand to the grid depends on two scarce skills: checking applications against a large, changing body of regulation, and running the network studies that decide where and how a project connects. We present Grid Agents, an AI system that brings both together, and the methodology we use t...

### [Contrastive Adapter Training and Consensus Knowledge Distillation for Multi-Source-Free Domain Adaptation in Skin Cancer Diagnosis](http://arxiv.org/abs/2611.03528v1)
_Ali Abedi, Q. M. Jonathan Wu, Ning Zhang, Farhad Pourpanah_ • 2026-11-02

Skin cancer diagnosis, particularly differentiating melanoma from benign nevi, is challenging due to the visual similarity between lesions. Although convolutional neural networks (CNNs) and vision transformers (ViTs) have shown promising performance, their effectiveness often deteriorates on data from heterogeneous...

### [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](http://arxiv.org/abs/2611.03526v1)
_Abdellah Rahmani, Sean McLeish, Ang Li, Sanae Lotfi, Pascal Frossard, +1 more_ • 2026-11-02

Computer programmers chain together the same reusable computational primitives, for example, conditional statements or loops, but in different orders to implement different algorithms. In contrast, existing language model architectures always execute their layers in the same order. We introduce Library of Layers (Lo...

### [Grading the Unannotated: Insights from the WorkRB Skill Extraction Challenge at RecSys-HR 2026](http://arxiv.org/abs/2611.03525v1)
_Warre Veys, Luis Gasco, Jens-Joris Decorte_ • 2026-11-02

Skill extraction benchmarks score models against a few human-annotated positives and treat every other skill in the vocabulary as equally wrong. At the scale of ESCO (13,939 skills) this binary view can reward models that rank the annotated positive high for the wrong reason, and hides semantically nonsensical predi...

### [PanoTac: A Dense Three-Axis Tactile Sensor for Robust Touch-Centric Manipulation](http://arxiv.org/abs/2611.03520v1)
_Binglin, Wang, Xiaole, Jiang, Zicheng Teng, +5 more_ • 2026-11-02

Contact-rich manipulation benefits from tactile feedback that captures both detailed contact geometry and interaction forces. When scooping grains, contact patterns help infer spoon orientation, while resistance transmitted through the grasp guides motion. To provide these complementary sensing capabilities, we pres...

### [VIAS: Value-Isolating Activation Steering for Multi-Value Alignment and Compliance for Organisations](http://arxiv.org/abs/2611.03518v1)
_Avni Mittal, Avinash Anand, Dikshant Kukreja, Erik Cambria, Rajiv Ratn Shah, +1 more_ • 2026-11-02

Organisations increasingly deploy large language model agents that must follow organisational values. We check whether activation steering, which adds vectors to a model's internal activations during generation without changing its weights, can improve compliance beyond prompting alone. Since most scenarios involve...

### [A Cross-Domain Matrix Engine for Signal Processing and Deep Neural Net Inference](http://arxiv.org/abs/2611.03503v1)
_Mehdi Safarpour_ • 2026-11-02

Matrix multiplication dominates both PHY signal processing and Deep Neural Network (DNN) inference, yet these domains place opposing demands on the matrix engine. Signal processing requires low-latency execution of relatively small matrix operations, whereas DNN inference, particularly at large batch sizes, prioriti...

### [Can AI Do Formal Demography? Why Vaccinating the Oldest Saves Both the Most Lives and the Most Years of Life](http://arxiv.org/abs/2611.03500v1)
_Joshua R. Goldstein, Kenneth W. Wachter_ • 2026-11-02

Can AI contribute to formal demography? We report an experiment in which an AI model, Claude, was asked to explain and then simplify the proof of an earlier result: that vaccinating the oldest against COVID-19 saves both the most lives and the most years of life, because the years saved per person treated rise with...

### [Online Label-Free Gradient Matching for Continual Language Model Training](http://arxiv.org/abs/2611.03496v1)
_Sajjad Pakdamansavoji, Mohammad Reza Rezaei, Ilija Subasic, Pedro Garzon, Radu Paradovschi, +1 more_ • 2026-11-02

Language models in customer-facing products must be continually updated, since the data they serve shifts over time. As retraining on the full accumulated data is impractical, each update should instead run on a small set of examples carrying the training signal of all data seen so far. The strongest current methods...

### [Harder Than the Task: From Technical to Organizational Difficulty in AI Benchmarking](http://arxiv.org/abs/2611.03494v1)
_Victor Barres, Aden Barton, Nicolai J. Foss, Henrik M. Nielsen_ • 2026-11-02

AI benchmarks have made remarkable progress in measuring the ability of AI systems to perform increasingly demanding cognitive and technical tasks. Yet, many of these benchmarks treat technical tasks as the unit of analysis, while much economically valuable work takes place within organizations, where tasks are embe...

### [Playing Dumb: How a Chess Transformer Simulates Users Across Skill Levels](http://arxiv.org/abs/2611.03439v1)
_Difan Jiao, George Eilender, Zhenwei Tang, Ashton Anderson_ • 2026-11-02

Generative models increasingly simulate users at different skill levels in education and AI evaluation. Yet it remains unclear whether lower-skill behavior reflects less internal knowledge or a different use of retained knowledge. This distinction is difficult to study in natural language, where proficiency and rele...

_snapshot taken at 2026-11-03T20:15:39+00:00_
