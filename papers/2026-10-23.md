# arxiv LLM daily — 2026-10-23

the 30 most recent papers from cs.CL and cs.AI.

### [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](http://arxiv.org/abs/2610.31667v1)
_Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn_ • 2026-10-22

Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool...

### [Cost-Aware Abstention for LLM-Based IT Ticket Classification](http://arxiv.org/abs/2610.31657v1)
_Sachin Gupta_ • 2026-10-22

Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ti...

### [METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](http://arxiv.org/abs/2610.31656v1)
_Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah_ • 2026-10-22

Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories...

### [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](http://arxiv.org/abs/2610.31650v1)
_Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, +2 more_ • 2026-10-22

Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchm...

### [Low-Bit N-Gram Embeddings for Language Models](http://arxiv.org/abs/2610.31646v1)
_Stephen Chung, Wenyu Du_ • 2026-10-22

Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: DeepSeek-V4.1-Fla...

### [Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](http://arxiv.org/abs/2610.31639v1)
_Gabriele Dominici, Teague McMillan, Fazl Barez, Marc Langheinrich, Martin Gjoreski_ • 2026-10-22

Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling the model to deri...

### [Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2](http://arxiv.org/abs/2610.31636v1)
_Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan_ • 2026-10-22

Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compiles each finding...

### [Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](http://arxiv.org/abs/2610.31624v1)
_Barış Alparslan, Sandy Tanwisuth, Caleb Petterson_ • 2026-10-22

Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of po...

### [Bilingual Language Models Capture Cross-Linguistic Influence in Second-Language Reading](http://arxiv.org/abs/2610.31620v1)
_Abderrahmane Issam, Irene E. Winther, Stefan L. Frank_ • 2026-10-22

While monolingual language model (LM) surprisal is widely established as a predictor of reading times, it cannot capture the non-native (L2) reading dynamics that are shaped by the reader's first language (L1). In this work, we investigate whether the cross-lingual transfer within bilingual models aligns with human...

### [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](http://arxiv.org/abs/2610.31606v1)
_Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, Thaís Gaudêncio, Yuri Malheiros, +1 more_ • 2026-10-22

Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with on...

### [Simulated Control Evals](http://arxiv.org/abs/2610.31593v1)
_Jeffrey Olmo, David Zhang, Tyler Tracy_ • 2026-10-22

Control evaluations measure whether safeguards can prevent an AI model from causing undesired outcomes even when it is intentionally trying to do so. These evaluations typically use purpose-built control settings and extrapolate their results to a model's deployment. However, the effectiveness of safeguards in deplo...

### [VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act](http://arxiv.org/abs/2610.31588v1)
_Robin Quériaux, Solveig Bachellery, Léa Déléris, Saurabhsingh Rajput, Mariam Barry, +2 more_ • 2026-10-22

Institutions that deploy large language models in regulated settings often need technical evidence of responsible AI practices before approving a deployment. COMPL-AI provides a technical interpretation of the EU AI Act that organises this evidence under six principle groups and eighteen technical requirements, twel...

### [Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination](http://arxiv.org/abs/2610.31586v1)
_Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera, Aritz Bilbao-Jayo, Aitor Almeida_ • 2026-10-22

Accuracy on medical examinations is common evidence offered for the clinical use of language models, yet a health system that intends to run an open model on its own hardware needs to know considerably more: whether the model recognizes when it is likely to be wrong, whether medical fine-tuning improves this ability...

### [Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration](http://arxiv.org/abs/2610.31579v1)
_Deepthika S, Pawni Yadav, B. Sankar_ • 2026-10-22

Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it? In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five...

### [What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models](http://arxiv.org/abs/2610.31576v1)
_Jinya Sakurai, Xun Xu, Jaehong Yoon_ • 2026-10-22

Masked diffusion language models generate tokens in parallel, but their efficiency depends on which predictions are committed. Learned unmasking policies improve the speed--accuracy trade-off, yet differ in supervision, inputs, and capacity, obscuring which choices matter. We view supervised policies as distilling a...

### [Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure](http://arxiv.org/abs/2610.31573v1)
_Pellegrino Casoria, Simon Pietro Romano_ • 2026-10-22

In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these prac...

### [When to Follow the Teacher: Advantage-Based On-Policy Distillation](http://arxiv.org/abs/2610.31563v1)
_Mahdi Sabbaghi, George Pappas, Hamed Hassani, Adel Javanmard_ • 2026-10-22

Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the student to follow the teacher at every state of the trajectory, assuming that teacher guidance is always beneficial....

### [Diffusion Language Models for Perplexity-Aware Black-Box Attacks](http://arxiv.org/abs/2610.31558v1)
_Ali Al-Lawati, Elsayed Eshra, Dongwon Lee, Suhang Wang_ • 2026-10-22

\emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned fro...

### [Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems](http://arxiv.org/abs/2610.31553v1)
_Humza Akhtar, Brian Freeman_ • 2026-10-22

Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separately. Classifying, linking, and docume...

### [An Empirical Study of Recent Large Language Models for Knowledge Graph to Text Generation on Standard Benchmarks](http://arxiv.org/abs/2610.31529v1)
_Priyanka, Renaud Delbru, Souhail Bakkali, Mickaël Coustaty, Antoine Doucet_ • 2026-10-22

