"""Single source of truth for the portfolio copy. Every design in this folder renders from it.

Fields marked (html) may contain <strong> and are rendered unescaped. Paths are relative to designs/.
"""

PROFILE = {
    "name": "M. Ahmad Siddiqui",
    "first": "Ahmad",
    "last": "Siddiqui",
    "role": "Machine learning engineer",
    "lead": "I build and measure ML systems that run on small hardware: local LLMs, RAG that has to quote its sources, and on-device vision and speech.",
    "lead_em": "local LLMs",
    "where": "BS Data Science graduate, KFUEIT 2026 · ML Engineer (contract) at Rezinx since Aug 2025 · Rahim Yar Khan, Pakistan",
    "email": "ahmadsiddiqui6127@gmail.com",
    "github": "https://github.com/Copperhorse",
    "linkedin": "https://www.linkedin.com/in/ahmad-siddiqui-559998267",
    "resume": "../data/Ahmad_Siddiqui_Resume.pdf",
    "avatar": "../data/profile.webp",
}

PROJECTS = [
    {
        "id": "picturebook",
        "n": "01",
        "name": "PictureBOOK",
        "tag": "an offline picture-book maker",
        "kind": "Local AI · Speech · Vision",
        "find": "Three models take turns on one 8 GB GPU and turn a spoken story into an illustrated PDF in 6 to 9 minutes. Nothing leaves the laptop.",
        "problem": "A parent types, imports or records a story and gets an illustrated PDF a few minutes later. The child's voice and the family's story stay on the machine.",
        "links": [
            ("Code on GitHub", "https://github.com/Copperhorse/PictureBOOK"),
            ("Research notes", "https://github.com/Copperhorse/PictureBOOK/tree/main/docs/research"),
        ],
        "steps": [
            ("Story in", False), ("Whisper", False), ("Plan (Gemma 4)", False), ("Parent approves characters", True),
            ("Draw (FLUX.2 klein)", False), ("Vision critic", False), ("Human review", True), ("PDF", False),
        ],
        "steps_caption": "Pipeline. Highlighted steps are where a person decides.",
        "hl_label": "person decides",
        "gallery": [
            ("../data/picturebook-1.webp", "Illustration of a girl with long blonde hair tiptoeing into a wooden kitchen with three bowls of porridge on the table"),
            ("../data/picturebook-2.webp", "Illustration of two bears and a small bear cub standing by a kitchen table with three bowls, looking upset"),
            ("../data/picturebook-3.webp", "Illustration of a bear family in a wooden kitchen with bowls of porridge on the table"),
        ],
        "gallery_caption": "Pages from a book generated on the 8 GB laptop GPU (Goldilocks and the Three Bears, crayon style).",
        "built": "A Tauri 2 desktop app. A Rust core owns the book library; a Python FastAPI sidecar runs one GPU job at a time behind a per-launch bearer token and streams progress over SSE. <strong>Every model stage is its own process under a memory-capped systemd scope</strong>, so killing the app, even with SIGKILL, leaves no stray process and no VRAM in use (this is tested).",
        "measured": "Whisper large-v3-turbo: <strong>1.9% word error rate</strong> on 48 synthetic clips. Vision critic: <strong>94.7% accuracy and 99% recall</strong> of deliberate mismatches on 40 synthetic images. About 10 s per image and 6 to 9 minutes per book. 95 sidecar tests and 61 pipeline-rule tests pass, alongside a Rust test suite.",
        "fail": "No model I tried could find extra hands or legs (0 of 3). Redrawing a flagged page fixed only 2 of 13 defects; the other 11 came back in all three redraws. So the critic writes notes for the parent and never acts alone, and a human reviews every page. Silence also became a made-up book until I added a gate for it.",
        "limits": "Tested on one machine (Linux, RTX A2000), English only, and speech was tested on synthetic clips rather than real parents. Not packaged yet.",
        "stack": ["Tauri 2", "Rust", "SvelteKit", "TypeScript", "FastAPI", "llama.cpp", "Whisper", "FLUX.2 klein", "Gemma 4"],
    },
    {
        "id": "template-rag",
        "n": "02",
        "name": "Template_RAG",
        "tag": "retrieval that has to show its evidence",
        "kind": "RAG · Retrieval evaluation",
        "find": "A RAG library for documents and code where an answer only counts if every quote is found word for word in the chunk it cites.",
        "problem": "Most RAG demos cannot tell you when they are wrong. This one only returns an answer if every quote can be found, word for word, in the chunk it cites.",
        "links": [
            ("Code on GitHub", "https://github.com/Copperhorse/Template_RAG"),
            ("Eval results", "https://github.com/Copperhorse/Template_RAG/tree/main/evals/results"),
        ],
        "steps": [
            ("Ingest", False), ("Chunk (Markdown / AST)", False), ("Quality gate", True), ("Dense + BM25", False),
            ("RRF", False), ("Rerank", False), ("Quote gates", True),
        ],
        "steps_caption": "Pipeline. Highlighted steps reject weak input or unsupported answers.",
        "hl_label": "gate",
        "gallery": [],
        "gallery_caption": "",
        "built": "Hybrid retrieval (EmbeddingGemma plus SQLite FTS5 BM25, fused with reciprocal rank fusion) and a listwise reranker. Python is chunked along its AST. Ingest-time gates keep tables of contents, licence headers and generated code out of the index, and answer gates locate each quote in its source chunk and store the chunk's exact text. A Streamlit UI shows every stage's rank. It started from the ingestion and verification code of QuestionPrep, generalised into a reusable library.",
        "measured": "Frozen corpus and gold sets, with bootstrap confidence intervals and paired significance tests. The reranker added <strong>+18.6 recall@1</strong> on 70 hand-written queries and <strong>+25.5</strong> on 149 synthetic ones. <strong>513 tests</strong> and CI.",
        "fail": "A web-trained cross-encoder (ms-marco) never helped, and letting it replace the ranking lost 14 points of recall@5 on code, so it votes alongside dense and BM25 instead. The best reranker is non-commercial (CC-BY-NC); the README says so and names a permissive fallback.",
        "limits": "",
        "stack": ["Python", "SQLite FTS5", "sentence-transformers", "Streamlit", "pytest", "GitHub Actions"],
    },
    {
        "id": "dlrag",
        "n": "03",
        "name": "DLRAG",
        "tag": "does a tool-using agent beat plain RAG for a small model?",
        "kind": "LLM evaluation · Agents",
        "find": "Retrieval took a 2B model from 3.3% to 33.3% of runs passing every test. Agent tools added nothing detectable.",
        "problem": "A 2B model writes PyTorch code from a textbook and its repository. Is it better to paste retrieved passages into the prompt once, or to let the model call search tools?",
        "links": [
            ("Code on GitHub", "https://github.com/Copperhorse/DLRAG"),
            ("Full report", "https://github.com/Copperhorse/DLRAG/blob/main/REPORT.md"),
        ],
        "steps": [],
        "steps_caption": "",
        "hl_label": "",
        "gallery": [],
        "gallery_caption": "",
        "built": "56 execution-graded tasks: 32 for tuning and 24 frozen for the final test, with a sha256 manifest checked before analysis. Six arms on one model, settings tuned on the dev tasks and the test run once, paired bootstrap intervals, and a parity check that proves each pair of arms gets an identical first message.",
        "measured": "<strong>Retrieval is what matters:</strong> 3.3% of runs passed every test with nothing, 33.3% with passages plus a repository map. <strong>Tools added nothing detectable</strong> (−1.7 points, 95% CI −10.8 to +6.7) at about 3× the tokens. A 4B model was not measurably better than the 2B. The repository map cut import failures from 34.2% to 9.2%.",
        "fail": "The original question, whether a small model plus retrieval can replace a much bigger one, was not tested: the largest model was 4B. The report says so. A fine-tuning arm was shelved because its training data was templated prompts nobody would ask.",
        "limits": "",
        "stack": ["Python", "uv workspace", "llama.cpp", "Agno", "BM25 + dense (fastembed)", "Docling"],
    },
    {
        "id": "questionprep",
        "n": "04",
        "name": "QuestionPrep",
        "tag": "interview practice from your own documents",
        "kind": "Full-stack ML · Final-year project",
        "find": "Upload a PDF, a local LLM writes the questions, and answers are scored in three stages. Stress detection runs in the browser. My final-year project.",
        "problem": "Upload a PDF, a local LLM writes interview questions with reference answers, and you answer by typing or speaking. Everything runs on your own machine.",
        "links": [("Code on GitHub", "https://github.com/Copperhorse/QuestionPrep")],
        "steps": [
            ("PDF", False), ("Docling", False), ("Chunks", False), ("LLM questions", False),
            ("Verification gates", True), ("Interview", False), ("3-stage scoring", True),
        ],
        "steps_caption": "Pipeline. Highlighted steps check generated questions and score answers.",
        "hl_label": "check",
        "gallery": [],
        "gallery_caption": "",
        "built": "FastAPI, SQLite and ChromaDB with a llama.cpp server. Answers are scored in three stages (fuzzy match, then a BGE bi-encoder, then a DeBERTa NLI cross-encoder), with a guard for cut-off answers and a cap when the answer contradicts the reference. Difficulty adapts to a running average of the score. <strong>Stress detection runs in the browser</strong>: a TCN on ONNX Runtime Web with a hand-written DSP front end (FFT, mel filterbank, DCT-II). Also token auth, single-use SSE tickets and upload validation.",
        "measured": "<strong>460 tests</strong> (plus 42 GPU and LLM tests run separately), CI, and a gold set used to tune the question-verification checks.",
        "fail": "The scoring has known weaknesses that I documented instead of hiding: an answer cut off mid-sentence can still score 0.8 to 1.0, and a correct answer in different terminology scores about 0.28. The stress detector also produced false positives on stutters.",
        "limits": "",
        "stack": ["FastAPI", "SQLite", "ChromaDB", "llama.cpp", "sentence-transformers", "ONNX Runtime Web", "JavaScript"],
    },
]

