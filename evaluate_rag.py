import csv
import matplotlib.pyplot as plt
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from bert_score import score as bert_score

# -------------------------------
# 1. Benchmark Set
# -------------------------------
benchmark = [
    {
        "query": "What is the dielectric constant of Cd-based polymer?",
        "gold_doc": "Cd-based_polymer",
        "gold_answer": "Dielectric constant ~6.87, band gap ~3.70 eV"
    },
    # Add more queries here for full evaluation
]

# -------------------------------
# 2. Stub RAG System
# -------------------------------
def run_rag(query):
    # Replace this with your actual retriever + generator
    retrieved_docs = ["Cd-based_polymer", "Organic_polymer_X"]
    generated_answer = "Cd-based polymer has dielectric constant 6.87 and band gap 3.70 eV."
    return retrieved_docs, generated_answer

# -------------------------------
# 3. Compute Metrics
# -------------------------------
smoothie = SmoothingFunction().method1
results = []

for item in benchmark:
    query = item["query"]
    gold_doc = item["gold_doc"]
    gold_answer = item["gold_answer"]

    retrieved_docs, generated_answer = run_rag(query)

    # Retrieval metrics
    recall_at_10 = int(gold_doc in retrieved_docs[:10])
    precision_at_10 = sum([1 for d in retrieved_docs[:10] if d == gold_doc]) / len(retrieved_docs[:10])
    mrr = 0
    for rank, doc in enumerate(retrieved_docs, start=1):
        if doc == gold_doc:
            mrr = 1.0 / rank
            break
    ndcg = 1.0 if retrieved_docs[0] == gold_doc else 0.5 if gold_doc in retrieved_docs[:5] else 0

    # Generation metrics
    bleu = sentence_bleu([gold_answer.split()], generated_answer.split(), smoothing_function=smoothie)
    rouge = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True).score(gold_answer, generated_answer)['rougeL'].fmeasure
    P, R, F1 = bert_score([generated_answer], [gold_answer], lang="en", verbose=False)

    results.append({
        "query": query,
        "recall@10": recall_at_10,
        "precision@10": precision_at_10,
        "MRR": mrr,
        "nDCG@10": ndcg,
        "BLEU": bleu,
        "ROUGE-L": rouge,
        "BERTScore_F1": F1.mean().item()
    })

# -------------------------------
# 4. Save Results to CSV
# -------------------------------
with open("rag_eval_results.csv", "w", newline="") as csvfile:
    fieldnames = results[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for r in results:
        writer.writerow(r)

print("Results saved to rag_eval_results.csv")

# -------------------------------
# 5. Plot Figures (1200 dpi)
# -------------------------------
# Bar chart of retrieval metrics
metrics = ["recall@10", "precision@10", "MRR", "nDCG@10"]
avg_scores = {m: sum(r[m] for r in results)/len(results) for m in metrics}

plt.figure(figsize=(8,6))
plt.bar(avg_scores.keys(), avg_scores.values(), color="skyblue", edgecolor="k")
plt.ylabel("Score")
plt.title("Average Retrieval Metrics")
plt.savefig("retrieval_metrics.png", dpi=1200)
plt.show()

# Scatter plot of BLEU vs ROUGE
bleu_scores = [r["BLEU"] for r in results]
rouge_scores = [r["ROUGE-L"] for r in results]

plt.figure(figsize=(6,6))
plt.scatter(bleu_scores, rouge_scores, c="red", alpha=0.7, edgecolors="k")
plt.xlabel("BLEU")
plt.ylabel("ROUGE-L")
plt.title("Generation Metrics Scatter")
plt.savefig("generation_metrics.png", dpi=1200)
plt.show()