Knowledge graph-to-text (KG-to-text) generation verbalizes a set of knowledge graph triples into fluent natural language. While fine-tuned encoder-decoder models have long been the standard approach, recent LLMs are becoming increasingly competitive. We benchmark recent LLMs against fine-tuned encoder-decoder models...

### [Beyond Causal Masks: Auditing and Localizing Hidden Future-Token Leakage in Adaptive Sequence Models](http://arxiv.org/abs/2610.31522v1)
_Huiting Liu, Jinsong Wu_ • 2026-10-22

Hidden future-token leakage can create false architectural gains: an autoregressive model may appear substantially better under teacher-forced evaluation while its free-running generation deteriorates. We investigate this failure in an adaptive residual-routing decoder whose sequence-level routing summary exposes pr...

### [Jev-DLC: Decision-Level Continual Learning from Typed Feedback](http://arxiv.org/abs/2610.31521v1)
_Yangyang Feng, Jianle Gan, Zhuoyan Feng, Chengwei Qin_ • 2026-10-22

Individual preferences often become visible only after deployment, when a user accepts one decision or revokes it in favor of another. Jev-style typed interfaces make this feedback explicit by identifying the selected action and, under revocation, the decision it replaces. We study how these consequences persist acr...

### [The Geometry of Metaphor: Probing and Steering Metaphor Representations in Large Language Models](http://arxiv.org/abs/2610.31520v1)
_Shihui Li, Mette Andersen, Martha Lewis_ • 2026-10-22

Metaphor is a crucial aspect of human cognition. As such, we would like to understand how it is represented in large language models (LLMs) and how it might be controlled. We use mechanistic interpretability techniques to identify causal subspaces in a range of LLMs covering different architectures and sizes. We sho...

### [From Prompt Rules to Golden Data Model: Production-Scale Generation of Personalized, Compliant Pharmaceutical Claims](http://arxiv.org/abs/2610.31519v1)
_Suyash Mishra, Qiang Li, Subhabrata Adak, Upender Phogat, Srikanth Patil, +1 more_ • 2026-10-22

Large language models (LLMs) are increasingly used to generate domain-specific commercial & medical content (e.g., claims, statements, and promotional phrases) in regulated industries such as pharmaceuticals. However, ensuring its regulatory compliance, factual accuracy, and audience-specific personalization remains...

### [Towards User Simulators That Stay On Task And Still Sound Natural](http://arxiv.org/abs/2610.31512v1)
_Mustafa Omer Gul, Philippe Laban, Tanya Goyal, Jennifer Neville_ • 2026-10-22

Users increasingly rely on AI systems for extended, multi-turn tasks, yet evidence indicates that LLM-based system performance degrades over prolonged interaction. To evaluate and improve AI assistants in such settings, we need user simulators that faithfully follow complex user intents while exhibiting realistic co...

### [DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination](http://arxiv.org/abs/2610.31511v1)
_Ziyi Jiao, Heng Zhang, Drishti Regmi, Xiaokang Ye, Lianhui Qin, +1 more_ • 2026-10-22

Coordinating two players in a cooking task requires a vision-language agent to track changing scene states, sequence recipe steps, and allocate shared resources under a time budget. We introduce an Overcooked-inspired benchmark for evaluating these capabilities in Unreal Engine environments constructed using coding...

### [FairFRESH: A Neuro-Symbolic Framework for Fair and Explainable Household Food Recommendation](http://arxiv.org/abs/2610.31506v1)
_Kodur Sai Vinay Sathvik, Kakoli Bora, Tejaswini R. M_ • 2026-10-22

Recommender systems typically serve one user at a time. However, in households, members share a finite pantry and follow different dietary rules, making independent recommendations prone to resource conflicts and dietary violations. We formulate household food recommendation as constrained fair division and present...

### [SABLE: Scalable Affine Bayesian Latent-space Exploration](http://arxiv.org/abs/2610.31495v1)
_Erik Bodin, Lisa Maria Kreusser, Donney Fan, Henry Moss, Geoff Pleiss, +1 more_ • 2026-10-22

Complex objects such as engineering designs and proteins are often difficult to optimise because their design spaces exhibit high-dimensional structure and objective evaluations are expensive. Generative models provide continuous latent representations, but their latent spaces can have thousands to tens of thousands...

### [Training Small Language Models for Transferable Tool Selection](http://arxiv.org/abs/2610.31483v1)
_Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon, Artem Kuriksha, Daniel Jiang, +2 more_ • 2026-10-22

As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which are actually needed. Recent work inste...

### [MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models](http://arxiv.org/abs/2610.31478v1)
_Khaled Waleed Dawoud, Muhammad Zaigham Zaheer, Khan Muhammad, Muhammad Haris Khan_ • 2026-10-22

Vision-Language Models (VLMs) have shown strong potential for video anomaly detection, but dense frame-level inference makes them impractical for real-time deployment. Existing acceleration commonly relies on uniform sampling, which ignores content dynamics and can either waste computation on static segments or miss...

_snapshot taken at 2026-10-23T17:56:51+00:00_