ALSO = [
    {"kind": "NLP · LoRA", "name": "Hybrid profanity detection and rewriting",
     "text": "A LoRA-tuned DistilBERT classifier (95.67% accuracy) labelled the synthetic training data for a QLoRA-tuned LFM2.5-1.2B, which classifies reviews and then switches its adapter off to rewrite the profane ones.",
     "url": "https://github.com/Copperhorse/profanity_distilbert_lora"},
    {"kind": "RAG · Legal NLP", "name": "PocketLaw",
     "text": "A retrieval-augmented chatbot over Pakistani banking law, using dense retrieval and a LoRA fine-tuned LLM.",
     "url": "https://github.com/Copperhorse/PocketLaw"},
    {"kind": "Computer vision", "name": "Currency classifier for the visually impaired",
     "text": "EfficientNet-B0 transfer learning for Pakistani banknotes, with a confidence gate so ambiguous frames are never spoken aloud.",
     "url": "https://github.com/Copperhorse/CurrencyClassification"},
    {"kind": "Machine learning · Security", "name": "Edge-IIoT attack detection",
     "text": "Multi-class network intrusion classifier (random forest and XGBoost) reaching 94.67% accuracy with class-imbalance handling.",
     "url": "https://github.com/Copperhorse/edge_iiot"},
]

EXPERIENCE = [
    {"when": "Aug 2025 – present", "place": "Remote", "role": "ML Engineer (contract)", "org": "Rezinx",
     "bullets": [
         "Fine-tuned language models with LoRA for downstream production use cases.",
         "Built a recommendation engine with Superlinked.",
         "Evaluated several embedding models for a job-classification task.",
         "Built a computer-vision hazard detector for fire, knives and stairs that estimates how close each one is to a child.",
         "Built a Grafana dashboard for monitoring models and systems.",
     ]},
    {"when": "May – Jun 2025", "place": "Remote", "role": "Machine Learning Intern", "org": "Arch Technologies",
     "bullets": [
         "Built machine learning models to find patterns in large datasets.",
         "Prepared data and engineered features to improve model accuracy.",
         "Ran experiments to evaluate models and recommended adjustments.",
     ]},
    {"when": "Jun – Jul 2026", "place": "Lahore", "role": "Network Administration Intern", "org": "Ittehad Chemicals",
     "bullets": ["Worked on network administration tasks covering microwave WAN links, OSPF routing, Cisco and MikroTik equipment, and Windows Server Active Directory."]},
]

SKILLS = [
    ("ML and deep learning", "Python, SQL, PyTorch, scikit-learn, XGBoost, Hugging Face Transformers, LoRA and QLoRA fine-tuning, ONNX Runtime, llama.cpp"),
    ("NLP and retrieval", "RAG, hybrid search (BM25 + dense), reranking, embeddings, ChromaDB, NLI, Docling, evaluation (recall@k, MRR, bootstrap confidence intervals)"),
    ("Vision and speech", "YOLOv8 / YOLO11, EfficientNet, ByteTrack, OpenCV, TCN, Whisper"),
    ("Backend and tooling", "FastAPI, REST APIs, SSE, SQLite, Polars, DuckDB, Docker, Grafana, Superlinked, Git, pytest, GitHub Actions, Linux, uv"),
]

ABOUT = [
    "I like ML work where the interesting part is finding out what actually works. My projects report what failed next to what succeeded, because that is the part another engineer needs.",
    "<strong>Education:</strong> BS Data Science graduate, Khwaja Fareed University of Engineering and Information Technology (KFUEIT), 2022 – 2026, CGPA 3.35 / 4.00.",
    "Away from a keyboard I read mythology and work through logic puzzles.",
]
